from PyQt5.QtWidgets import QLineEdit
from PyQt5 import QtCore

self.ley = QLineEdit(self)
self.ley.setGeometry(160, 600, 40, 30)  # 设置大小
self.ley.setStyleSheet("border-radius: 10px;background-color: gray")  # 设置背景色
self.ley.setText("Y")  # 设置默认文本
self.ley.setAlignment(QtCore.Qt.AlignCenter)  # 设置文本居中显示
