#include "flowButtons.h"

FlowButtons::FlowButtons(QWidget * parent)
  :QHBoxLayout(parent)
{
  QPushButton * backB = new QPushButton("Back");
  QPushButton * nextB = new QPushButton("Next");
  QPushButton * cancelB = new QPushButton("Cancel");
  this -> addStretch(1);
  this -> addWidget(backB);
  this -> addWidget(nextB);
  this -> addWidget(cancelB);
}
