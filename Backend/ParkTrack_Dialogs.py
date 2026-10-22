from PyQt6.QtWidgets import QMessageBox

class Dialogs:
    @staticmethod
    def show_warning(parent, title, message):
        QMessageBox.warning(parent, title, message)