import sys
from PyQt6.QtWidgets import QMainWindow, QApplication

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Liquid RXD")
        self.resize(1200, 800)
        #运行时弹窗
        # QMessageBox.information(self, "关于作者：", "作者：郭朴(godpoor)\nbug反馈：godpoor@163.com\nA gift to everyone at BL02U2")
        self.show()



def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()
