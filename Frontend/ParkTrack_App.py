import sys
from datetime import datetime
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, 
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, 
    QComboBox, QSpinBox, QGridLayout, QFrame, QTextEdit, QScrollArea,
    QStackedWidget, QCheckBox
)
from PyQt6.QtCore import Qt
from ParkTrack_Model import ParkingSlotWidget
from ParkTrack_Style import Styles
from ParkTrack_Engine import ParkingEngine
from ParkTrack_Dialogs import Dialogs
from ParkTrack_Receipt import Receipt
from ParkTrack_Billing import BillingEngine

class ParkingSystemApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ParkTrack Parking Management System")
        self.setMinimumSize(1150, 720)
        
    #-------------------NEW------------------------------    
        self.engine = ParkingEngine(24, 24)
        self.car_filter_status = "All"
        self.moto_filter_status = "All"
        
        self.car_slot_ui_elements = {}
        self.moto_slot_ui_elements = {}
        
        self.subtext_labels = []
        self.rate_subtext_labels =[]
    #-------------------NEW------------------------------    
    
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(15, 15, 15, 15)
        self.main_layout.setSpacing(15)
        
        self.left_canvas_container = QWidget()
        self.left_canvas_layout = QVBoxLayout(self.left_canvas_container)
        self.left_canvas_layout.setContentsMargins(0, 0, 0, 0)
        
    #-------------------NEW------------------------------    
        # Setup left side grid maps first
        self.ParkTrack_banner()
        self.ParkTrack_view_switcher_and_maps()
        self.main_layout.addWidget(self.left_canvas_container, stretch=3)
        
        # Setup right sidebar (creates self.spot_selector, self.active_spot_selector, etc.)
        self.right_sidebar_container = QFrame()
        self.right_sidebar_container.setFixedWidth(380)
        self.right_sidebar_container.setObjectName("rSidebar")
        self.right_sidebar_layout = QVBoxLayout(self.right_sidebar_container)
        self.right_sidebar_layout.setContentsMargins(10, 10, 10, 10)
        self.right_sidebar_layout.setSpacing(10)
    #-------------------NEW------------------------------    

        self.control_tabs = QTabWidget()
        
        self.ParkTrack_checkin_tab_panel()
        self.ParkTrack_billing_tab_panel()
        self.ParkTrack_history_tab_panel()
        self.right_sidebar_layout.addWidget(self.control_tabs, stretch=1)
        
        log_title = QLabel("System Activity Log")
        log_title.setObjectName("logTitle")
        self.right_sidebar_layout.addWidget(log_title)
        
        self.activity_log_box = QTextEdit()
        self.activity_log_box.setObjectName("activityLogBox")
        self.activity_log_box.setReadOnly(True)
        self.activity_log_box.setFixedHeight(150)
        self.right_sidebar_layout.addWidget(self.activity_log_box)
        
        self.main_layout.addWidget(self.right_sidebar_container, stretch=1)
        
    #-------------------NEW------------------------------    
        # Connect map_stack signal AFTER all widgets are instantiated
        self.map_stack.currentChanged.connect(lambda idx: self.update_ui())
    #-------------------NEW------------------------------    
        
    #-------------------NEW------------------------------    
        Styles.apply_widget_styles(self)
        # 4. Populate UI state
    #-------------------NEW------------------------------    
        self.update_ui()
        self.log_message("System loaded successfully.")         
    def apply_qss(self, qss_filename):
        if os.path.exists(qss_filename):
            with open(qss_filename, "r") as f:
                self.setStyleSheet(f.read())
        else:
            print(f"Warning: Stylesheet file '{qss_filename}' not found.")

    # BANNER LAYOUT WIDGETS
    def ParkTrack_banner(self):
        banner = QFrame()
        banner.setObjectName("Banner")
        banner.setFixedHeight(70)
        banner_layout = QHBoxLayout(banner)
        banner_layout.setContentsMargins(15, 0, 15, 0)
        
        p_logo = QLabel("P")
        p_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        p_logo.setFixedSize(40, 40)
        p_logo.setObjectName("Logo")
        banner_layout.addWidget(p_logo)
        
        title = QLabel("TIP QC Hub Facility")
        title.setObjectName("bannerTitle")
        banner_layout.addWidget(title)
        banner_layout.addStretch()
        
    #-------------------NEW------------------------------    
        self.total_stat = QLabel("24")
        self.vacant_stat = QLabel("0")
        self.occupied_stat = QLabel("0")
    #-------------------NEW------------------------------    
        
        stats_configurations = [
            ("Total Spaces", self.total_stat, "white"),
            ("Available", self.vacant_stat, Styles.ACCENT_GREEN.name()),
            ("Occupied", self.occupied_stat, Styles.ACCENT_RED.name())
        ]
        for text, metric_widget, font_color in stats_configurations:
            box = QFrame()
            box.setFixedSize(95, 50)
            box.setObjectName("bannerBox")
            box_vbox = QVBoxLayout(box)
            box_vbox.setContentsMargins(0, 4, 0, 4)
            box_vbox.setSpacing(1)
            
            lbl = QLabel(text)
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            lbl.setObjectName("lblC")
            
            metric_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
            metric_widget.setStyleSheet(f"color: {font_color}; font-size: 14px; font-weight: bold; background: transparent; border: none;")
            
            box_vbox.addWidget(lbl)
            box_vbox.addWidget(metric_widget)
            banner_layout.addWidget(box)
            
        self.left_canvas_layout.addWidget(banner)


    
    def ParkTrack_view_switcher_and_maps(self):
        switcher_strip = QHBoxLayout()
        switcher_strip.setContentsMargins(5, 5, 5, 0)
        
        lbl_switch = QLabel("Grid Layout View:")
        lbl_switch.setObjectName("mapFilter")
        switcher_strip.addWidget(lbl_switch)
        
        btn_cars_grid = QPushButton("Cars View")
        btn_cars_grid.setObjectName("viewAll")
        btn_cars_grid.clicked.connect(lambda: self.switch_grid_view(0))
        
        btn_moto_grid = QPushButton("Motorcycles View")
        btn_moto_grid.setObjectName("viewAll")
        btn_moto_grid.clicked.connect(lambda: self.switch_grid_view(1))
        
        switcher_strip.addWidget(btn_cars_grid)
        switcher_strip.addWidget(btn_moto_grid)
        switcher_strip.addStretch()
        
        self.left_canvas_layout.addLayout(switcher_strip)
        
        self.map_stack = QStackedWidget()
        
        # Page 0: Cars View
        car_page = QWidget()
        car_layout = QVBoxLayout(car_page)
        car_layout.setContentsMargins(0, 0, 0, 0)
        
        car_filter_strip = QHBoxLayout()
        car_filter_strip.addWidget(QLabel("Cars Status Filter:", objectName="mapFilter"))
        
        car_all_btn = QPushButton("View All", objectName="viewAll")
        car_all_btn.clicked.connect(lambda: self.set_car_status_filter("All"))
        car_avail_btn = QPushButton("Available", objectName="viewAvail")
        car_avail_btn.clicked.connect(lambda: self.set_car_status_filter("Available"))
        car_occ_btn = QPushButton("Occupied", objectName="viewOcc")
        car_occ_btn.clicked.connect(lambda: self.set_car_status_filter("Occupied"))
        
        car_filter_strip.addWidget(car_all_btn)
        car_filter_strip.addWidget(car_avail_btn)
        car_filter_strip.addWidget(car_occ_btn)
        car_filter_strip.addStretch()
        car_layout.addLayout(car_filter_strip)
        
        car_scroll = QScrollArea(objectName="scrollArea", widgetResizable=True)
        car_frame = QFrame(objectName="frame")
        car_grid = QGridLayout(car_frame)
        car_grid.setContentsMargins(15, 15, 15, 15)
        car_grid.setHorizontalSpacing(15)
        car_grid.setVerticalSpacing(0)
        
        self.build_grid_layout(car_grid, self.engine.get_car_slots(), self.car_slot_ui_elements, "Car")
        car_scroll.setWidget(car_frame)
        car_layout.addWidget(car_scroll)
        
        # Page 1: Motorcycles View
        moto_page = QWidget()
        moto_layout = QVBoxLayout(moto_page)
        moto_layout.setContentsMargins(0, 0, 0, 0)
        
        moto_filter_strip = QHBoxLayout()
        moto_filter_strip.addWidget(QLabel("Motorcycle Status Filter:", objectName="mapFilter"))
        
        moto_all_btn = QPushButton("View All", objectName="viewAll")
        moto_all_btn.clicked.connect(lambda: self.set_moto_status_filter("All"))
        moto_avail_btn = QPushButton("Available", objectName="viewAvail")
        moto_avail_btn.clicked.connect(lambda: self.set_moto_status_filter("Available"))
        moto_occ_btn = QPushButton("Occupied", objectName="viewOcc")
        moto_occ_btn.clicked.connect(lambda: self.set_moto_status_filter("Occupied"))
        
        moto_filter_strip.addWidget(moto_all_btn)
        moto_filter_strip.addWidget(moto_avail_btn)
        moto_filter_strip.addWidget(moto_occ_btn)
        moto_filter_strip.addStretch()
        moto_layout.addLayout(moto_filter_strip)
        
        moto_scroll = QScrollArea(objectName="scrollArea", widgetResizable=True)
        moto_frame = QFrame(objectName="frame")
        moto_grid = QGridLayout(moto_frame)
        moto_grid.setContentsMargins(15, 15, 15, 15)
        moto_grid.setHorizontalSpacing(15)
        moto_grid.setVerticalSpacing(0)
        
        self.build_grid_layout(moto_grid, self.engine.get_moto_slots(), self.moto_slot_ui_elements, "Motorcycle")
        moto_scroll.setWidget(moto_frame)
        moto_layout.addWidget(moto_scroll)
        
        self.map_stack.addWidget(car_page)
        self.map_stack.addWidget(moto_page)
        self.left_canvas_layout.addWidget(self.map_stack)
    #-------------------NEW------------------------------



    def ParkTrack_checkin_tab_panel(self):
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(10, 15, 10, 15)
        layout.setSpacing(12)
        
        lbl_section = QLabel("Space Allocation Entry")
        lbl_section.setObjectName("Allocation")
        layout.addWidget(lbl_section)
        
        lbl_plate = QLabel("Customer Name / Plate Ref:")
        lbl_plate.setProperty("class", "mutedLabel")
        layout.addWidget(lbl_plate)
        
        self.plateNum = QLineEdit()
        self.plateNum.setObjectName("panelInput")
        layout.addWidget(self.plateNum)
        
        lbl_spot = QLabel("Target Parking Grid Code:")
        lbl_spot.setProperty("class", "mutedLabel")
        layout.addWidget(lbl_spot)
        
        self.spot_selector = QComboBox()
        self.spot_selector.setObjectName("panelCombo")
        layout.addWidget(self.spot_selector)
        
        assign_btn = QPushButton("Execute Gate Check-in")
        assign_btn.setObjectName("assign")
        assign_btn.clicked.connect(self.assign_spot)
        layout.addWidget(assign_btn)
        
        layout.addStretch()
        self.control_tabs.addTab(panel, "Check-In")
      
    def ParkTrack_billing_tab_panel(self):
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(10, 15, 10, 15)
        layout.setSpacing(10)
        
        lbl_section = QLabel("Process Log-Out Operations")
        lbl_section.setObjectName("section")
        layout.addWidget(lbl_section)
        
        lbl_active = QLabel("Select Active Occupied Spot:")
        lbl_active.setProperty("class", "mutedLabel")
        layout.addWidget(lbl_active)
        
        self.active_spot_selector = QComboBox()

        self.active_spot_selector.setObjectName("panelCombo")
        layout.addWidget(self.active_spot_selector)
        
        rate_box = QFrame()
        rate_box.setObjectName("rate")
        rate_layout = QGridLayout(rate_box)
        self.base_rate_spin = QSpinBox()
        self.base_rate_spin.setRange(0, 1000)
        self.base_rate_spin.setValue(50)
        self.base_rate_spin.setObjectName("panelSpin")
        self.hourly_rate_spin = QSpinBox()
        self.hourly_rate_spin.setRange(0, 1000)
        self.hourly_rate_spin.setValue(20)
        self.hourly_rate_spin.setObjectName("panelSpin")
        lbl_base_rate = QLabel("Base Rate (₱):")
        rate_layout.addWidget(lbl_base_rate, 0, 0)
        rate_layout.addWidget(self.base_rate_spin, 0, 1)
        lbl_hourly_fee = QLabel("Hourly Fee (₱):")
        rate_layout.addWidget(lbl_hourly_fee, 1, 0)
        rate_layout.addWidget(self.hourly_rate_spin, 1, 1)
        layout.addWidget(rate_box)
        checkout_btn = QPushButton("Calculate & Clear Invoicing")
        checkout_btn.setObjectName("checkoutBtn")
        checkout_btn.clicked.connect(self.process_timeout)
        layout.addWidget(checkout_btn)
        layout.addStretch()
        self.control_tabs.addTab(panel, "Billing Box")
    def ParkTrack_history_tab_panel(self):
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(5, 10, 5, 10)
        self.ticket_log = QTableWidget(0, 5)
        self.ticket_log.setObjectName("ticketLog")
        self.ticket_log.setHorizontalHeaderLabels(["Target", "Customer", "Time-In", "Time-Out" ,"Paid Fees"])
        self.ticket_log.horizontalHeader().setStretchLastSection(True)
        lbl_history = QLabel("Session History Record Matrix:")
        layout.addWidget(lbl_history)
        layout.addWidget(self.ticket_log)
        self.control_tabs.addTab(panel, "Ledger Log")
    def log_message(self, message):
        timestamp = datetime.now().strftime("%I:%M:%S %p")
        self.activity_log_box.append(f"[{timestamp}] {message}")
    def set_grid_filter(self, filter_mode):
        self.current_filter = filter_mode
        self.log_message(f"Filtering map layout view constraints to: {filter_mode}")
        self.update_ui()
    def handle_grid_button_click(self, spot_label):
        if not self.engine.is_occupied(spot_label):
            self.control_tabs.setCurrentIndex(0)
            index = self.spot_selector.findText(spot_label)
            if index >= 0:
                self.spot_selector.setCurrentIndex(index)
            self.plateNum.setFocus()
            self.log_message(f"Focused empty {spot_label} allocation workspace node.")
        else:
            self.control_tabs.setCurrentIndex(1)
            index = self.active_spot_selector.findText(spot_label)
            if index >= 0:
                self.active_spot_selector.setCurrentIndex(index)
            self.log_message(f"Focused occupied data node profile on {spot_label}.")
    def update_ui(self):
            self.spot_selector.clear()
            self.active_spot_selector.clear()
            vacant_count = 0
            occupied_count = 0
            for spot_label, data in self.engine.get_all_slots():
                ui = self.slot_ui_elements.get(spot_label)
                if not ui:
                    continue
                if data is None:
                    vacant_count += 1
                    self.spot_selector.addItem(spot_label)
                    ui["car"].set_occupied(False)
                    ui["frame"].setVisible(self.current_filter != "Occupied")
                else:
                    occupied_count += 1
                    self.active_spot_selector.addItem(spot_label)
                    ui["car"].set_occupied(True)
                    ui["frame"].setVisible(self.current_filter != "Available")
            self.vacant_stat.setText(str(vacant_count))
            self.occupied_stat.setText(str(occupied_count))
    def assign_spot(self):
        customer = self.plateNum.text().strip()
        selected_spot = self.spot_selector.currentText()
        if not customer:
            Dialogs.show_warning(self, "Input Error", "Please provide a valid plate descriptor string sequence.")
            return
        if not selected_spot:
            Dialogs.show_warning(self, "Capacity Error", "No allocation coordinates are available.")
            return
        
        self.engine.allocate_spot(selected_spot, {
            "customer": customer,
            "time_in": datetime.now()
        })
        self.log_message(f"Allocated {selected_spot} successfully to client: {customer}")
        self.plateNum.clear()
        self.update_ui()
        
    def process_timeout(self):
        selected_spot = self.active_spot_selector.currentText()
        if not selected_spot:
            Dialogs.show_warning(self, "Selection Error", "No active track selected for processing.")
            return
        spot_data = self.engine.get_slot_data(selected_spot)
        checkout_time = datetime.now()
        
        hours_parked, total_bill = BillingEngine.calculate_bill(
            spot_data["time_in"],
            checkout_time,
            self.base_rate_spin.value(),
            self.hourly_rate_spin.value()
        )
        
        row_count = self.ticket_log.rowCount()
        self.ticket_log.insertRow(row_count)
        self.ticket_log.setItem(row_count, 0, QTableWidgetItem(selected_spot))
        self.ticket_log.setItem(row_count, 1, QTableWidgetItem(spot_data["customer"]))
        self.ticket_log.setItem(row_count, 2, QTableWidgetItem(spot_data["time_in"].strftime("%I:%M:%S %p")))
        self.ticket_log.setItem(row_count, 3, QTableWidgetItem(checkout_time.strftime("%I:%M:%S %p")))
        self.ticket_log.setItem(row_count, 4, QTableWidgetItem(f"₱{total_bill:.2f}"))
        
        Receipt.export_ticket_receipt(selected_spot, spot_data, checkout_time, hours_parked, total_bill)
        
        self.log_message(f"Released space {selected_spot}. Transaction payment settled: ₱{total_bill:.2f}")
        self.engine.release_spot(selected_spot)
        self.update_ui()
        
        
