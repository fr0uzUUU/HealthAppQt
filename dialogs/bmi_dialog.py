from PySide6.QtWidgets import QWidget, QMessageBox, QLineEdit, QPushButton, QComboBox, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class BMIDialog(QWidget):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        ui_file = QFile("dialogs/ui/bmi_dialog.ui")
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file)
        ui_file.close()

        self.weight_input = self.window.findChild(QLineEdit, "weightInput")
        self.height_input = self.window.findChild(QLineEdit, "heightInput")
        self.age_input = self.window.findChild(QLineEdit, "ageInput")
        self.gender_combo = self.window.findChild(QComboBox, "genderCombo")
        self.result_label = self.window.findChild(QLabel, "resultLabel")
        self.calculate_button = self.window.findChild(QPushButton, "calculateButton")

        self.calculate_button.clicked.connect(self.calculate_bmi)
        self.window.show()

    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height_cm = float(self.height_input.text())
            age = int(self.age_input.text())
            gender = self.gender_combo.currentText()

            if height_cm <= 0 or weight <= 0 or age <= 0:
                raise ValueError("Invalid input values")

            height_m = height_cm / 100
            bmi = weight / (height_m ** 2)

            category = self.bmi_category(bmi, age, gender)
            self.result_label.setText(f"BMI: {bmi:.2f} ({category})")

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Wprowadź poprawne dane liczbowe.")

    def bmi_category(self, bmi, age, gender):
        if bmi < 18.5:
            return "Niedowaga"
        elif 18.5 <= bmi < 25:
            return "Waga prawidłowa"
        elif 25 <= bmi < 30:
            return "Nadwaga"
        else:
            return "Otyłość"
