import random
from PySide6.QtWidgets import QMessageBox

def show_motivation_gui(parent=None):
    messages = [
        "Dobrze Ci idzie! Nie przestawaj! 💪",
        "Małe kroki prowadzą do wielkich zmian.",
        "Zdrowie to najlepszy prezent – dbaj o nie!",
        "Jesteś silniejszy niż myślisz 💚",
        "Każdy dzień to nowa szansa.",
        "Dbając o zdrowie, inwestujesz w siebie!"
    ]

    message = random.choice(messages)
    QMessageBox.information(parent, "Motywacja", message)
