from PyQt5 import QtWidgets, QtGui, QtCore
from test import Ui_MainWindow      # импорт нашего сгенерированного файла
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #  изменяем шрифт и размер надписи
        self.ui.label.setFont(
            QtGui.QFont('Arial', 20)
        )

        # изменить геометрию
        self.ui.label.setGeometry(
            QtCore.QRect(210, 210, 600, 200)
        )

        self.ui.label.setText("Бамоновка - помойка!")

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())