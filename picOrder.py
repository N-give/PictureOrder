import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import playerInfoForm


class PictureOrder():
    pass


class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setWindowTitle('Picture Order Form')
        self.form_widget = playerInfoForm.PlayerInfoWidget(self)
        self.setCentralWidget(self.form_widget)


def main(argv):
    app = QApplication(argv)
    aWindow = MyMainWindow()
    aWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
