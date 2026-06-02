from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
import sys

class OurWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shivam's Window")
        self.setGeometry(100, 100, 800, 600)

        label = QLabel("Hello, I am Shivam", self) #self refers to window object, that will be our parent object

        label.setFont(QFont("Times New Roman",20))
        label.adjustSize() #it will automatically adjust size of label according to font


def main():
    app = QApplication(sys.argv)
    window = OurWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()