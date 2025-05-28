import os
import json
from PySide6.QtWidgets import QMessageBox

def show_motivation_gui(parent=None, username=None):
    if not username:
        QMessageBox.warning(parent, "Błąd", "Nie podano użytkownika.")
        return

    file_path = f"data/{username}_meds.json"
    if not os.path.exists(file_path):
        QMessageBox.information(parent, "Brak leków", "Nie dodano jeszcze żadnych leków.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        meds = json.load(f)

    if not meds:
        QMessageBox.information(parent, "Brak leków", "Lista leków jest pusta.")
        return

    message = "Przypomnienie o lekach:\n\n"

    for med in meds:
        lek = med.get("lek", "Nieznany lek")
        dawka = med.get("dawka", "brak dawki")
        godzina = med.get("godzina", "--:--")
        status = med.get("status", "niezażyty")

        message += f"- {lek} ({dawka}) o {godzina} — [{status}]\n"

    QMessageBox.information(parent, "Przypomnienie", message)
