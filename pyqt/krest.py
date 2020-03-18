from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QMessageBox, QTableWidget, QPushButton
from numpy import *
import sys

class CustomButton(QPushButton):
    def __init__(self):
        QPushButton.__init__(self)
        self.setText(' ')
        self.clicked.connect(self.set_xo)

    xo = ['x', 'o']
    def set_xo(self):
        if self.text() == ' ':
            curr_sym = CustomButton.xo.pop(0)
            CustomButton.xo.append(curr_sym)
            self.setText(curr_sym)
            mw.check()



class MainWindow(QMainWindow):
    def __init__(self, n=4):
        self.winner = ''
        self.n = n
        QMainWindow.__init__(self)

        self.setWindowTitle("xo")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()  # Создать QGridLayout
        central_widget.setLayout(grid_layout)  # Установить это размещение в центральном виджете

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(4)
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)

        self.newgame()

        central_widget.setFixedHeight(160)
        central_widget.setFixedWidth(176)
        self.setFixedWidth(175)
        self.setFixedHeight(175)
        grid_layout.addWidget(self.table, 0, 0)

    def newgame(self):
        self.winner = ''
        self.all_buttons = [[CustomButton() for j in range(self.n)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                self.table.setCellWidget(i, j, self.all_buttons[i][j])

        for i in range(self.n):
            self.table.horizontalHeader().resizeSection(i, 10)
            self.table.verticalHeader().resizeSection(i, 35)

    def findwin(self, strings):
        reply = None
        for s in strings:
            if s.find('xxx') != -1:
                self.winner = 'x'
            elif s.find('ooo') != -1:
                self.winner = 'o'
        if self.winner:
            reply = QMessageBox.question(self, 'Endgame',
                                         f"'{self.winner}' wins! Else?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.newgame()
        elif reply == QMessageBox.No:
            exit()

    def check(self):
        matrix = array([[el.text() for el in i] for i in self.all_buttons])
        self.findwin([''.join([s for s in i]) for i in matrix])
        self.findwin([''.join([s for s in i]) for i in matrix.transpose()])
        self.findwin([''.join([s for s in i]) for i in [matrix.diagonal(i)
                                                        for i in range(3 - self.n, self.n - 3 + 1)]])
        self.findwin([''.join([s for s in i]) for i in [matrix[:, ::-1].diagonal(i)
                                                        for i in range(3 - self.n, self.n - 3 + 1)]])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())