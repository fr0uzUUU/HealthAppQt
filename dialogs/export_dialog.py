import os
import json
from PySide6.QtWidgets import QMessageBox

def export_to_txt_gui(username, parent=None):
    json_file = f"data/{username}_meds.json"
    txt_file = f"data/{username}_meds.txt"

    if not os.path.exists(json_file):
        QMessageBox.warning(parent, "Błąd", "Brak historii do eksportu.")
        return

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not data:
        QMessageBox.information(parent, "Info", "Brak danych do eksportu.")
        return

    with open(txt_file, "w", encoding="utf-8") as f:
        for entry in data:
            f.write(f"Lek: {entry['lek']}, Dawka: {entry['dawka']}\n")

    QMessageBox.information(parent, "Eksport zakończony", f"Dane zapisano do pliku:\n{txt_file}")

