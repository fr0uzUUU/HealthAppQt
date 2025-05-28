from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QTimer, QTime
import json
import os

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
        self.mark_taken_btn = self.window.findChild(QPushButton, "markAsTakenButton")
        self.welcome_lbl = self.window.findChild(QLabel, "welcomeLabel")

        if self.welcome_lbl:
            self.welcome_lbl.setText(f"Witaj, {self.username}!")

        self.bmi_btn.clicked.connect(self.show_bmi_dialog)
        self.add_med_btn.clicked.connect(self.show_add_med_dialog)
        self.history_btn.clicked.connect(self.show_history_dialog)
        self.export_btn.clicked.connect(self.export_data_to_txt)
        self.motivate_btn.clicked.connect(self.show_motivation_gui)
        self.mark_taken_btn.clicked.connect(self.mark_meds_as_taken)
        self.logout_btn.clicked.connect(self.logout)

        self.window.show()
        self.start_medication_reminder_timer()

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
        show_motivation_gui(self.window, self.username)

    def start_medication_reminder_timer(self):
        self.reminder_timer = QTimer()
        self.reminder_timer.timeout.connect(self.check_medication_time)
        self.reminder_timer.start(60 * 1000)  # sprawdzanie co 60 sek.

    def check_medication_time(self):
        now = QTime.currentTime().toString("HH:mm")
        file_path = f"data/{self.username}_meds.json"
        if not os.path.exists(file_path):
            return

        with open(file_path, "r", encoding="utf-8") as f:
            meds = json.load(f)

        updated = False
        for med in meds:
            if med.get("godzina") == now and med.get("status") != "zażyty":
                response = QMessageBox.question(
                    self.window,
                    "Przypomnienie",
                    f"Czas na lek: {med['lek']} ({med['dawka']})\nCzy już go zażyłeś?",
                    QMessageBox.Yes | QMessageBox.No
                )
                if response == QMessageBox.Yes:
                    med["status"] = "zażyty"
                    updated = True

        if updated:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(meds, f, ensure_ascii=False, indent=4)

    def mark_meds_as_taken(self):
        file_path = f"data/{self.username}_meds.json"
        if not os.path.exists(file_path):
            QMessageBox.information(self.window, "Brak danych", "Nie znaleziono listy leków.")
            return

        with open(file_path, "r", encoding="utf-8") as f:
            meds = json.load(f)

        updated = False
        for med in meds:
            if med.get("status") != "zażyty":
                med["status"] = "zażyty"
                updated = True

        if updated:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(meds, f, ensure_ascii=False, indent=4)
            QMessageBox.information(self.window, "Oznaczono", "Wszystkie leki oznaczono jako zażyte.")
        else:
            QMessageBox.information(self.window, "Informacja", "Wszystkie leki już były oznaczone.")

    def logout(self):
        self.window.close()
        from dialogs.login_dialog import LoginWindow
        LoginWindow()
