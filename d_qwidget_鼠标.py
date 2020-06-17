# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QCursor, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys

# 鼠标事件

class Windows(QWidget):

    def __init__(self):
        super().__init__()
        # 设置鼠标追踪
        self.setMouseTracking(True)

    def mouseMoveEvent(self, evt):
        # 鼠标点击移动事件
        print("鼠标移动了")


    def mousePressEvent(self, evt):
       print("鼠标点击了")


# 创建实例应用
app = QApplication(sys.argv)
# 创建控件
windows = Windows()
# 设置标题
windows.setWindowTitle("鼠标操作")
# 设置控件大小
windows.resize(400,400)

# 设置鼠标
# windows.setCursor(Qt.ForbiddenCursor)

# 自定义鼠标图像
pixmap = QPixmap("image/xxx.png").scaled(30,30)

# QCursor(QPixmap, hotX: int = -1, hotY: int = -1)
# hotX ,hotY:已什么点中心
# -1,-1 : 中心点
# 0 ，0  右上角
# cursor = QCursor(pixmap,hotX=0, hotY=-1)
# windows.setCursor(cursor)



# 展示控件
windows.show()
# app.exec_() 创建循环
sys.exit(app.exec_())