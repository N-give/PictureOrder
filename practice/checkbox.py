import sys
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QtWidgets.QLabel()
        self.ck = QtWidgets.QCheckBox('Do you like dogs')
        self.btn = QtWidgets.QPushButton('Push Me')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.ck)
        layout.addWidget(self.btn)

        self.setLayout(layout)

        self.btn.clicked.connect(lambda: self.btnClick(self.ck.isChecked(), self.lbl))

        self.show()
    
    def btnClick(self, ck, lbl):
        if ck:
            lbl.setText('I guess you like dogs')
        else:
            lbl.setText('Dog hater then')

app = QtWidgets.QApplication(sys.argv)
aWindow = Window()
sys.exit(app.exec_())
