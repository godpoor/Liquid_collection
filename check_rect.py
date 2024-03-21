import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QPushButton


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.setWindowTitle("Button Window")
        self.setGeometry(100, 100, 400, 300)
        self.resize(850, 650)
        self.center()



        piclabel = QLabel("Pic：", self)
        piclabel.setGeometry(650, 520, 70, 50)
        font = piclabel.font()
        font.setPointSize(20)
        piclabel.setFont(font)
        piclabel.setStyleSheet("color: #555555;")

        RIOlabel = QLabel("RIO：", self)
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
        leftbutton.setStyleSheet("border-radius: 10px; border: 1px solid ")

        playbutton = QPushButton(self)
        playbutton.setGeometry(400, 550, 50, 40)
        playicon = QIcon("pic/play.png")
        playbutton.setIcon(playicon)
        playbutton.clicked.connect(self.playClicked)
        playbutton.setStyleSheet("border-radius: 10px; border: 1px solid ")

        rightbutton = QPushButton(self)
        rightbutton.setGeometry(460, 550, 50, 40)
        righticon = QIcon("pic/right.png")
        rightbutton.setIcon(righticon)
        rightbutton.clicked.connect(self.rightClicked)
        rightbutton.setStyleSheet("border-radius: 10px; border: 1px solid ")

        confirmbutton = QPushButton(self)
        confirmbutton.setGeometry(720, 590, 100, 50)
        confirmbutton.setText("Confirm")
        confirmbutton.clicked.connect(self.confirmClicked)
        confirmbutton.setStyleSheet("QPushButton {border-radius: 10px; border: 2px solid #CCCCCC;}")

        quitbutton = QPushButton(self)
        quitbutton.setGeometry(600, 590, 100, 50)
        quitbutton.setText("quit")
        quitbutton.clicked.connect(QApplication.instance().quit)
        # quitbutton.clicked.connect(self.quitClicked)
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

    # def quitClicked(self):
    #     print("quit")
def main():

    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
