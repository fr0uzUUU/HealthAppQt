from time import sleep

from PySide6.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton, QProgressBar
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
        self.result_label = self.window.findChild(QLabel, "resultLabel")
        self.progress_bar = self.window.findChild(QProgressBar, "progressBar")
        self.calc_button = self.window.findChild(QPushButton, "calculateButton")

        self.calc_button.clicked.connect(self.calculate_bmi)
        self.progress_bar.setValue(0)
        self.window.show()

    def calculate_bmi(self):
        try:


            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            bmi = weight / (height ** 2)
            for x in range(100):
                self.progress_bar.setValue(x)
                x+=5
                sleep(0.01)

            self.result_label.setText(f"Twoje BMI: {bmi:.2f}")
        except ValueError:
            self.result_label.setText("Nieprawidłowe dane")
