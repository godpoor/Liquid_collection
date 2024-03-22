import sys
from PyQt6.QtWidgets import QMainWindow, QApplication

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Check ROI")
        self.resize(900, 650)
        self.show()

def main():

    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
