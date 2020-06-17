# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication,QWidget
import sys

# 创建实例应用
app = QApplication(sys.argv)
# 创建控件
windows = QWidget()
# 设置标题
windows.setWindowTitle("qwidget 最大最小值")
# 设置控件大小
windows.resize(400,400)

# 设置最大值
# windows.setMaximumSize(800,800)
# 设置最大宽度
windows.setMaximumWidth(400)

# 展示控件
windows.show()
# app.exec_() 创建循环
sys.exit(app.exec_())

