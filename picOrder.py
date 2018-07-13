import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from windowClasses import playerInfoForm


class PictureOrder():
    pass


class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        print("stuff")
        super(MyMainWindow, self).__init__(parent)
        self.setWindowTitle('Picture Order Form')
        self.player_form_widget = playerInfoForm.PlayerInfoWidget(self)
        self.setCentralWidget(self.player_form_widget)
        self.player_form_widget.pb_next.clicked.connect(self.next_orderForm)


    def next_orderForm(self):
        print("next press")


def main(argv):
    app = QApplication(argv)
    aWindow = MyMainWindow()
    aWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
