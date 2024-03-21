import sys

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

        self.lepic = QLineEdit(self)
        self.lepic.setGeometry(740, 530, 60, 30)  # 设置大小
        self.lepic.setStyleSheet("background-color: gray")  # 设置背景色
        self.lepic.setText("pic")  # 设置默认文本

        self.lex = QLineEdit(self)
        self.lex.setGeometry(100, 600, 40, 30)  # 设置大小
        self.lex.setStyleSheet("background-color: gray")  # 设置背景色
        self.lex.setText("X")  # 设置默认文本

        self.ley = QLineEdit(self)
        self.ley.setGeometry(180, 600, 40, 30)  # 设置大小
        self.ley.setStyleSheet("background-color: gray")  # 设置背景色
        self.ley.setText("y")  # 设置默认文本

        self.lew = QLineEdit(self)
        self.lew.setGeometry(270, 600, 40, 30)  # 设置大小
        self.lew.setStyleSheet("background-color: gray")  # 设置背景色
        self.lew.setText("w")  # 设置默认文本

        self.leh = QLineEdit(self)
        self.leh.setGeometry(340, 600, 40, 30)  # 设置大小
        self.leh.setStyleSheet("background-color: gray")  # 设置背景色
        self.leh.setText("h")  # 设置默认文本

        piclabel = QLabel("Pic：", self)
        piclabel.setGeometry(700, 520, 200, 50)
        font = piclabel.font()
        font.setPointSize(20)
        piclabel.setFont(font)
        piclabel.setStyleSheet("color: #555555;")

        RIOlabel = QLabel("RIO：", self)
        RIOlabel.setGeometry(30, 570, 400, 50)
        font = RIOlabel.font()
        font.setPointSize(20)
        RIOlabel.setFont(font)
        RIOlabel.setStyleSheet("color: #555555;")

        RIOlabel = QLabel("X：", self)
        RIOlabel.setGeometry(80, 590, 400, 50)
        font = RIOlabel.font()
        font.setPointSize(20)
        RIOlabel.setFont(font)

        RIOlabel = QLabel("Y：", self)
        RIOlabel.setGeometry(160, 590, 400, 50)
        font = RIOlabel.font()
        font.setPointSize(20)
        RIOlabel.setFont(font)

        RIOlabel = QLabel("W：", self)
        RIOlabel.setGeometry(240, 590, 20, 50)
        font = RIOlabel.font()
        font.setPointSize(20)
        RIOlabel.setFont(font)

        RIOlabel = QLabel("H：", self)
        RIOlabel.setGeometry(320, 590, 400, 50)
        font = RIOlabel.font()
        font.setPointSize(20)
        RIOlabel.setFont(font)

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
        quitbutton.clicked.connect(self.quitClicked)
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

    def quitClicked(self):
        print("quit")
def main():

    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
