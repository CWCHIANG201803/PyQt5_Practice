import sys
# 加入QPush button module
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    def __init__(self):
        # 在類別的繼承中，如果重定義某個方法
        # 該方法會覆蓋父類別的同名function
        # 但有些時候我們希望能同時實現父類別的功能
        # 這時就需要調用父類別的方法了，這時可以使用 super來實現這目標
        super().__init__()

        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 500
        self.top = 500
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # QPushButton creates the widget, the first argument is text on the button.
        # The method setToolTip shows the message when the user points the mouse on the button.
        # Finally the button is moved to the coordinates x=100,y=70.

        button = QPushButton('PyQt5 button', self)
        # 游標放在上面產生註記
        button.setToolTip('This is an example button')
        # button擺放位置
        button.move(100,100)
        button.resize(100,70)
        # Add connect the method to the click with:
        # 引數裡面是要執行的事件
        button.clicked.connect(self.on_click)

        self.show()

    # We need to create a method for a button click:
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())