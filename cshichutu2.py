# -*- coding: utf-8 -*-
import sys
#import os
#from OCC.Display.qtDisplay import qtViewer3d
#from PyQt5 import QtWidgets, QtCore, QtGui
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
#from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from Xianshi import jiemian
from OCC.Display.SimpleGui import init_display
#from OCC.Extend.DataExchange import read_iges_file,read_step_file,read_stl_file

class Form(QWidget):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)
        self.resize(400,400)    #设置窗口大小
        #垂直布局
        layout = QVBoxLayout()
        # 创建按钮并添加快捷键
        self.btn4 = QPushButton('&Download')
        # setDefault()：设置按钮的默认状态
        self.btn4.setDefault(True)
        ##点击信号与槽函数进行连接，这一步实现：在控制台输出被点击的按钮
        #self.btn4.clicked.connect(lambda: self.whichbtn(self.btn4))
        self.btn4.clicked.connect(self.showocc)


        layout.addWidget(self.btn4)

        self.setWindowTitle("Button demo")
        self.setLayout(layout)
        self.show()

    def showocc(self):
        display, start_display, add_menu, add_function_to_menu = init_display()
        start_display()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    btnDemo=Form()                 #窗口名字
    btnDemo.show()
    sys.exit(app.exec_())
