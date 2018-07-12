import sys
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

app = QtWidgets.QApplication(sys.argv)
aWindow = Window()
sys.exit(app.exec_())
