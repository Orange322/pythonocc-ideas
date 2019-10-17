import sys
#import os
#from OCC.Display.qtDisplay import qtViewer3d
from PyQt5 import QtWidgets, QtCore, QtGui
#import os

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from Xianshi import jiemian

from OCC.Display.SimpleGui import init_display
from OCC.Extend.DataExchange import read_iges_file,read_step_file,read_stl_file


#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"




class Form(QWidget):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)
        self.resize(400,400)    #设置窗口大小
        #垂直布局
        layout=QVBoxLayout()



        #创建按钮1
        self.btn1=QPushButton('open  3D moudel')
        #setCheckable()：设置按钮是否已经被选中，如果为True，则表示按钮将保持已点击和释放状态
        self.btn1.setCheckable(True)
        #toggle()：在按钮状态之间进行切换
        self.btn1.toggle()
        #点击信号与槽函数进行连接，这一步实现：在控制台输出被点击的按钮
        self.btn1.clicked.connect(lambda :self.whichbtn(self.btn1))
        #点击信号与槽函数进行连接，实现的目的：输入安妞的当前状态，按下还是释放
        self.btn1.clicked.connect(self.btnstate)

        #添加控件到布局中
        layout.addWidget(self.btn1)

        #创建按钮2
        self.btn2=QPushButton('image')
        #为按钮2添加图标
        self.btn2.setIcon(QIcon(QPixmap(r'C:\Users\lenovo\Desktop\Tushibie\lianxi5.jpg')))
        ##点击信号与槽函数进行连接，这一步实现：在控制台输出被点击的按钮
        self.btn2.clicked.connect(lambda :self.whichbtn(self.btn2))
        # 点击信号与槽函数进行连接
        self.btn2.clicked.connect(self.biubiu)
        #self.btn2.setAutoRepeat(True)
        layout.addWidget(self.btn2)

        self.btn3=QPushButton('Disabled')
        #setEnabled()设置按钮是否可以使用，当设置为False的时候，按钮变成不可用状态，点击它不会发射信号
        self.btn3.setEnabled(False)

        layout.addWidget(self.btn3)

        #创建按钮并添加快捷键
        self.btn4=QPushButton('&Download')
        #setDefault()：设置按钮的默认状态
        self.btn4.setDefault(True)
        ##点击信号与槽函数进行连接，这一步实现：在控制台输出被点击的按钮
        self.btn4.clicked.connect(lambda :self.whichbtn(self.btn4))

        self.btn4.clicked.connect(self.showocc)
        #self.showocc()

        layout.addWidget(self.btn4)

        self.setWindowTitle("Button demo")
        self.setLayout(layout)

    def btnstate(self): #isChecked()：判断按钮的状态，返回值为True或False
        if self.btn1.isChecked():

            print('button pressed')
        else:
            print('button released')


    def biubiu(self):
        display, start_display, add_menu, add_function_to_menu = init_display()
        self.shapes = read_step_file(r'C:\Users\lenovo\Desktop\dest1.step')
        display.DisplayShape(self.shapes, update=True)
        start_display()

    def whichbtn(self, btn):
        # 输出被点击的按钮
        print('clicked button is ' + btn.text())


    def showocc(self):
        #self.shapes = read_step_file(r'C:\Users\lenovo\Desktop\dest1.step')
        #init_display()
        #display, start_display, add_menu, add_function_to_menu = init_display()
        #self.abc=init_display()
        #display.DisplayShape(self.shapes, update=True)
        #start_display()  # 不加这一行代码直接exit with code 0闪退了，因为没有类似于print的输出，直接就运行成功关闭了。
        #self.layout().addQWidget(self.abc)
        #self.abc.show()
        #showocc.destroyed.connect(self.self.print_destroyinfo)

        if __name__ == '__main__':
            #shapes = read_step_file(r'C:\Users\lenovo\Desktop\dest1.step')
            display, start_display, add_menu, add_function_to_menu = init_display()

            #display.DisplayShape(shapes, update=True)
            start_display()

            pass


if __name__ == '__main__':
    app=QApplication(sys.argv)
    btnDemo=Form()                 #窗口名字
    btnDemo.show()
    sys.exit(app.exec_())








