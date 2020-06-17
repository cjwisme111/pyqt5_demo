# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication,QWidget
import sys


# 九宫格
class Windows(QWidget):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # 设置标题
        self.setWindowTitle("位置大小案例")
        # 设置控件大小
        self.count = 10
        self.columns = 3
        self.width = 400
        self.height = 400

    def resize(self, width,height) -> None:
        super().resize(width,height)
        self.width = width
        self.height = height

    def set_count(self,count):
        self.count = count

    def set_column(self,count):
        self.columns = count

    def setup_ui(self):
        count = self.count
        columns = self.columns
        widget_width = self.width / columns
        rows_count = (count - 1) // columns + 1
        widget_height = self.height / rows_count
        for i in range(count):
            widget_box = QWidget(windows)
            widget_box.resize(widget_width, widget_height)
            widget_x = (i % columns) * widget_width
            widget_y = (i // columns) * widget_height
            widget_box.move(widget_x, widget_y)
            widget_box.setStyleSheet("background-color:red;border:1px solid yellow;")


# 创建实例应用
app = QApplication(sys.argv)
# 创建控件
windows = Windows()
windows.resize(600,600)
windows.set_count(100)
windows.setup_ui()


# 展示控件
windows.show()
# app.exec_() 创建循环
sys.exit(app.exec_())