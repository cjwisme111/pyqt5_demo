# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)
# 创建空白控件,       flags 设置窗口外观标志
windows = QWidget(flags=Qt.FramelessWindowHint)
windows.resize(500,500)
red = QWidget(windows)
red.resize(200,200)
red.setStyleSheet("background-color:red;")
# 展示
windows.show()

sys.exit(app.exec_())