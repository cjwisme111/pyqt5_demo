# -*- coding: utf-8 -*-
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys


class MyLabel(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("10")
        self.move(100, 100)
        self.setStyleSheet("color:red; font-size:24px;")
        self.timer_id = self.startTimer(1000)

    def setSec(self, ms):
        self.setText(ms)

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        current_val = int(self.text())
        current_val -= 1
        self.setText(str(current_val))
        if current_val == 0:
            self.killTimer(self.timer_id)
            self.deleteLater()

# 创建实例应用
app = QApplication(sys.argv)
# 创建控件
windows = QWidget()
# 设置标题
windows.setWindowTitle("定时器")
# 设置控件大小
windows.resize(400,400)

label = MyLabel(windows)
label.setSec("5")

# 展示控件
windows.show()
# app.exec_() 创建循环
sys.exit(app.exec_())