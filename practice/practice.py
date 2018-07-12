import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QtWidgets.QLineEdit()
        self.b1 = QtWidgets.QPushButton('Clear')
        self.b2 = QtWidgets.QPushButton('Print')
        self.s1 = QtWidgets.QSlider(Qt.Horizontal)
        self.s1.setMinimum(1)
        self.s1.setMaximum(99)
        self.s1.setValue(25)
        self.s1.setTickInterval(10)
        self.s1.setTickPosition(QtWidgets.QSlider.TicksBelow)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)
        v_box.addWidget(self.s1)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt5 practice')

        self.b1.clicked.connect(lambda: self.btnClick(self.b1, 'Hello from Clear'))
        self.b2.clicked.connect(lambda: self.btnClick(self.b2, 'Hello from Print'))
        self.s1.valueChanged.connect(self.vChange)

        self.show()
    
    def btnClick(self, b, string):
        if b.text() == 'Print':
            print(self.le.text())
        else: 
            self.le.clear()
        print(string)

    def vChange(self):
        value = str(self.s1.value())
        self.le.setText(value)

app = QtWidgets.QApplication(sys.argv)
aWindow = Window()
sys.exit(app.exec_())
