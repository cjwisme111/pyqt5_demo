# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys

# 创建实例应用
app = QApplication(sys.argv)
# 创建控件
windows = QWidget()
# 设置标题
windows.setWindowTitle("qwidget 内容边距")
# 设置控件大小
windows.resize(600,600)

label = QLabel(windows)
label.resize(300,300)
label.setText("hello world")
label.setContentsMargins(50,50,50,50)
label.setStyleSheet("background-color:cyan;color:red;")



# 获取内容边距
print(label.getContentsMargins())
print(label.contentsRect())

# 展示控件
windows.show()
# app.exec_() 创建循环
sys.exit(app.exec_())