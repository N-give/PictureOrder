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
        self.le_packA.setPlaceholderText('Number of A')
        form_A.addRow(QLabel('Order Package A:'), self.le_packA)

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
        self.le_packB.setPlaceholderText('Number of B')
        form_B.addRow(QLabel('Order Package B:'), self.le_packB)

        
        # Create top horizontal layout
        hLayout_top = QHBoxLayout()
        hLayout_top.addWidget(groupBox_A)
        hLayout_top.addWidget(groupBox_B)

        hLayout_AB_order = QHBoxLayout()
        hLayout_AB_order.addLayout(form_A)
        hLayout_AB_order.addLayout(form_B)

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

        form_C = QFormLayout()
        self.le_packC = QLineEdit()
        self.le_packC.setPlaceholderText('Number of C')
        form_C.addRow(QLabel('Order Package C:'), self.le_packC)

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

        form_D = QFormLayout()
        self.le_packD = QLineEdit()
        self.le_packD.setPlaceholderText('Number of D')
        form_D.addRow(QLabel('Order Package D:'), self.le_packD)

        # Create bot horizontal layout
        hLayout_bot = QHBoxLayout()
        hLayout_bot.addWidget(groupBox_C)
        hLayout_bot.addWidget(groupBox_D)

        hLayout_CD_order = QHBoxLayout()
        hLayout_CD_order.addLayout(form_C)
        hLayout_CD_order.addLayout(form_D)

        # Create A la carte items
        self.le_wallets = QLineEdit()
        self.le_wallets.setPlaceholderText('Number of Orders')

        self.le_46Ind = QLineEdit()
        self.le_46Ind.setPlaceholderText('Number of Orders')

        self.le_57Ind = QLineEdit()
        self.le_57Ind.setPlaceholderText('Number of Orders')

        self.le_810Ind = QLineEdit()
        self.le_810Ind.setPlaceholderText('Number of Orders')

        self.le_57Team = QLineEdit()
        self.le_57Team.setPlaceholderText('Number of Orders')

        self.le_mag = QLineEdit()
        self.le_mag.setPlaceholderText('Number of Orders')

        self.le_mem = QLineEdit()
        self.le_mem.setPlaceholderText('Number of Orders')

        g_carte = QGroupBox('A la Carte')
        form_carte = QGridLayout()
        #form_carte.addWidget(QLabel('A la carte Items'), 0, 0)
        #form_carte.addWidget(QLabel('Price'), 0, 1)
        #form_carte.addWidget(QLabel('Orders'), 0, 2)

        #v_name = QVBoxLayout()
        #v_name.addWidget(QLabel('A la carte'))
        form_carte.addWidget(QLabel('8 Wallet Photos'), 1, 0)
        form_carte.addWidget(QLabel('2 4x6 Individual Photos'), 2, 0)
        form_carte.addWidget(QLabel('2 5x7 Individual Photos'), 3, 0)
        form_carte.addWidget(QLabel('1 8x10 Individual Photos'), 4, 0)
        form_carte.addWidget(QLabel('2 5x7 Team Photos'), 5, 0)
        form_carte.addWidget(QLabel('1 Magazine Cover'), 6, 0)
        form_carte.addWidget(QLabel('1 Memory Mate'), 7, 0)

        #v_price = QVBoxLayout()
        #v_price.addWidget(QLabel('Price'))
        form_carte.addWidget(QLabel('$11.00'), 1, 1)
        form_carte.addWidget(QLabel('$11.00'), 2, 1)
        form_carte.addWidget(QLabel('$11.00'), 3, 1)
        form_carte.addWidget(QLabel('$11.00'), 4, 1)
        form_carte.addWidget(QLabel('$11.00'), 5, 1)
        form_carte.addWidget(QLabel('$12.00'), 6, 1)
        form_carte.addWidget(QLabel('$14.00'), 7, 1)

        #v_les = QVBoxLayout()
        #v_les.addWidget(QLabel('Orders'))
        form_carte.addWidget(self.le_wallets, 1, 2)
        form_carte.addWidget(self.le_46Ind, 2, 2)
        form_carte.addWidget(self.le_57Ind, 3, 2)
        form_carte.addWidget(self.le_810Ind, 4, 2)
        form_carte.addWidget(self.le_57Team, 5, 2)
        form_carte.addWidget(self.le_mag, 6, 2)
        form_carte.addWidget(self.le_mem, 7, 2)

        g_carte.setLayout(form_carte)

        # Create push buttons for cancel, back, and next
        self.pb_cancel = QPushButton("Cancel")
        self.pb_back = QPushButton("Back")
        self.pb_next = QPushButton("Next")

        next_button_layout = QHBoxLayout()
        next_button_layout.addWidget(self.pb_cancel)
        next_button_layout.addStretch(1)
        next_button_layout.addWidget(self.pb_back)
        next_button_layout.addWidget(self.pb_next)

        pack_layout = QVBoxLayout()
        pack_layout.addLayout(hLayout_top)
        pack_layout.addLayout(hLayout_AB_order)
        pack_layout.addLayout(hLayout_bot)
        pack_layout.addLayout(hLayout_CD_order)

        h_layout = QHBoxLayout()
        h_layout.addLayout(pack_layout)
        h_layout.addWidget(g_carte)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(next_button_layout)

        self.setLayout(v_layout)
