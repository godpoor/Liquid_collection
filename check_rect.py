"""
Author: Pro Good
Emial: godpoor@163.com
"""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QPainter
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QPushButton, QGraphicsView, QWidget,QGraphicsScene
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
        self.lepic.setGeometry(700, 530, 60, 30)  # 设置大小
        self.lepic.setStyleSheet("border-radius: 10px;background-color: #D3D3D3")  # 设置背景色
        self.lepic.setText("pic")  # 设置默认文本
        self.lepic.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lex = QLineEdit(self)
        self.lex.setGeometry(70, 600, 40, 30)  # 设置大小
        self.lex.setStyleSheet("border-radius: 10px;background-color: #D3D3D3")  # 设置背景色
        self.lex.setText("X")  # 设置默认文本
        self.lex.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ley = QLineEdit(self)
        self.ley.setGeometry(170, 600, 40, 30)  # 设置大小
        self.ley.setStyleSheet("border-radius: 10px;background-color: #D3D3D3")  # 设置背景色
        self.ley.setText("Y")  # 设置默认文本
        self.ley.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lew = QLineEdit(self)
        self.lew.setGeometry(270, 600, 40, 30)  # 设置大小
        self.lew.setStyleSheet("border-radius: 10px;background-color: #D3D3D3")  # 设置背景色
        self.lew.setText("W")  # 设置默认文本
        self.lew.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.leh = QLineEdit(self)
        self.leh.setGeometry(380, 600, 40, 30)  # 设置大小
        self.leh.setStyleSheet("border-radius: 10px;background-color: #D3D3D3")  # 设置背景色
        self.leh.setText("H")  # 设置默认文本
        self.leh.setAlignment(Qt.AlignmentFlag.AlignCenter)

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



        self.show()
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def leftClicked(self):
        print("left")

    def playClicked(self):
        print("play")

    def rightClicked(self):
        print("right")

    def confirmClicked(self):
        print("confirm")

class CustomGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)  # 设置为拖动模式
        self.setRenderHint(QPainter.RenderHint.Antialiasing)

    def wheelEvent(self, event):
        # Check if Ctrl key is pressed
        if QApplication.keyboardModifiers() == Qt.KeyboardModifier.ControlModifier:
            # Scale factor
            zoomInFactor = 1.25
            zoomOutFactor = 1 / zoomInFactor
            # Zoom
            if event.angleDelta().y() > 0:
                zoomFactor = zoomInFactor
            else:
                zoomFactor = zoomOutFactor
            self.scale(zoomFactor, zoomFactor)

    def mouseMoveEvent(self, event):
        scenePos = self.mapToScene(event.pos())
        pixmap = self.scene().items()[0]  # 获取场景中的第一个项（这里是pixmap）

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
