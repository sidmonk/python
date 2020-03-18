from PyQt5.QtCore import pyqtSignal, QObject

class nut(QObject):
    cracked = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

    def crack(self):
        self.cracked.emit()

def crackit():
    print("Не понимаю, зачем это")

hazelnut = nut()
hazelnut.cracked.connect(crackit)
hazelnut.crack()
