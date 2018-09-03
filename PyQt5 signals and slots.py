from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)

import sys


class Dialog(QDialog):

    def slot_method(self):
        print('slot method called.')

    def __init__(self):
        super(Dialog, self).__init__()

        button = QPushButton("Click")
        # The button click (signal) is connected to the action (slot).
        # In this example, the method slot_method will be called if the signal emits.
        # This principle of connecting slots methods or function to a widget, applies to all widgets,
        button.clicked.connect(self.slot_method)



        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)

        self.setLayout(mainLayout)
        self.setWindowTitle("Button Example - pythonspot.com")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())