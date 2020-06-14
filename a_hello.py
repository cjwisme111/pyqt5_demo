# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication
import sys


from b_qobject import Windows

# 创建实例应用
app = QApplication(sys.argv)

# 创建控件
windows = Windows()
# 展示控件
windows.show()

# app.exec_() 创建循环
sys.exit(app.exec_())

