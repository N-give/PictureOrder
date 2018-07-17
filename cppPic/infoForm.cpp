#include "infoForm.h"

InfoFormWidget::InfoFormWidget()
  :QWidget()
{
  FlowButtons * flowButtons = new FlowButtons(this);
  /*
  QPushButton * cancelB = new QPushButton("Cancel");
  QPushButton * nextB = new QPushButton("Next");

  flowButtons -> addWidget(cancelB);
  flowButtons -> addStretch(1);
  flowButtons -> addWidget(nextB);
  */

  this -> setLayout(flowButtons);
}
