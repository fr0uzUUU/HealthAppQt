from PySide6.QtWidgets import QLineEdit, QPushButton, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from dialogs.user_auth import load_users, save_users, hash_password, is_password_strong
from dialogs.main_window import MainWindow

class LoginWindow:
    def __init__(self):
        loader = QUiLoader()
        ui_file = QFile("dialogs/ui/login.ui")
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file)
        ui_file.close()

        self.username_input = self.window.findChild(QLineEdit, "usernameInput")
        self.password_input = self.window.findChild(QLineEdit, "passwordInput")
        self.login_button = self.window.findChild(QPushButton, "loginButton")
        self.create_button = self.window.findChild(QPushButton, "createButton")
        self.status_label = self.window.findChild(QLabel, "statusLabel")

        self.login_button.clicked.connect(self.login)
        self.create_button.clicked.connect(self.create_account)
        self.window.show()

    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        users = load_users()

        if username in users and users[username] == hash_password(password):
            self.status_label.setText("")
            self.window.close()
            self.main_window = MainWindow(username)
        else:
            self.status_label.setText("Niepoprawna nazwa lub hasło.")

    def create_account(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        users = load_users()

        if username in users:
            self.status_label.setText("Użytkownik już istnieje.")
            return

        if not is_password_strong(password):
            self.status_label.setText("Hasło za słabe.")
            return

        users[username] = hash_password(password)
        save_users(users)
        self.status_label.setText("Konto utworzone.")
