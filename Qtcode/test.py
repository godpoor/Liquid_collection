import sys
from PyQt6.QtWidgets import QMainWindow, QApplication

class testCLA(QMainWindow):
    def __init__(self, father):
        super().__init__()
        self.father = father
        self.initUI()

    def initUI(self):
        self.setWindowTitle("test")
        self.setGeometry(100, 100, 400, 300)
        self.show()

    def test(self):
        print("here is test")

def main():
    app = QApplication(sys.argv)
    testCLA()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
