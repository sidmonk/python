from PyQt5 import QtCore, QtGui, QtWidgets
from combobox_ui import Ui_MainWindow
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #   добавить значения
        self.ui.comboBox.addItem("хуй")
        self.ui.comboBox.addItem("пизда")

        for i in range(self.ui.comboBox.count()):
            print(self.ui.comboBox.itemText(i))

        print(self.ui.comboBox.itemText(1))

        # выбрать второй индекс
        self.ui.comboBox.setCurrentIndex(1)

        # выбрать по тексту
        self.ui.comboBox.setCurrentText("хуй")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    appl = Window()
    appl.show()
    sys.exit(app.exec())