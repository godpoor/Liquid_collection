import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from Qtcode.test import testCLA

class test1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("test1")
        self.setGeometry(100, 100, 400, 300)
        # 添加按钮
        self.button = QPushButton('Show test window', self)
        self.button.clicked.connect(self.show_test_window)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    def show_test_window(self):
        self.testCLA = testCLA(self)
        self.testCLA.test()
        self.testCLA.show()


def main():
    app = QApplication(sys.argv)
    ex=test1()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
