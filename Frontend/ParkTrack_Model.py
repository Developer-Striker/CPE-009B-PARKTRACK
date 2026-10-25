from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QColor

class ParkingSlotWidget(QWidget):
    def __init__(self, is_occupied, spot_label, parent=None):
        super().__init__(parent)
        self.is_occupied = is_occupied
        self.spot_label = spot_label
        self.setMinimumSize(70, 95)
        
    def set_occupied(self, state):
        self.is_occupied = state
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        color = QColor("#e74c3c") if self.is_occupied else QColor("#2ecc71")
        
        pen = QPen(color, 2)
        painter.setPen(pen)
        painter.drawRoundedRect(10, 8, 50, 65, 6, 6)
        
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawRoundedRect(16, 20, 38, 25, 2, 2)
        
        painter.setPen(QColor("#ffffff"))
        painter.setFont(painter.font())
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter, self.spot_label)
