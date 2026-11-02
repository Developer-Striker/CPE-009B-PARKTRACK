from PyQt6.QtGui import QColor

class Styles:
    # Color Constants used for QPainter/Canvas or dynamic logic
    BACKGROUND_COLOR = "#22272E"
    SIDEBAR_COLOR = "#2B3036"
    TERMINAL_COLOR = "#0D1117"
    BORDER_COLOR = "#373E47"
    BORDER_DARK = "#2E343D"
    ROAD_COLOR = "#1C2128"
    ROAD_DASH_COLOR = "#545D68"
    
    TEXT_MUTED = "color: #768390; border: none;"
    TEXT_LIGHT_GRAY = "color: #ADBAC7; border: none;"
    
    ACCENT_GREEN = QColor("#57AB5A")
    ACCENT_RED = QColor("#E5534B")
    ACCENT_GOLD = QColor("#C69026")
    ACCENT_BLUE = QColor("#316DCA")
    ACCENT_GRAY = QColor("#768390")
    
    @staticmethod
    def apply_widget_styles(app_window):
        
        #FOR TAB'S QLABEL WIDGETS
        for lbl in app_window.subtext_labels:
            lbl.setStyleSheet("color: #6CB6FF; border: 1px solid #2B3036; border-radius: 6px;")
            
        for lbl in app_window.rate_subtext_labels:
            lbl.setStyleSheet("color: #ADBAC7; border: 1px solid #2B3036;")
