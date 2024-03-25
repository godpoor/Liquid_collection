import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow,  QMenuBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("菜单栏示例")
        self.setGeometry(100, 100, 800, 600)

        # 创建菜单栏
        menubar = QMenuBar()

        # 创建“主页”菜单项
        home_menu = menubar.addMenu("主页")

        # 创建“关于”菜单项
        about_menu = menubar.addMenu("关于")

        # 创建“关于”菜单下的子菜单项
        about_action = QAction("关于我们", self)
        about_menu.addAction(about_action)

        # 信号连接到槽
        about_menu.triggered.connect(self.show_about_message)

        # 设置菜单栏
        self.setMenuBar(menubar)

    def show_about_message(self):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(self, "关于", "这是一个简单的关于信息。")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
