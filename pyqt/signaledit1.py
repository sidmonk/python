from PyQt5 import QtCore, QtGui, QtWidgets
from signaledit import *
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    appl = Window()
    appl.show()
    sys.exit(app.exec())