# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, qApp, QPushButton
from PyQt5.QtCore import QObject

class Windows(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt object demo")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # self.qobject名称属性()
        # self.case_qobject()
        # self.qobject父子关系()
        # self.case_父子控件()
        # self.case_single_cao()
        # self.qobject_类型判定()
        self.qobject_删除对象()

    def qobject名称属性(self):
        obj = QObject()
        obj.setObjectName("notice")
        print(obj.objectName())
        obj.setProperty("notice_level","error")
        print(obj.property("notice_level"))

    def case_qobject(self):
        """属性名称应用案例"""

        with open("comman_style.qss") as f:
            # 设置全局样式
            qApp.setStyleSheet(f.read())

        label = QLabel(self)
        label.setText("cjw")
        label.setProperty("notice_level", "error")

        label2 = QLabel(self)
        label2.setText("hello")
        label2.setObjectName("notice")
        label2.move(100,100)

        label3 = QLabel(self)
        label3.setText("world")
        label3.setProperty("notice_level", "warning")
        label3.move(150,150)
        # label.setObjectName("notice")

    def qobject父子关系(self):
        obj0 = QObject()
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()
        obj4 = QObject()

        print("obj0",obj0)
        print("obj1",obj1)
        print("obj2",obj2)
        print("obj3",obj3)
        print("obj4",obj4)

        # 设置父关系，只能有一个父，根据最后一个声明的父控件
        obj1.setParent(obj0)
        # obj1.setParent(obj2)
        print(obj1.parent())
        obj2.setParent(obj0)
        obj3.setParent(obj1)
        obj4.setParent(obj2)

        # error 设置父控件的前提条件必须是QWidget类型
        # label = QLabel()
        # label.setParent(obj0)

        print(obj0.findChild(QObject))
        print(obj0.findChildren(QObject))

    def case_父子控件(self):
        """内存管理机制
            父控件销毁，所有子控件都销毁
        """
        obj = QObject()
        # self.obj = obj
        obj1 = QObject()
        obj1.setParent(obj)
        # 监听obj1对象释放
        obj1.destroyed.connect(lambda : print("obj1 被调用"))

    def case_single_cao(self):
        self.obj = QObject()

        def destroyed_cao(val):
            print("槽被调用了")
            print(val)

        self.obj.destroyed.connect(destroyed_cao)

        def obj_name(val):
            print("名称被改变了")
            print(val)

        self.obj.objectNameChanged.connect(obj_name)
        self.obj.setObjectName("notice")

        # 取消对象信号与槽的关系
        # self.obj.disconnect()
        self.obj.blockSignals(True)
        #
        print(self.obj.signalsBlocked())
        print(self.obj.receivers(self.obj.objectNameChanged))

    def qobject_类型判定(self):
        obj = QObject()
        btn = QPushButton(self)
        label = QLabel(self)

        objs = [obj, btn, label]
        for widget in objs:
            if widget.inherits("QPushButton"):
                print(widget)
            # print(widget.isWidgetType())

    def qobject_删除对象(self):

        obj = QObject()
        self.obj = obj
        obj2 = QObject()
        obj2.setParent(obj)
        obj3 = QObject()
        obj3.setParent(obj)

        obj2.destroyed.connect(lambda : print("obj2 被调用了"))

        # 删除只是删除栈中的变量和引用的关系
        # del obj2  # 不会触发obj2销毁函数
        obj2.deleteLater()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    windows = Windows()
    windows.show()
    sys.exit(app.exec_())