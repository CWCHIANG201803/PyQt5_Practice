import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


# 如同C++的class
class App(QWidget):
    # 事實上就是constructor
    def __init__(self):
        # 在類別的繼承中，如果重定義某個方法
        # 該方法會覆蓋父類別的同名function
        # 但有些時候我們希望能同時實現父類別的功能
        # 這時就需要調用父類別的方法了，這時可以使用 super來實現這目標
        super().__init__()
        # 下面這些都是在定義窗體的屬性值
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 240
        self.initUI()

    # 這個function的功能就如同於set
    def initUI(self):
        # 下面這些function是調整東西
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

# 這個就類似於C++中的main()
if __name__ == '__main__':
    # This calls the constructor of the C++ class QApplication.
    # It uses sys.argv (argc and argv in C++) to initialize the QT application.
    # There are a bunch of arguments that you can pass to QT, like styles, debugging stuff and so on.
    app = QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())