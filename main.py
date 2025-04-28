from PySide6.QtWidgets import QApplication
from dialogs.login_dialog import LoginWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
