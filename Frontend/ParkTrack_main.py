import sys
from PyQt6.QtWidgets import QApplication
from pathlib import Path

from ParkTrack_Login import EmployeeLoginWindow
from ParkTrack_App import ParkingSystemApp
main_window = None

def open_main_app(app):
    global main_window
    qss_file = Path(__file__).with_name("ParkTrack_Style.qss")
    if qss_file.exists():
        app.setStyleSheet(qss_file.read_text(encoding="utf-8"))        
    main_window = ParkingSystemApp()
    main_window.show()

def main(): 
    app = QApplication(sys.argv)    
    login_window = EmployeeLoginWindow(on_login_success=lambda: open_main_app(app))
    login_window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()
