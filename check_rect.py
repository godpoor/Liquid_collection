import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel
from PyQt6.QtGui import QIcon
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Button Window")
        self.setGeometry(100, 100, 400, 300)

        self.initUI()

    def initUI(self):
        self.resize(850, 650)
        self.center()

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
        RIOlabel.setGeometry(240, 590, 400, 50)
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
        leftbutton.setStyleSheet("border-radius: 5px; border: 1px solid ")

        playbutton = QPushButton(self)
        playbutton.setGeometry(400, 550, 50, 40)
        playicon = QIcon("pic/play.png")
        playbutton.setIcon(playicon)
        playbutton.clicked.connect(self.playClicked)
        playbutton.setStyleSheet("border-radius: 5px; border: 1px solid ")

        rightbutton = QPushButton(self)
        rightbutton.setGeometry(460, 550, 50, 40)
        righticon = QIcon("pic/right.png")
        rightbutton.setIcon(righticon)
        rightbutton.clicked.connect(self.rightClicked)
        rightbutton.setStyleSheet("border-radius: 5px; border: 1px solid ")

        confirmbutton = QPushButton(self)
        confirmbutton.setGeometry(720, 590, 100, 50)
        confirmbutton.setText("Confirm")
        confirmbutton.clicked.connect(self.confirmClicked)

        quitbutton = QPushButton(self)
        quitbutton.setGeometry(600, 590, 100, 50)
        quitbutton.setText("quit")
        quitbutton.clicked.connect(self.quitClicked)

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
    #  关闭窗口确认
    # def closeEvent(self, event):
    #     reply = QMessageBox.question(self, 'Message',
    #                                  "Are you sure to quit?", QMessageBox.StandardButton.Yes |
    #                                  QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
    #     if reply == QMessageBox.StandardButton.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
