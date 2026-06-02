from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import QIcon 

class OurWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shivam's Window")
    #   self.setWindowIcon(QIcon("path or name of of profile picture")) 
        self.setGeometry(0,0,600,600) # first two are x,y coordinates and rest are length and width
        

def main():
    app = QApplication(sys.argv)
    window = OurWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()