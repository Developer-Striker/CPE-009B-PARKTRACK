from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QColor, QFont

class ParkingSlotWidget(QWidget):
    def __init__(self, is_occupied, spot_label, vehicle_type="Car", is_overstay=False, parent=None):
        super().__init__(parent)
        self.is_occupied = is_occupied
        self.spot_label = spot_label
        self.vehicle_type = vehicle_type
        self.is_overstay = is_overstay
        self.setMinimumSize(70, 95)
        
    def set_occupied(self, state, vehicle_type="Car", is_overstay=False): 
        self.is_occupied = state
        self.vehicle_type = vehicle_type
        self.is_overstay = is_overstay
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        if not self.is_occupied:
            color = QColor("#2ecc71")
        elif self.is_overstay:
            color = QColor("#e67e22")
        else:
            color = QColor("#e74c3c")
        
        pen = QPen(color, 2)
        painter.setPen(pen)
        painter.drawRoundedRect(10, 8, 50, 65, 6, 6)
        
        pen.setWidth(1)
        painter.setPen(pen)
        if self.vehicle_type == "Motorcycle":
            painter.drawRoundedRect(22, 20, 26, 25, 2, 2)
        else:
            painter.drawRoundedRect(16, 20, 38, 25, 2, 2)

        if self.is_occupied and self.is_overstay:
            painter.setPen(QColor("#f39c12"))
            badge_text = "OVERSTAY"
            font_size = 6
            
        else:
            painter.setPen(QColor("#2ecc71") if not self.is_occupied else QColor("#f1c40f"))
            badge_text = "MOTO" if self.vehicle_type == "Motorcycle" else "CAR"
            font_size = 7
            
        font = painter.font()
        font.setPointSize(font_size)
        font.setBold(True)
        painter.setFont(font)
        painter.drawText(10, 20, 50, 25, Qt.AlignmentFlag.AlignCenter, badge_text)

        painter.setPen(QColor("#ffffff"))
        font = painter.font()
        font.setPointSize(8)
        font.setBold(False)
        painter.setFont(font)
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter, self.spot_label)
