from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
import sys

class OurWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shivam's Window")
        self.setGeometry(100, 100, 800, 600)

        label = QLabel("Hello, I am Shivam", self) 
        label.adjustSize() 
        pixmap = QPixmap("Profile.pic.jpg") #name or path of image
        label.setPixmap(pixmap)


def main():
    app = QApplication(sys.argv)
    window = OurWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()