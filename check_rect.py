"""
Author: Pro Good
Emial: godpoor@163.com
"""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QPainter
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QPushButton, QGraphicsView, QWidget, \
    QGraphicsScene
import warnings

# 忽略特定类型的 DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Check ROI")
        self.setGeometry(100, 100, 400, 300)
        self.resize(850, 650)
        self.center()

        # 添加可伸缩涂层画布
        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        # 添加QGraphicsView来显示图像
        self.graphicsView = CustomGraphicsView(self.widget)
        self.scene = QGraphicsScene(self)
        self.pixmap = QPixmap("contours.png")
        self.scene.addPixmap(self.pixmap)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setGeometry(10, 10, 830, 500)

        # 显示鼠标位置的标签
        self.label = QLabel("Pixel Pos: (0, 0)", self.widget)
        self.label.setGeometry(15, 330, 200, 400)

        # 添加其他控件
        pictlabel = QLabel("Pic：", self)
        pictlabel.setGeometry(650, 520, 70, 50)
        font = pictlabel.font()
        font.setPointSize(20)
        pictlabel.setFont(font)
        pictlabel.setStyleSheet("color: #555555;")

        RIOlabel = QLabel("ROI：", self)
        RIOlabel.setGeometry(30, 550, 60, 50)
        font = RIOlabel.font()
        font.setPointSize(20)
        RIOlabel.setFont(font)
        RIOlabel.setStyleSheet("color: #555555;")

        RIOlabel = QLabel("X:", self)
        RIOlabel.setGeometry(30, 590, 30, 50)
        font = RIOlabel.font()
        font.setPointSize(20)
        RIOlabel.setFont(font)

        RIOlabel = QLabel("Y:", self)
        RIOlabel.setGeometry(130, 590, 30, 50)
        font = RIOlabel.font()
        font.setPointSize(20)
        RIOlabel.setFont(font)

        RIOlabel = QLabel("W:", self)
        RIOlabel.setGeometry(230, 590, 35, 50)
        font = RIOlabel.font()
        font.setPointSize(20)
        RIOlabel.setFont(font)

        RIOlabel = QLabel("H:", self)
        RIOlabel.setGeometry(340, 590, 30, 50)
        font = RIOlabel.font()
        font.setPointSize(20)
        RIOlabel.setFont(font)

        tollabel = QLabel("/tol", self)
        tollabel.setGeometry(770, 520, 60, 50)
        font = tollabel.font()
        font.setPointSize(20)
        tollabel.setFont(font)
        tollabel.setStyleSheet("color: #555555;")

        self.lepic = QLineEdit(self)
        self.lepic.setGeometry(700, 530, 60, 30)
        self.lepic.setStyleSheet("border-radius: 10px;background-color: #D3D3D3")
        self.lepic.setText("pic")
        self.lepic.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lex = QLineEdit(self)
        self.lex.setGeometry(70, 600, 40, 30)
        self.lex.setStyleSheet("border-radius: 10px;background-color: #D3D3D3")
        self.lex.setText("X")
        self.lex.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ley = QLineEdit(self)
        self.ley.setGeometry(170, 600, 40, 30)
        self.ley.setStyleSheet("border-radius: 10px;background-color: #D3D3D3")
        self.ley.setText("Y")
        self.ley.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lew = QLineEdit(self)
        self.lew.setGeometry(270, 600, 40, 30)
        self.lew.setStyleSheet("border-radius: 10px;background-color: #D3D3D3")
        self.lew.setText("W")
        self.lew.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.leh = QLineEdit(self)
        self.leh.setGeometry(380, 600, 40, 30)
        self.leh.setStyleSheet("border-radius: 10px;background-color: #D3D3D3")
        self.leh.setText("H")
        self.leh.setAlignment(Qt.AlignmentFlag.AlignCenter)

        remarkbutton = QPushButton(self)
        remarkbutton.setGeometry(450, 600, 60, 30)
        remarkbutton.setText("remark")
        remarkbutton.clicked.connect(self.remarkClicked)
        remarkbutton.setStyleSheet("QPushButton {border-radius: 8px; border: 2px solid #706D6C;}")

        leftbutton = QPushButton(self)
        leftbutton.setGeometry(340, 550, 50, 40)
        lefticon = QIcon("pic/left.png")
        leftbutton.setIcon(lefticon)
        leftbutton.clicked.connect(self.leftClicked)
        leftbutton.setStyleSheet("border-radius: 10px; border: 1px solid #706D6C")

        playbutton = QPushButton(self)
        playbutton.setGeometry(400, 550, 50, 40)
        playicon = QIcon("pic/play.png")
        playbutton.setIcon(playicon)
        playbutton.clicked.connect(self.playClicked)
        playbutton.setStyleSheet("border-radius: 10px; border: 1px solid #706D6C;")

        rightbutton = QPushButton(self)
        rightbutton.setGeometry(460, 550, 50, 40)
        righticon = QIcon("pic/right.png")
        rightbutton.setIcon(righticon)
        rightbutton.clicked.connect(self.rightClicked)
        rightbutton.setStyleSheet("border-radius: 10px; border: 1px solid #706D6C")

        confirmbutton = QPushButton(self)
        confirmbutton.setGeometry(720, 590, 100, 50)
        confirmbutton.setText("Confirm")
        confirmbutton.clicked.connect(self.confirmClicked)
        confirmbutton.setStyleSheet("QPushButton {border-radius: 10px; border: 2px solid #CCCCCC;}")

        quitbutton = QPushButton(self)
        quitbutton.setGeometry(600, 590, 100, 50)
        quitbutton.setText("quit")
        quitbutton.clicked.connect(QApplication.instance().quit)
        quitbutton.setStyleSheet("QPushButton {border-radius: 10px; border: 2px solid #CCCCCC;}")

        # 调用zoomToRect函数将画布放大到指定位置
        self.zoomToRect(914, 835, 14, 14, zoomFactor=0.2)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #使ROI始终保持在视野中心
    def zoomToRect(self, x, y, w, h, zoomFactor=0.8):
        # 计算放大比例
        scale_x = self.graphicsView.width() / w
        scale_y = self.graphicsView.height() / h
        scale = min(scale_x, scale_y) * zoomFactor  # 添加缩放因子
        # 设置放大比例
        self.graphicsView.resetTransform()
        self.graphicsView.scale(scale, scale)
        # 计算并调整视图中心以使矩形框位于中心
        rect_center_x = x + w / 1.6
        rect_center_y = y + h / 1.6
        self.graphicsView.centerOn(rect_center_x, rect_center_y)

    def leftClicked(self):
        print("left")

    def playClicked(self):
        print("play")

    def rightClicked(self):
        print("right")

    def confirmClicked(self):
        print("confirm")

    def remarkClicked(self):
        print("remark")


class CustomGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)

    def wheelEvent(self, event):
        if QApplication.keyboardModifiers() == Qt.KeyboardModifier.ControlModifier:
            zoomInFactor = 1.25
            zoomOutFactor = 1 / zoomInFactor
            if event.angleDelta().y() > 0:
                zoomFactor = zoomInFactor
            else:
                zoomFactor = zoomOutFactor
            self.scale(zoomFactor, zoomFactor)

    def mouseMoveEvent(self, event):
        scenePos = self.mapToScene(event.pos())
        pixmap = self.scene().items()[0]
        if pixmap.pixmap().rect().contains(event.pos()):
            self.window().label.setText(
                f"Pixel Pos: ({int(scenePos.x())}, {int(scenePos.y())})")
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
            self.setInteractive(True)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setDragMode(QGraphicsView.DragMode.NoDrag)
        super().mouseReleaseEvent(event)


def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
