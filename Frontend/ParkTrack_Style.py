from PyQt6.QtGui import QColor

class Styles:
    # Color Constants used for QPainter/Canvas or dynamic logic
    BACKGROUND_COLOR = "#2d2d30"
    SIDEBAR_COLOR = "#3e3e42"
    TERMINAL_COLOR = "#1e1e1e"
    BORDER_COLOR = "#555"
    BORDER_DARK = "#444"
    ROAD_COLOR = "#282828"
    ROAD_DASH_COLOR = "#777"
    
    TEXT_MUTED = "color: #aaa; border: none;"
    TEXT_LIGHT_GRAY = "color: #ccc; border: none;"
    
    ACCENT_GREEN = QColor("#2ecc71")
    ACCENT_RED = QColor("#e74c3c")
    ACCENT_GOLD = QColor("#f1c40f")
    ACCENT_BLUE = QColor("#2980b9")
    ACCENT_GRAY = QColor("#7f8c8d")
    
    @staticmethod
    def apply_widget_styles(app_window):
        
        #FOR TAB'S QLABEL WIDGETS
        for lbl in app_window.subtext_labels:
            lbl.setStyleSheet("color: #aaa; border: 1px solid #555; border-radius: 6px;")
            
        for lbl in app_window.rate_subtext_labels:
            lbl.setStyleSheet("color: #aaa; border: 1px solid #555;")
