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

        # Creating order list
        self.orders = []

        # button click event listeners
        self.player_form_widget.pb_cancel.clicked.connect(self.cancel_playerForm)
        self.player_form_widget.pb_next.clicked.connect(self.next_playerForm)

        # self.order_form.pb_cancel.clicked.connect(self.cancel_orderForm)
        self.order_form.pb_back.clicked.connect(self.back_orderForm)
        # self.order_form.pb_next.clicked.connect(self.next_orderForm)


    # Player info flow control buttons
    def next_playerForm(self):
        self.currentIndex += 1
        self.currentIndex %= QStackedWidget.__len__(self.widget_stack)
        self.widget_stack.setCurrentIndex(self.currentIndex)

        self.orders.append(PictureOrder())
        self.orders[len(self.orders) - 1].player_name = ' '.join([
            self.player_form_widget.le_player_first.text().strip(),
            self.player_form_widget.le_player_last.text().strip()
            ])

        self.orders[len(self.orders) - 1].parent_name = ' '.join([
            self.player_form_widget.le_parent_first.text().strip(),
            self.player_form_widget.le_parent_last.text().strip()
            ])

        self.orders[len(self.orders) - 1].phone = ''.join([
            self.player_form_widget.le_area_code.text().strip(),
            self.player_form_widget.le_prefix.text().strip(),
            self.player_form_widget.le_line_number.text().strip()
            ])

        self.orders[len(self.orders) - 1].address = '\n'.join([
            self.player_form_widget.le_address1.text().strip(),
            self.player_form_widget.le_address2.text().strip(),
            ' '.join([
                self.player_form_widget.le_city.text().strip(),
                self.player_form_widget.cb_state.currentText().strip(),
                self.player_form_widget.le_zip_code.text().strip()
                ])
            ])

        self.orders[len(self.orders) - 1].league = self.player_form_widget.le_league.text().strip()
        self.orders[len(self.orders) - 1].coach = self.player_form_widget.le_coach.text().strip()
        self.orders[len(self.orders) - 1].team = self.player_form_widget.le_league.text().strip()


    def cancel_playerForm(self):
        print("cancel press")


    def back_orderForm(self):
        self.currentIndex -= 1
        self.currentIndex %= QStackedWidget.__len__(self.widget_stack)
        self.widget_stack.setCurrentIndex(self.currentIndex)


def main(argv):
    app = QApplication(argv)
    aWindow = MyMainWindow()
    aWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
