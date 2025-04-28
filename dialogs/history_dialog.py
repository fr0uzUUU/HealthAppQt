import os
import json
from PySide6.QtWidgets import QWidget, QListWidget, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class HistoryDialog(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.file_path = f"data/{self.username}_meds.json"

        loader = QUiLoader()
        ui_file = QFile("dialogs/ui/history_dialog.ui")
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file)
        ui_file.close()

        self.history_list = self.window.findChild(QListWidget, "historyList")
        self.info_label = self.window.findChild(QLabel, "infoLabel")

        self.load_history()
        self.window.show()

    def load_history(self):
        if not os.path.exists(self.file_path):
            self.info_label.setText("Brak zapisanych leków.")
            return

        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not data:
            self.info_label.setText("Brak historii.")
            return

        for entry in data:
            lek = entry.get("lek", "Nieznany")
            dawka = entry.get("dawka", "")
            self.history_list.addItem(f"{lek} — {dawka}")
