import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt6.QtGui import QPixmap


class testCLA(QMainWindow):
    def __init__(self,father):
        super().__init__()
        self.father = father
        self.initUI()

    def initUI(self):
        self.setWindowTitle("test")
        self.setGeometry(100, 100, 400, 300)
        # 添加显示PNG的QLabel
        self.picLabel = QLabel(self)
        self.picLabel.setGeometry(30, 30, 600, 500)  # 设置大小
        self.picLabel.setScaledContents(True)  # 图片自适应大小
        self.picLabel.setToolTip('Position: (0, 0)')  # 设置默认提示文本
        # 加载PNG图片
        pixmap = QPixmap("path_to_your_image.png")
        self.picLabel.setPixmap(pixmap)
        self.show()

    def mouseMoveEvent(self, event):
        pos = event.pos()
        x = pos.x()
        y = pos.y()

        if 30 <= x <= 630 and 30 <= y <= 530:  # 检查鼠标是否在图片区域内
            # 计算并设置对应的数值
            rel_x = x - 30  # 相对于图片左上角的X坐标
            rel_y = y - 30  # 相对于图片左上角的Y坐标
            self.picLabel.setToolTip(f'Position: ({rel_x}, {rel_y})')
    def test(self):
        print("here is test")

def main():
    app = QApplication(sys.argv)
    ex = testCLA()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
