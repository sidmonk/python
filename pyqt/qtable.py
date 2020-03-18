from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from ui_qtable import Ui_MainWindow
import sys

data = [[str(i), str(2*i)] for i in range(5)]

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.setText("Очистить")

        self.ui.tableWidget.setGeometry(30, 40, 290, 190)

        # Установить размер таблицы
        self.ui.tableWidget.setColumnCount(len(data[0]))
        self.ui.tableWidget.setRowCount(len(data))

        # Назвать столбцы
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ('Столб 1', 'Столб 2')
        )

        # спрятать
        self.ui.tableWidget.horizontalHeader().setVisible(False)

        # Назвать строки
        self.ui.tableWidget.setVerticalHeaderLabels(
            ("Строка 1", "Строка 2")
        )

        # Задать размер столбца
        self.ui.tableWidget.horizontalHeader().resizeSection(1, 2)

        self.ui.tableWidget.setSelectionMode(False)

        # Всплывающая подсказка
        self.ui.tableWidget.horizontalHeaderItem(0).setToolTip("Column 1 ")

        # Заполнение
        for i in range(self.ui.tableWidget.rowCount()):
            for j in range(self.ui.tableWidget.columnCount()):
                # ячейка - класс. Запускаем конструктор
                cellinfo = QtWidgets.QTableWidgetItem(data[i][j])

                # Только для чтения
                cellinfo.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )

                # Записываем
                self.ui.tableWidget.setItem(i, j, cellinfo)


        # Сортировка
        self.ui.tableWidget.setSortingEnabled(True)

        # очистка таблицы при клике на кнопку
        self.ui.pushButton.clicked.connect(self.clear)

        # добавим comboBox в ячейку
        combo = QtWidgets.QComboBox()
        combo.addItem('1')
        combo.addItem('2')
        combo.addItem('3')
        self.ui.tableWidget.setCellWidget(i, j, combo)

        # добавим progressBar
        pr = QtWidgets.QProgressBar()
        pr.setMinimum(0)
        pr.setMaximum(100)

        # формат вывода: 10.50%
        n = 25.3564
        pr.setValue(int(n))
        pr.setFormat('{0:.2f}%'.format(n))
        self.ui.tableWidget.setCellWidget(i, j-1, pr)

    def clear(self):
        self.ui.tableWidget.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app1 = Window()
    app1.show()
    sys.exit(app.exec())