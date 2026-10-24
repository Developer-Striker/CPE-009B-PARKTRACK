import sys
from datetime import datetime
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, 
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, 
    QComboBox, QSpinBox, QGridLayout, QFrame, QTextEdit, QScrollArea
)
from PyQt6.QtCore import Qt
from ParkTrack_Model import ParkingSlotWidget
from ParkTrack_Style import APPLICATION_STYLESHEET, Styles
from ParkTrack_Engine import ParkingEngine

class ParkingSystemApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ParkTrack Parking Management System")
        self.resize(1150, 720)
        self.setStyleSheet(f"background-color: {Styles.BACKGROUND_COLOR}")
        
        self.engine = ParkingEngine(24)
        self.current_filter = "All"
        self.slot_ui_elements = {}
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(15, 15, 15, 15)
        self.main_layout.setSpacing(15)

        
        #LEFT SIDE LAYOUT
        self.left_canvas_container = QWidget()
        self.left_canvas_layout = QVBoxLayout(self.left_canvas_container)
        self.left_canvas_layout.setContentsMargins(0, 0, 0, 0)
        
        self.apply_qss()
        self.ParkTrack_banner()
        self.ParkTrack_parking_map_grid()
        
        self.main_layout.addWidget(self.left_canvas_container, stretch=3)

        
        # RIGHT SIDE LAYOUT
        self.right_sidebar_container = QFrame()
        self.right_sidebar_container.setFixedWidth(300)
        self.right_sidebar_layout = QVBoxLayout(self.right_sidebar_container)
        self.right_sidebar_layout.setContentsMargins(10, 10, 10, 10)
        self.right_sidebar_layout.setSpacing(10)

        # TABS
        self.control_tabs = QTabWidget()
        self.control_tabs.setStyleSheet(Styles.TAB_STYLESHEET)
        
        self.ParkTrack_checkin_tab_panel()
        self.ParkTrack_billing_tab_panel()
        self.ParkTrack_history_tab_panel()
        self.right_sidebar_layout.addWidget(self.control_tabs, stretch=1)

        # ACTIVITY LOG
        log_title = QLabel("System Activity Log")
        log_title.setObjectName("logTitle")
        self.right_sidebar_layout.addWidget(log_title)
        
        self.activity_log_box = QTextEdit()
        self.activity_log_box.setReadOnly(True)
        self.activity_log_box.setFixedHeight(150)
        self.activity_log_box.setStyleSheet(Styles.LOG_STYLESHEET)
        self.right_sidebar_layout.addWidget(self.activity_log_box)
        
        self.main_layout.addWidget(self.right_sidebar_container, stretch=1)
        
        self.update_ui()
        self.log_message("System loaded successfully.")
        
        
    def apply_qss(self):
        self.setStyleSheet(APPLICATION_STYLESHEET)

        # BANNER AREA LAYOUT
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
        
        self.total_stat = QLabel(str(len(self.engine.parking_slots)))
        self.vacant_stat = QLabel("0")
        self.occupied_stat = QLabel("0")
        
        stats_configurations = [
            ("Total Spaces", self.total_stat, "white"),
            ("Available", self.vacant_stat, Styles.ACCENT_GREEN),
            ("Occupied", self.occupied_stat, Styles.ACCENT_RED)
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
            #to fix
            metric_widget.setStyleSheet(f"color: {font_color}; font-size: 14px; font-weight: bold; background: transparent; border: none;")
            
            box_vbox.addWidget(lbl)
            box_vbox.addWidget(metric_widget)
            banner_layout.addWidget(box)
            
        self.left_canvas_layout.addWidget(banner)

        #PARKING GRID AREA LAYOUT
    def ParkTrack_parking_map_grid(self):
        filter_strip = QHBoxLayout()
        filter_strip.setContentsMargins(5, 5, 5, 0)
        
        map_filter = QLabel("Map Filter View Mode:")
        map_filter.setObjectName("mapFilter")
        filter_strip.addWidget(map_filter)
        
        viewAll_btn = QPushButton("View All")
        viewAll_btn.setObjectName("viewAll")
        viewAll_btn.clicked.connect(lambda: self.set_grid_filter("All"))
        
        viewAvail_btn = QPushButton("Available")
        viewAvail_btn.setObjectName("viewAvail")
        viewAll_btn.clicked.connect(lambda: self.set_grid_filter("Available"))
        
        viewOcc_btn = QPushButton("Occupied")
        viewOcc_btn.setObjectName("viewOcc")
        viewAll_btn.clicked.connect(lambda: self.set_grid_filter("Occupied"))
        
        filter_strip.addWidget(viewAll_btn)
        filter_strip.addWidget(viewAvail_btn)
        filter_strip.addWidget(viewOcc_btn)
        filter_strip.addStretch()
        self.left_canvas_layout.addLayout(filter_strip)
        
        
        # SCROLL FUNCTION
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setObjectName("scrollArea")

        # PARKING GRID FRAME
        grid_frame = QFrame()
        grid_frame.setObjectName("frame")
        grid_layout = QGridLayout(grid_frame)
        grid_layout.setContentsMargins(15, 15, 15, 15)
        grid_layout.setHorizontalSpacing(15)
        grid_layout.setVerticalSpacing(0) 
        
        
        scroll_area.setWidget(grid_frame)
        self.left_canvas_layout.addWidget(scroll_area)
        
        
        
    def ParkTrack_checkin_tab_panel(self):
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(10, 15, 10, 15)
        layout.setSpacing(12)
        
        lbl_section = QLabel("Space Allocation Entry")
        lbl_section.setObjectName("Allocation")
        layout.addWidget(lbl_section)
        
        
        
        layout.addStretch()
        self.control_tabs.addTab(panel, "Check In")
        
    def ParkTrack_billing_tab_panel(self):
        pass
    
    def ParkTrack_history_tab_panel(self):
        pass
    
    
    def log_message(self, message):
        timestamp = datetime.now().strftime("%I:%M:%S %p")
        self.activity_log_box.append(f"[{timestamp}] {message}")
        
    def update_ui(self):
        pass
    
    def set_grid_filter(self):
        pass
