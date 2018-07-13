from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class OrderFormWidget(QWidget):

    def __init__(self, parent):
        super(OrderFormWidget, self).__init__(parent)

        # Create Package A
        groupBox_A = QGroupBox('Package A:')
        item_A1 = QLabel('1 5x7 Individual Photo')
        item_A2 = QLabel('1 5x7 Team Photo')
        item_A3 = QLabel('8 Wallets')
        item_A4 = QLabel('$18.00')


        gLayout_A = QVBoxLayout()
        gLayout_A.addWidget(item_A1)
        gLayout_A.addWidget(item_A2)
        gLayout_A.addWidget(item_A3)
        gLayout_A.addWidget(item_A4)

        groupBox_A.setLayout(gLayout_A)

        form_A = QFormLayout()
        self.le_packA = QLineEdit()
        self.le_packA.setPlaceholderText('# of A')
        form_A.addRow(QLabel('Order Package A:'), self.le_packA)

        vLayout_A = QVBoxLayout()
        vLayout_A.addWidget(groupBox_A)
        vLayout_A.addLayout(form_A)

        # Create Package B
        groupBox_B = QGroupBox('Package B:')
        item_B1 = QLabel('1 8x10 Individual Photo')
        item_B2 = QLabel('1 5x7 Individual Photo')
        item_B3 = QLabel('1 5x7 Team Photo')
        item_B4 = QLabel('8 Wallets')
        item_B5 = QLabel('$26.00')

        gLayout_B = QVBoxLayout()
        gLayout_B.addWidget(item_B1)
        gLayout_B.addWidget(item_B2)
        gLayout_B.addWidget(item_B3)
        gLayout_B.addWidget(item_B4)
        gLayout_B.addWidget(item_B5)

        groupBox_B.setLayout(gLayout_B)

        form_B = QFormLayout()
        self.le_packB = QLineEdit()
        self.le_packB.setPlaceholderText('# of B')
        form_B.addRow(QLabel('Order Package B:'), self.le_packB)

        vLayout_B = QVBoxLayout()
        vLayout_B.addWidget(groupBox_B)
        vLayout_B.addLayout(form_B)
        
        # Create bot horizontal layout
        hLayout_top = QHBoxLayout()
        hLayout_top.addWidget(groupBox_A)
        hLayout_top.addWidget(groupBox_B)


        # Create Package C
        groupBox_C = QGroupBox('Package C:')
        item_C1 = QLabel('1 8x10 Individual Photo')
        item_C2 = QLabel('2 5x7 Individual Photo')
        item_C3 = QLabel('1 5x7 Team Photo')
        item_C4 = QLabel('1 8X10 Memory Mate')
        item_C5 = QLabel('$35.00')

        vLayout_C = QVBoxLayout()
        vLayout_C.addWidget(item_C1)
        vLayout_C.addWidget(item_C2)
        vLayout_C.addWidget(item_C3)
        vLayout_C.addWidget(item_C4)
        vLayout_C.addWidget(item_C5)

        groupBox_C.setLayout(vLayout_C)

        # Create Package D
        groupBox_D = QGroupBox('Package D:')
        item_D1 = QLabel('1 8x10 Magazine Cover')
        item_D2 = QLabel('1 8x10 Individual Photo')
        item_D3 = QLabel('1 5x7 Individual Photo')
        item_D4 = QLabel('1 8x10 Memory Mate')
        item_D5 = QLabel('$44.00')

        vLayout_D = QVBoxLayout()
        vLayout_D.addWidget(item_D1)
        vLayout_D.addWidget(item_D2)
        vLayout_D.addWidget(item_D3)
        vLayout_D.addWidget(item_D4)
        vLayout_D.addWidget(item_D5)

        groupBox_D.setLayout(vLayout_D)

        
        # Create bot horizontal layout
        hLayout_bot = QHBoxLayout()
        hLayout_bot.addWidget(groupBox_C)
        hLayout_bot.addWidget(groupBox_D)

        # Create push buttons for cancel, back, and next
        self.pb_cancel = QPushButton("Cancel")
        self.pb_back = QPushButton("Back")
        self.pb_next = QPushButton("Next")

        next_button_layout = QHBoxLayout()
        next_button_layout.addStretch(1)
        next_button_layout.addWidget(self.pb_cancel)
        next_button_layout.addWidget(self.pb_back)
        next_button_layout.addWidget(self.pb_next)

        v_layout = QVBoxLayout()
        v_layout.addLayout(hLayout_top)
        v_layout.addLayout(hLayout_bot)
        v_layout.addLayout(next_button_layout)

        self.setLayout(v_layout)
