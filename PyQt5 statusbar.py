import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon


# 這個example的功用是demo視窗的status bar
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 status bar example - pythonspot.com'
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Window properties are set in the initUI() method which is called in the constructor.
        # The method:
        self.statusBar().showMessage('hello')
        # *************
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())