#include "flowButtons.h"

FlowButtons::FlowButtons()
  :QHBoxLayout()
{
  QPushButton * backB = new QPushButton("Back");
  QPushButton * nextB = new QPushButton("Next");
  QPushButton * cancelB = new QPushButton("Cancel");
  QPalette pal = nextB->palette();

  pal.setColor(QPalette::Background, Qt::blue);
  nextB -> setAutoFillBackground(true);
  nextB -> setPalette(pal);
  this -> addWidget(cancelB);
  this -> addStretch(1);
  this -> addWidget(backB);
  this -> addWidget(nextB);
}
