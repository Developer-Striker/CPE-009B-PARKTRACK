import sys
import os

from PyQt6.QtCore import (
    Qt, QPropertyAnimation, QEasingCurve, QPoint, QTimer
)
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QCheckBox, QVBoxLayout, QHBoxLayout, QMessageBox,
    QFrame, QGraphicsDropShadowEffect
)
from PyQt6.QtGui import QColor


def load_qss():
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "style.qss"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


class EmployeeLoginWindow(QWidget):
    def __init__(self, on_login_success=None):
        super().__init__()

        self.on_login_success = on_login_success
        self.init_ui()
        self.init_animations()

    def init_ui(self):
        self.setWindowTitle("PARKTRACK - Employee Login")
        self.setFixedSize(400, 480)

        # Main Layout
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(35, 25, 35, 25)
        main_layout.setSpacing(10)

        # Login Card
        card = QFrame()
        card.setObjectName("CardFrame")

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 30))
        card.setGraphicsEffect(shadow)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(25, 20, 25, 20)
        card_layout.setSpacing(10)

        # Logo
        badge_layout = QHBoxLayout()

        logo_badge = QLabel("P")
        logo_badge.setObjectName("LogoBadge")
        logo_badge.setFixedSize(44, 44)
        logo_badge.setAlignment(Qt.AlignmentFlag.AlignCenter)

        badge_layout.addStretch()
        badge_layout.addWidget(logo_badge)
        badge_layout.addStretch()

        card_layout.addLayout(badge_layout)

        # Header
        self.title = QLabel("PARKTRACK")
        self.title.setObjectName("title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.subtitle = QLabel("Staff Portal")
        self.subtitle.setObjectName("Subtitle")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card_layout.addWidget(self.title)
        card_layout.addWidget(self.subtitle)
        card_layout.addSpacing(5)

        # Username
        user_label = QLabel("USERNAME")
        user_label.setProperty("class", "FieldLabel")

        self.username = QLineEdit()
        self.username.setPlaceholderText("e.g. Attendant")

        card_layout.addWidget(user_label)
        card_layout.addWidget(self.username)

        # Password
        pass_label = QLabel("PASSWORD")
        pass_label.setProperty("class", "FieldLabel")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Enter your password")
        self.password.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        card_layout.addWidget(pass_label)
        card_layout.addWidget(self.password)

        # Show Password
        self.show_password = QCheckBox("Show Password")
        self.show_password.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        card_layout.addWidget(self.show_password)

        # Buttons
        buttons_layout = QHBoxLayout()

        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setObjectName("clearBtn")
        self.clear_btn.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.login_btn = QPushButton("Sign In")
        self.login_btn.setObjectName("loginBtn")
        self.login_btn.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        buttons_layout.addWidget(self.clear_btn)
        buttons_layout.addWidget(self.login_btn)

        card_layout.addLayout(buttons_layout)

        # Status Message
        self.status = QLabel("")
        self.status.setObjectName("status")
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card_layout.addWidget(self.status)

        # Footer
        footer_note = QLabel("CPE 009B Final Project")
        footer_note.setObjectName("footerNote")
        footer_note.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card_layout.addWidget(footer_note)

        main_layout.addWidget(card)

        # Connections
        self.login_btn.clicked.connect(self.login)
        self.clear_btn.clicked.connect(self.clear)
        self.show_password.toggled.connect(
            self.toggle_password
        )

        # Load External QSS
        self.setStyleSheet(load_qss())

    # Fade-in Animation
    def init_animations(self):
        self.setWindowOpacity(0.0)

        self.fade = QPropertyAnimation(
            self, b"windowOpacity"
        )
        self.fade.setDuration(800)
        self.fade.setStartValue(0.0)
        self.fade.setEndValue(1.0)
        self.fade.setEasingCurve(
            QEasingCurve.Type.InOutQuad
        )
        self.fade.start()

    # Shake Animation
    def shake(self):
        if (
            hasattr(self, "shake_anim")
            and self.shake_anim.state()
            == QPropertyAnimation.State.Running
        ):
            return

        start = self.pos()
        offsets = [0, 10, -10, 8, -8, 4, -4, 0]

        self.shake_anim = QPropertyAnimation(
            self, b"pos"
        )
        self.shake_anim.setDuration(400)

        for i, dx in enumerate(offsets):
            step = i / (len(offsets) - 1)
            self.shake_anim.setKeyValueAt(
                step, start + QPoint(dx, 0)
            )

        self.shake_anim.start()

    # Update QSS Properties
    def set_style_property(self, widget, name, value):
        widget.setProperty(name, value)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()

    # Show or Hide Password
    def toggle_password(self, checked):
        if checked:
            self.password.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
        else:
            self.password.setEchoMode(
                QLineEdit.EchoMode.Password
            )

    # Login Loading
    def login(self):
        self.login_btn.setEnabled(False)
        self.login_btn.setText("Please wait...")

        self.set_style_property(
            self.status, "state", ""
        )
        self.status.setText("Verifying credentials...")

        QTimer.singleShot(1000, self.check_login)

    # Custom Success Popup
    def show_success_popup(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Login Successful")
        msg.setText(
            "Login Successful!\n\nWelcome to PARKTRACK!"
        )
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(
            QMessageBox.StandardButton.Ok
        )

        msg.setStyleSheet(load_qss())
        msg.exec()

    # Check Login Credentials
    def check_login(self):
        user = self.username.text().strip()
        pw = self.password.text().strip()

        self.login_btn.setEnabled(True)
        self.login_btn.setText("Sign In")

        if user == "group 4" and pw == "1234":
            self.set_style_property(
                self.username, "error", False
            )
            self.set_style_property(
                self.password, "error", False
            )
            self.set_style_property(
                self.status, "state", "success"
            )

            self.status.setText("Login successful!")

            self.show_success_popup()

            if self.on_login_success:
                self.on_login_success()

            self.close()

        else:
            self.set_style_property(
                self.username, "error", True
            )
            self.set_style_property(
                self.password, "error", True
            )
            self.set_style_property(
                self.status, "state", "error"
            )

            self.status.setText(
                "Invalid Employee ID or Password."
            )

            self.password.clear()
            self.shake()

    # Clear Fields
    def clear(self):
        self.username.clear()
        self.password.clear()
        self.show_password.setChecked(False)
        self.status.setText("")

        self.set_style_property(
            self.username, "error", False
        )
        self.set_style_property(
            self.password, "error", False
        )
        self.set_style_property(
            self.status, "state", ""
        )

        self.login_btn.setEnabled(True)
        self.login_btn.setText("Sign In")

        self.username.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = EmployeeLoginWindow()
    login_window.show()

    sys.exit(app.exec())
