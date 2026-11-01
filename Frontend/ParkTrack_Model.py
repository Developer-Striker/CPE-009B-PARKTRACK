from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QPen, QColor, QBrush, QPainterPath, QTransform, QFont

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
        pen2 = QPen(color, 3)
        pen3 = QPen(color, 4) 
        color2 = QColor("#949191")
        brush = QBrush(color2)

        if self.vehicle_type == "Motorcycle":
            # Calling Motorcycle
            MotorcycleHelper.drawMotor_Body(painter, pen, brush)
            MotorcycleHelper.drawMotor_SideRearMirrors(painter, pen3)
            MotorcycleHelper.drawMotor_HandleBar(painter, pen, pen2, brush)
            MotorcycleHelper.drawMotor_Seat(painter, pen)             
        else:
            # Calling Automobile 
            CarHelper.drawCar(painter, pen)

        # WILL BE REMOVING THESE!!!
        # if self.is_occupied and self.is_overstay:
        #     painter.setPen(QColor("#f39c12"))
        #     badge_text = "OVERSTAY"
        #     font_size = 6
            
        # else:
        #     painter.setPen(QColor("#2ecc71") if not self.is_occupied else QColor("#e74c3c"))
        #     badge_text = "MOTO" if self.vehicle_type == "Motorcycle" else "CAR"  # Will be removing this
        #     font_size = 7
            
        # font = painter.font()
        # font.setPointSize(font_size)
        # font.setBold(True)
        # painter.setFont(font)
        # painter.drawText(10, 20, 50, 25, Qt.AlignmentFlag.AlignCenter, badge_text)

        # painter.setPen(QColor("#ffffff"))
        # font = painter.font()
        # font.setPointSize(8)
        # font.setBold(False)
        # painter.setFont(font)
        # painter.drawText(self.rect(), Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter, self.spot_label)

class MotorcycleHelper:
    @staticmethod
    def drawMotor_Body(painter, pen, brush):
        back_body = QPainterPath()
        back_body.addRoundedRect(35, 10, 25, 50, 35, 10)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(back_body)
        
        body1 = QPainterPath()
        body1.addEllipse(33, 37, 29, 58)
        body2 = QPainterPath()
        body2.addRoundedRect(41, 17, 13, 35, 10, 5)
        body3 = QPainterPath()
        body3.addEllipse(41, 2, 13, 25)
        body4 = QPainterPath()
        body4.moveTo(90, 60)
        body4.arcTo(30, 30, 60, 60, 180, 180)
        transf = QTransform()
        transf.scale(0.16, 0.3)
        transf.translate(235, 230)
        body_4 = transf.map(body4)

        main_body = (body1 + body2 + body3)
        painter.setPen(pen)
        painter.drawPath(main_body)
        painter.drawPath(body_4)

    def drawMotor_SideRearMirrors(painter, pen3):
        # Side Bars
        painter.drawLine(QPoint(15, 23), QPoint(26, 21))
        painter.drawLine(QPoint(79, 23), QPoint(68, 21))
        # Side Mirrors
        painter.setPen(pen3)
        painter.drawLine(QPoint(10, 25), QPoint(15, 24))
        painter.drawLine(QPoint(78, 24), QPoint(82, 25))

    def drawMotor_HandleBar(painter, pen, pen2, brush):
        # Handle Bar Right
        handleBarBody1 = QPainterPath()    
        handleBarBody1.addEllipse(40, 14, 16, 14)
        transform = QTransform()
        transform.shear(0.5, 0.0)
        handleBar_body1 = transform.map(handleBarBody1)
        painter.setPen(pen2)
        painter.drawLine(QPoint(20, 30), QPoint(26, 27))

        # Handle Bar Left
        painter.setPen(pen2)
        handleBarBody2 = QPainterPath()
        handleBarBody2.addEllipse(38, 14, 16, 14)
        transform2 = QTransform()
        transform2.shear(-0.5, 0.0)
        handleBar_body2 = transform2.map(handleBarBody2)
        painter.setPen(pen2)
        painter.drawLine(QPoint(75, 30), QPoint(68, 27))

        handleBar_body3 = QPainterPath()
        handleBar_body3.addRoundedRect(38, 10, 18, 18, 5, 5)

        handle_Bar = (handleBar_body1 + handleBar_body2 + handleBar_body3)
        handle_Bar.setFillRule(Qt.FillRule.WindingFill)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(handle_Bar)

    def drawMotor_Seat(painter, pen):
        seat1 = QPainterPath()
        seat1.addRoundedRect(39, 54, 17, 29, 17, 10)     
        seat2 = QPainterPath()
        seat2.addEllipse(39, 44, 17, 37)

        seat12 = seat1.united(seat2)        
        seat12.setFillRule(Qt.FillRule.WindingFill)
        painter.setPen(pen)
        painter.drawPath(seat12)

class CarHelper:
    @staticmethod
    def drawCar(painter, pen):

        painter.setPen(pen)
        whole_car = QPainterPath()
        car1 = QPainterPath()
        car2 = QPainterPath()
        car3 = QPainterPath()
        car4 = QPainterPath()

        # Body Outline
        car1.addRoundedRect(26, 15, 42, 69, 30, 12)
        # Trunk Outline
        car2.addRoundedRect(25, 70, 44, 20, 10, 10)
        # Hood Outline
        car3.addRoundedRect(25, 5, 44, 30, 15, 15)
        # Side Rear Mirror (Left) Outline
        painter.drawLine(QPoint(20, 32), QPoint(25, 28))
        # Side Rear Mirror (Right) Outline
        painter.drawLine(QPoint(74, 32), QPoint(68, 28))
        # "Inner" Roof Outline
        car4 = QPainterPath()
        car4.addRoundedRect(32, 27, 30, 48, 30, 5)

        car_2 = car2.subtracted(car4)
        car_3 = car3.subtracted(car4)
        whole_car.addPath(car1)
        whole_car.addPath(car_2)
        whole_car.addPath(car_3)
        whole_car.addPath(car4)
        whole_car.setFillRule(Qt.FillRule.WindingFill)
        painter.setPen(pen)
        painter.drawPath(whole_car)