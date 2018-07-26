#include "playerName.h"

InfoFormWidget::InfoFormWidget()
  :QWidget()
{
  QVBoxLayout * wLayout = new QVBoxLayout(this); // Overall widget layout
  QVBoxLayout * leLayout = new QVBoxLayout(); // Vertical layout for line edits
  QLineEdit * playerFirst = new QLineEdit();
  QLineEdit * playerLast = new QLineEdit();
  QGroupBox * playerBox = new QGroupBox("Player Information");
  FlowButtons * flowButtons = new FlowButtons();

  playerFirst -> setPlaceholderText("First Name");
  playerLast -> setPlaceholderText("Last Name");
  leLayout -> addWidget(playerFirst);
  leLayout -> addWidget(playerLast);
  playerBox -> setAlignment(Qt::AlignLeft);
  playerBox -> setLayout(leLayout);
  wLayout -> addWidget(playerBox);
  wLayout -> addLayout(flowButtons);
  this -> setLayout(wLayout);
}
