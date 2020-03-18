from PyQt5 import QtCore, QtGui, QtWidgets
from button import *
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # подключить кнопку
        self.ui.pushButton.clicked.connect(self.clickBtn)


    def clickBtn(self):
        self.ui.label.setText("Нажалиerqvwvewvreукмммммммw!")
        #чтобы весь текст влез
        self.ui.label.adjustSize()
        QtWidgets.QMessageBox.about(self, 'feq', 'qfe')

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_F12:
            self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app1 = Window()
    app1.show()
    sys.exit(app.exec())