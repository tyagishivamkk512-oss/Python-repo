import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(700, 300, 500, 500)

        self.button = QPushButton("Mujhe Dabao", self)
        self.label = QLabel("Main shivam hun", self)

        self.initUI()

    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.move(100, 300)
        self.label.setStyleSheet("font-size: 50px;")
        self.label.adjustSize()

    def on_click(self):
        self.label.setText("🤤")
        self.label.adjustSize() 

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())