# -*- coding: utf-8 -*-
from PyQt5 import QtCore
# from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys

class App(QApplication):

    # 1.分发到应用 notify()
    def notify(self, receiver, evt) -> bool:
        if receiver.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress:
            print(receiver, evt)
        return super().notify(receiver,evt)

class Btn(QPushButton):

    #2. 分发每个控件的 event()
    def event(self, evt) -> bool:
        if evt.type() == QEvent.MouseButtonPress:
            print(evt)
        return super().event(evt)

    # 3. 分发到具体 事件
    def mousePressEvent(self, e) -> None:
        print("我被点击了--cjw")
        return super().mousePressEvent(e)

# 创建实例应用
app = App(sys.argv)

# 创建控件
windows = QWidget()
# 设置标题
windows.setWindowTitle("")
# 设置控件大小
windows.resize(400,400)

btn = Btn(windows)
btn.setText("点我")
btn.clicked.connect(lambda : print("我被点击了"))
# 展示控件
windows.show()

# app.exec_() 创建循环
sys.exit(app.exec_())