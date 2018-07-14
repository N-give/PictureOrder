import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from windowClasses import playerInfoForm, orderForm


class PictureOrder():
    pass


class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setWindowTitle('Picture Order Form')

        # Create form widgets
        self.player_form_widget = playerInfoForm.PlayerInfoWidget(self)
        self.order_form = orderForm.OrderFormWidget(self)

        # Create widget stack and add widgets
        self.widget_stack = QStackedWidget(self)
        self.widget_stack.addWidget(self.player_form_widget)
        self.widget_stack.addWidget(self.order_form)
        self.currentIndex = 0
        self.widget_stack.setCurrentIndex(self.currentIndex)

        # setting central widget to widget stack
        self.setCentralWidget(self.widget_stack)

        # button click event listeners
        self.player_form_widget.pb_cancel.clicked.connect(self.cancel_orderForm)
        self.player_form_widget.pb_next.clicked.connect(self.next_orderForm)

        self.order_form.pb_cancel.clicked.connect(self.cancel_orderForm)
        self.order_form.pb_back.clicked.connect(self.back_orderForm)
        self.order_form.pb_next.clicked.connect(self.next_orderForm)


    def next_orderForm(self):
        self.currentIndex += 1
        self.currentIndex %= QStackedWidget.__len__(self.widget_stack)
        self.widget_stack.setCurrentIndex(self.currentIndex)


    def back_orderForm(self):
        self.currentIndex -= 1
        self.currentIndex %= QStackedWidget.__len__(self.widget_stack)
        self.widget_stack.setCurrentIndex(self.currentIndex)


    def cancel_orderForm(self):
        print("cancel press")


def main(argv):
    app = QApplication(argv)
    aWindow = MyMainWindow()
    aWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
