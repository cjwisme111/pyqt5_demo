# -*- coding: utf-8 -*-

from  PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

# label 跟着鼠标移动

class Windows(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()
        self.setMouseTracking(True)

    def setup_ui(self):
        label = QLabel(self)
        self.label = label
        label.setText("hello world")
        label.setStyleSheet("background-color:red")

    def mouseMoveEvent(self, evt):
        # QMouseEvent
        # print(evt.x(),evt.y())
        self.label.move(evt.x()+10,evt.y()+10)

windows = Windows()
windows.show()
sys.exit(app.exec_())
