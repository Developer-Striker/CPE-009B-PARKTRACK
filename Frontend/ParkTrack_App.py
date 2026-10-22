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
from ParTrack_Engine import ParkingEngine

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
        
        self.left_canvas_container = QWidget()
        self.left_canvas_layout = QVBoxLayout(self.left_canvas_container)
        self.left_canvas_layout.setContentsMargins(0, 0, 0, 0)
        
        # self.ParkTrack_parking_map_grid()
        self.apply_qss()
        self.ParkTrack_banner()
        
        self.main_layout.addWidget(self.left_canvas_container, stretch=3)
        
        self.right_sidebar_container = QFrame()
        self.right_sidebar_container.setFixedWidth(300)
        self.right_sidebar_layout = QVBoxLayout(self.right_sidebar_container)
        self.right_sidebar_layout.setContentsMargins(10, 10, 10, 10)
        self.right_sidebar_layout.setSpacing(10)
        
        self.main_layout.addWidget(self.right_sidebar_container, stretch=1)
        
    def apply_qss(self):
        self.setStyleSheet(APPLICATION_STYLESHEET)
        
    def ParkTrack_banner(self):
        banner = QFrame()
        banner.setObjectName("Banner")
        # banner.setStyleSheet(f"background-color: {Styles.SIDEBAR_COLOR}; border-radius: 6px;")
        banner.setFixedHeight(70)
        banner_layout = QHBoxLayout(banner)
        banner_layout.setContentsMargins(15, 0, 15, 0)
        
        p_logo = QLabel("P")
        p_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        p_logo.setFixedSize(40, 40)
        p_logo.setObjectName("Logo")
        # p_logo.setStyleSheet(f"background:color: {Styles.TERMINAL_COLOR}; color: {Styles.ACCENT_GOLD}; font-size")
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
            lbl.setStyleSheet(Styles.TEXT_MUTED)
            
            metric_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
            metric_widget.setStyleSheet(f"color: {font_color}; font-size: 14px; font-weight: bold; background: transparent; border: none;")
            
            box_vbox.addWidget(lbl)
            box_vbox.addWidget(metric_widget)
            banner_layout.addWidget(box)
        self.left_canvas_layout.addWidget(banner)