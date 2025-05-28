import json
import os
from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QTimeEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class AddMedDialog(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.file_path = f"data/{self.username}_meds.json"

        loader = QUiLoader()
        ui_file = QFile("dialogs/ui/add_med_dialog.ui")
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file)
        ui_file.close()

        self.med_name_input = self.window.findChild(QLineEdit, "medNameInput")
        self.med_dose_input = self.window.findChild(QLineEdit, "medDoseInput")
        self.med_time_input = self.window.findChild(QTimeEdit, "medTimeInput")
        self.save_button = self.window.findChild(QPushButton, "saveButton")
        self.status_label = self.window.findChild(QLabel, "statusLabel")

        self.save_button.clicked.connect(self.save_med)
        self.window.show()

    def save_med(self):
        name = self.med_name_input.text().strip()
        dose = self.med_dose_input.text().strip()
        time = self.med_time_input.time().toString("HH:mm")

        if not name or not dose or not time:
            self.status_label.setText("Uzupełnij wszystkie pola.")
            self.status_label.setStyleSheet("color: red;")
            return

        entry = {
            "lek": name,
            "dawka": dose,
            "godzina": time,
            "status": "niezażyty"
        }
        data = []

        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

        data.append(entry)

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        self.status_label.setText("Zapisano lek.")
        self.status_label.setStyleSheet("color: green;")
        self.med_name_input.clear()
        self.med_dose_input.clear()
