import sys
from PyQt6.QtWidgets import QApplication
from ParkTrack_App import ParkingSystemApp
from pathlib import Path

def main():
    app = QApplication(sys.argv)
    
    #-------------------NEW------------------------------    
    # Read and apply QSS file globally across QApplication
    qss_file = Path(__file__).with_name("ParkTrack_Style.qss")
    if qss_file.exists():
        app.setStyleSheet(qss_file.read_text(encoding="utf-8"))
    #-------------------NEW------------------------------    
        
    window = ParkingSystemApp()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()
