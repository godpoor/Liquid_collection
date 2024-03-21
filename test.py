import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Button Window")
        self.setGeometry(100, 100, 400, 300)

        self.initUI()

    def initUI(self):
        button = QPushButton(self)
        button.setGeometry(150, 150, 100, 50)
        icon = QIcon("pic/play.png")  # 替换为你自己的图标文件路径
        button.setIcon(icon)
        button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print("Button clicked!")


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
