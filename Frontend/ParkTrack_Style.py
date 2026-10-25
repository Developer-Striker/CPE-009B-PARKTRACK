from PyQt6.QtGui import QColor

class Styles:
    # Color Constants used for QPainter/Canvas or dynamic logic
    BACKGROUND_COLOR = "#2d2d30"
    SIDEBAR_COLOR = "#3e3e42"
    TERMINAL_COLOR = "#0D1117"
    BORDER_COLOR = "#555"
    BORDER_DARK = "#444"
    ROAD_COLOR = "#282828"
    ROAD_DASH_COLOR = "#777"
    
    TEXT_MUTED = "color: #aaa; border: none;"
    TEXT_LIGHT_GRAY = "color: #ccc; border: none;"
    
    ACCENT_GREEN = QColor("#8EDFB0")
    ACCENT_RED = QColor("#e3a59e")
    ACCENT_GOLD = QColor("#fad96d")
    ACCENT_BLUE = QColor("#74b9e4")
    ACCENT_GRAY = QColor("#bdc3c7")
    
    @staticmethod
    def apply_widget_styles(app_window):
        
        #FOR TAB'S QLABEL WIDGETS
        for lbl in app_window.subtext_labels:
            lbl.setStyleSheet("color: #aaa; border: 1px solid #555; border-radius: 6px;")
            
        for lbl in app_window.rate_subtext_labels:
            lbl.setStyleSheet("color: #aaa; border: 1px solid #555;")
