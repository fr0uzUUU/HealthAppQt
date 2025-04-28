from PySide6.QtWidgets import QWidget, QPushButton, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MainWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        loader = QUiLoader()
        ui_file = QFile("dialogs/ui/main_window.ui")
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file)
        ui_file.close()

        self.bmi_btn = self.window.findChild(QPushButton, "bmiButton")
        self.add_med_btn = self.window.findChild(QPushButton, "addMedButton")
        self.history_btn = self.window.findChild(QPushButton, "historyButton")
        self.export_btn = self.window.findChild(QPushButton, "exportButton")
        self.motivate_btn = self.window.findChild(QPushButton, "motivateButton")
        self.logout_btn = self.window.findChild(QPushButton, "logoutButton")
        self.welcome_lbl = self.window.findChild(QLabel, "welcomeLabel")

        if self.welcome_lbl:
            self.welcome_lbl.setText(f"Witaj, {self.username}!")

        self.bmi_btn.clicked.connect(self.show_bmi_dialog)
        self.add_med_btn.clicked.connect(self.show_add_med_dialog)
        self.history_btn.clicked.connect(self.show_history_dialog)
        self.export_btn.clicked.connect(self.export_data_to_txt)
        self.motivate_btn.clicked.connect(self.show_motivation_gui)
        self.logout_btn.clicked.connect(self.logout)

        self.window.show()

    def show_bmi_dialog(self):
        from dialogs.bmi_dialog import BMIDialog
        self.bmi_window = BMIDialog()

    def show_add_med_dialog(self):
        from dialogs.add_med_dialog import AddMedDialog
        self.add_med_window = AddMedDialog(self.username)

    def show_history_dialog(self):
        from dialogs.history_dialog import HistoryDialog
        self.history_window = HistoryDialog(self.username)

    def export_data_to_txt(self):
        from dialogs.export_dialog import export_to_txt_gui
        export_to_txt_gui(self.username, self.window)

    def show_motivation_gui(self):
        from dialogs.motivation_dialog import show_motivation_gui
        show_motivation_gui(self.window)

    def logout(self):
        self.window.close()
        from dialogs.login_dialog import LoginWindow
        LoginWindow()
