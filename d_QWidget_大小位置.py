# -*- coding: utf-8 -*-
from PyQt5.QtCore import QPoint,QSize
from PyQt5.QtWidgets import QApplication,QWidget
import sys

# 创建实例应用
app = QApplication(sys.argv)
# 创建控件
windows = QWidget()
# 设置标题
windows.setWindowTitle("大小位置")
# 设置控件大小
windows.resize(400,400)
windows.move(100,100)
# print(windows.x())
# print(windows.y())
red = QWidget(windows)
red.setStyleSheet("background-color:red;")
red.move(150,150)
# print(red.x())
# print(red.y())

# pos()  返回 Qcore.QPoint()
# print(red.pos().x(),red.pos().y())

# print(red.width(),red.height())

# size()  返回 QCore.QSize() 对象
# print(red.size())

# geometry  返回 PyQt5.QtCore.QRect(x, y, width, height)
# print(red.geometry())

# PyQt5.QtCore.QRect(0, 0, 100, 30)
# print(red.rect())

# print(windows.frameSize())

print(windows.frameGeometry())

# 展示控件
windows.show()
# app.exec_() 创建循环
sys.exit(app.exec_())