import sys
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QtWidgets.QLabel('which do you like best?')
        self.dog = QtWidgets.QRadioButton('Dogs')
        self.cat = QtWidgets.QRadioButton('Cats')
        self.btn = QtWidgets.QPushButton('Select')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.dog)
        layout.addWidget(self.cat)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 Radio Buttons')

        self.btn.clicked.connect(lambda: self.btnClk(self.dog.isChecked(), self.lbl))

        self.show()

    def btnClk(self, dogCk, lbl):
        if dogCk:
            lbl.setText('I guess you like dogs')
        else:
            lbl.setText('So its cats for you')

app = QtWidgets.QApplication(sys.argv)
aWindow = Window()
sys.exit(app.exec_())
