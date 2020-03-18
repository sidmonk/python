from PyQt5 import QtWidgets
from lineedit import Ui_window2
import sys

class win2(QtWidgets.QDialog):
    def __init__(self):
        super(win2, self).__init__()
        self.ui = Ui_window2()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = win2()
    application.show()
    sys.exit(app.exec())