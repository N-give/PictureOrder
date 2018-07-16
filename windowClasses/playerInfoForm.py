from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


def create_QLineEdit(name):
    line_edit = QLineEdit()
    if name:
        line_edit.setPlaceholderText(name)
    return line_edit


def create_stateDropdown():
    dropdown = QComboBox()
    dropdown.addItem('Alabama')
    dropdown.addItem('Alaska')
    dropdown.addItem('Arizona')
    dropdown.addItem('Arkansas')
    dropdown.addItem('California')
    dropdown.addItem('Colorado')
    dropdown.addItem('Connecticut')
    dropdown.addItem('Delaware')
    dropdown.addItem('Florida')
    dropdown.addItem('Georgia')
    dropdown.addItem('Hawaii')
    dropdown.addItem('Idaho')
    dropdown.addItem('Illinois')
    dropdown.addItem('Indiana')
    dropdown.addItem('Iowa')
    dropdown.addItem('Kansas')
    dropdown.addItem('Kentucky')
    dropdown.addItem('Louisiana')
    dropdown.addItem('Maine')
    dropdown.addItem('Maryland')
    dropdown.addItem('Massachusetts')
    dropdown.addItem('Michigan')
    dropdown.addItem('Minnesota')
    dropdown.addItem('Mississippi')
    dropdown.addItem('Missouri')
    dropdown.addItem('Montana')
    dropdown.addItem('Nebraska')
    dropdown.addItem('Nevada')
    dropdown.addItem('New Hampshire')
    dropdown.addItem('New Jersey')
    dropdown.addItem('New Mexico')
    dropdown.addItem('New York')
    dropdown.addItem('North Carolina')
    dropdown.addItem('North Dakota')
    dropdown.addItem('Ohio')
    dropdown.addItem('Oklahoma')
    dropdown.addItem('Oregon')
    dropdown.addItem('Pennsylvania')
    dropdown.addItem('Rhode Island')
    dropdown.addItem('South Carolina')
    dropdown.addItem('South Dakota')
    dropdown.addItem('Tennessee')
    dropdown.addItem('Texas')
    dropdown.addItem('Utah')
    dropdown.addItem('Vermont')
    dropdown.addItem('Virginia')
    dropdown.addItem('Washington')
    dropdown.addItem('West Virginia')
    dropdown.addItem('Wisconsin')
    dropdown.addItem('Wyoming')
    
    dropdown.setStyleSheet("combobox-popup: O")
    dropdown.setMaxVisibleItems(5)

    return dropdown


class PlayerInfoWidget(QWidget):

    def __init__(self, parent):
        super(PlayerInfoWidget, self).__init__(parent)

        # Create push buttons for next and back
        self.pb_next = QPushButton("Next")
        self.pb_cancel = QPushButton("Cancel")

        next_button_layout = QHBoxLayout()
        next_button_layout.addWidget(self.pb_cancel)
        next_button_layout.addStretch(1)
        next_button_layout.addWidget(self.pb_next)

        # Create line edits
        # Creating player fields
        self.label_player = QLabel('Player Name')
        self.le_player_first = create_QLineEdit("First Name")
        self.le_player_last = create_QLineEdit("Last Name")
        player_hlayout = QHBoxLayout()
        player_hlayout.addWidget(self.le_player_first)
        player_hlayout.addWidget(self.le_player_last)

        # Creat parent fields
        self.label_parent = QLabel('Parent Name')
        self.le_parent_first = create_QLineEdit("First Name")
        self.le_parent_last = create_QLineEdit("Last Name")
        parent_hlayout = QHBoxLayout()
        parent_hlayout.addWidget(self.le_parent_first)
        parent_hlayout.addWidget(self.le_parent_last)

        # Create phone fields
        self.label_phone = QLabel('Phone Number')
        self.le_area_code = create_QLineEdit("XXX")
        self.le_prefix = create_QLineEdit("XXX")
        self.le_line_number = create_QLineEdit("XXXX")
        phone_hlayout = QHBoxLayout()
        phone_hlayout.addWidget(QLabel('('))
        phone_hlayout.addWidget(self.le_area_code)
        phone_hlayout.addWidget(QLabel(')'))
        phone_hlayout.addWidget(self.le_prefix)
        phone_hlayout.addWidget(QLabel('-'))
        phone_hlayout.addWidget(self.le_line_number)

        # Create address fields
        self.label_address = QLabel('Mailing Address')
        self.le_address1 = create_QLineEdit("Address Line 1")
        self.le_address2 = create_QLineEdit("Address Line 2")
        self.le_city = create_QLineEdit("City")
        self.cb_state = create_stateDropdown()
        self.le_zip_code = create_QLineEdit('Zip Code')

        city_hlayout = QHBoxLayout()
        city_hlayout.addWidget(self.le_city)
        city_hlayout.addWidget(self.cb_state)
        city_hlayout.addWidget(self.le_zip_code)

        address_vlayout = QVBoxLayout()
        address_vlayout.addWidget(self.le_address1)
        address_vlayout.addWidget(self.le_address2)
        address_vlayout.addLayout(city_hlayout)

        # Create league line edit
        self.label_league = QLabel('League')
        self.le_league = create_QLineEdit("ex. Coaches Pitch")

        # Create coach line edit
        self.label_coach = QLabel('Coach')
        self.le_coach = create_QLineEdit('ex. Shannon')

        # Create team line edit
        self.label_team = QLabel('Team')
        self.le_team = create_QLineEdit('ex. Reds')

        # Set vertical layout for player information window 
        form_player = QFormLayout()
        form_player.addRow(self.label_player, player_hlayout)
        form_player.addRow(self.label_parent, parent_hlayout)
        form_player.addRow(self.label_phone, phone_hlayout)
        form_player.addRow(self.label_address, address_vlayout)
        form_player.addRow(self.label_league, self.le_league)
        form_player.addRow(self.label_coach, self.le_coach)
        form_player.addRow(self.label_team, self.le_team)

        v_layout = QVBoxLayout()
        v_layout.addLayout(form_player)
        v_layout.addLayout(next_button_layout)

        self.setLayout(v_layout)
