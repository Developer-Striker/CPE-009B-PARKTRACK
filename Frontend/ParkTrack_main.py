import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from pathlib import Path

from ParkTrack_Login import EmployeeLoginWindow
from ParkTrack_App import ParkingSystemApp

main_window = None
style_now = "ParkTrack_Style.qss"
icon = "ParkTrack_Icon.ico"

def apply_stylesheet(app, style_name):
    global style_now
    style_now = style_name
    base_dir = os.path.dirname(os.path.abspath(__file__))
    qss_path = os.path.join(base_dir, style_name)
    
    if os.path.exists(qss_path):
        with open(qss_path, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())

def open_main_app(app):
    global main_window
    apply_stylesheet(app, style_now)        
    main_window = ParkingSystemApp()
    if style_now == "ParkTrack_Style.qss" and hasattr(main_window, 'toggle_btn'):
        main_window.toggle_btn.setText("🌙")  
    main_window.show()

def main(): 
    app = QApplication(sys.argv)
    # Added: set 'ParkTrack_Icon.ico' as icon
    app.setWindowIcon(QIcon(str(Path(__file__).with_name(icon))))    
    login_window = EmployeeLoginWindow(on_login_success=lambda: open_main_app(app))
    login_window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()
