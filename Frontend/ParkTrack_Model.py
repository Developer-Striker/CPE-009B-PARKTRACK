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
        
        color = QColor("#e74c3c") if self.is_occupied else QColor("#2ecc71")
        
        pen = QPen(color, 2)
        brush = QBrush()
        painter.setPen(pen)

        # Body Outline
        painter.drawRoundedRect(26, 15, 42, 69, 30, 12)

        # Trunk Outline
        painter.drawRoundedRect(25, 70, 44, 20, 10, 10)

        # Hood Outline
        painter.drawRoundedRect(25, 5, 44, 30, 15, 15)

        # Side Rear Mirror (Left) Outline
        painter.drawLine(QPoint(20, 32), QPoint(25, 28))

        # Side Rear Mirror (Right) Outline
        painter.drawLine(QPoint(74, 32), QPoint(68, 28))

        # "Inner" Roof Outline
        brush.setColor(QColor("#2d2d30")) # Hide Excess Lines
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)
        painter.drawRoundedRect(32, 27, 30, 48, 30, 5)
        
        painter.setPen(QColor("#ffffff"))
        painter.setFont(painter.font())
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter, self.spot_label)
