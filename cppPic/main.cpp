#include "main.h"

using namespace std;

int main(int argc, char ** argv){
  QApplication app(argc, argv);

  InfoFormWidget * window = new InfoFormWidget();
  window -> setWindowTitle("Picture Order Form");
  /*
  window.setWindowTitle("Picture Order Form");

  //QPushButton * button = new QPushButton("test");

  QVBoxLayout * vLayout = new QVBoxLayout(&window);
  QHBoxLayout * hLayout1 = new QHBoxLayout();
  QHBoxLayout * hLayout2 = new QHBoxLayout();
  QLineEdit * le1 = new QLineEdit();
  le1->setPlaceholderText("testing");
  QLineEdit * le2 = new QLineEdit();
  le2->setPlaceholderText("testing");
  QPushButton * button1 = new QPushButton("test");
  QPushButton * button2 = new QPushButton("test");
  hLayout1->addWidget(le1);
  hLayout1->addWidget(button1);

  hLayout2->addWidget(le2);
  hLayout2->addWidget(button2);

  vLayout->addLayout(hLayout1);
  vLayout->addLayout(hLayout2);

  //window.setLayout(vLayout);
  */
  window -> show();
  return app.exec();
}
