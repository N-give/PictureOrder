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
    
    return dropdown


class PlayerInfoWidget(QWidget):

    def __init__(self, parent):
        super(PlayerInfoWidget, self).__init__(parent)

        # Create push buttons for next and back
        pb_next = QPushButton("Next")

        next_button_layout = QHBoxLayout()
        next_button_layout.addStretch(1)
        next_button_layout.addWidget(pb_next)

        # Create line edits
        # Creating player fields
        label_player = QLabel('Player Name')
        le_player_first_name = create_QLineEdit("First Name")
        le_player_last_name = create_QLineEdit("Last Name")
        player_hlayout = QHBoxLayout()
        player_hlayout.addWidget(le_player_first_name)
        player_hlayout.addWidget(le_player_last_name)

        # Creat parent fields
        label_parent = QLabel('Parent Name')
        le_parent_first_name = create_QLineEdit("First Name")
        le_parent_last_name = create_QLineEdit("Last Name")
        parent_hlayout = QHBoxLayout()
        parent_hlayout.addWidget(le_parent_first_name)
        parent_hlayout.addWidget(le_parent_last_name)

        # Create phone fields
        label_phone = QLabel('Phone Number')
        le_area_code = create_QLineEdit("XXX")
        le_prefix = create_QLineEdit("XXX")
        le_line_number = create_QLineEdit("XXXX")
        phone_hlayout = QHBoxLayout()
        phone_hlayout.addWidget(QLabel('('))
        phone_hlayout.addWidget(le_area_code)
        phone_hlayout.addWidget(QLabel(')'))
        phone_hlayout.addWidget(le_prefix)
        phone_hlayout.addWidget(QLabel('-'))
        phone_hlayout.addWidget(le_line_number)

        # Create address fields
        label_address = QLabel('Mailing Address')
        le_address1 = create_QLineEdit("Address Line 1")
        le_address2 = create_QLineEdit("Address Line 2")
        le_city = create_QLineEdit("City")
        cb_state = create_stateDropdown()
        le_zip_code = create_QLineEdit('Zipe Code')

        city_hlayout = QHBoxLayout()
        city_hlayout.addWidget(le_city)
        city_hlayout.addWidget(cb_state)
        city_hlayout.addWidget(le_zip_code)

        address_vlayout = QVBoxLayout()
        address_vlayout.addWidget(le_address1)
        address_vlayout.addWidget(le_address2)
        address_vlayout.addLayout(city_hlayout)

        # Create league line edit
        label_league = QLabel('League')
        le_league = create_QLineEdit("ex. Coaches' Pitch")

        # Create coach line edit
        label_coach = QLabel('Coach')
        le_coach = create_QLineEdit('ex. Shannon')

        # Create team line edit
        label_team = QLabel('Team')
        le_team = create_QLineEdit('ex. Reds')

        # Set vertical layout for player information window 
        v_layout = QFormLayout()
        v_layout.addRow(label_player, player_hlayout)
        v_layout.addRow(label_parent, parent_hlayout)
        v_layout.addRow(label_phone, phone_hlayout)
        v_layout.addRow(label_address, address_vlayout)
        v_layout.addRow(label_league, le_league)
        v_layout.addRow(label_coach, le_coach)
        v_layout.addRow(label_team, le_team)
        v_layout.addRow(next_button_layout)

        self.setLayout(v_layout)


