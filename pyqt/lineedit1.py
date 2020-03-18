from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from lineedit import *

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit.setText("Ку ку епт")
        self.ui.lineEdit_2.setMaxLength(7)
        # ввод пароля
        self.ui.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEdit_4.setReadOnly(True)
        self.ui.lineEdit_5.setStyleSheet("color: rgb(38, 43, 255);")
        self.ui.lineEdit_6.setStyleSheet("background-color: rgb(192, 192, 192);")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app1 = Window()
    app1.show()
    sys.exit(app.exec())