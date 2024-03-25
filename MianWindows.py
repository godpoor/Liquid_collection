import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QApplication, QMenuBar


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Liquid RXD")
        self.resize(1200, 800)
        # 创建菜单栏
        menubar = QMenuBar()
        # 创建“主页”菜单项
        home_menu = menubar.addMenu("主页")
        # 创建“关于”菜单项
        about_menu = menubar.addMenu("关于")

        # 创建“关于”菜单下的子菜单项
        about_action = QAction("关于作者", self)
        about_menu.addAction(about_action)

        # 信号连接到槽
        about_action.triggered.connect(self.show_about_message)

        # 设置菜单栏
        self.setMenuBar(menubar)

    def show_about_message(self):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(self, "关于", "这是一个简单的关于信息。")
        self.show()

def main():

    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
