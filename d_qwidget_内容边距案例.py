# -*- coding: utf-8 -*-

# 显示内容在右下角

from PyQt5.QtWidgets import QApplication,QWidget,QLabel
import sys

# 创建实例应用
app = QApplication(sys.argv)
# 创建控件
windows = QWidget()
# 设置标题
windows.setWindowTitle("内容边距案例")
# 设置控件大小
windows.resize(400,400)
label = QLabel(windows)
# label.resize(400,400)
label.setText("hello world")
label.setStyleSheet("background-color:cyan;")

# label.move(400-label.width(),400-label.height())
label.setContentsMargins(300,370,0,0)

# 展示控件
windows.show()
# app.exec_() 创建循环
sys.exit(app.exec_())