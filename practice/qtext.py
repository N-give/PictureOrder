import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QAction, qApp


class Notepad(QWidget):
    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clrBtn = QPushButton('Clear')
        self.svBtn = QPushButton('Save')
        self.opnBtn = QPushButton('Open')

        self.initUI()

    def initUI(self):
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()

        hLayout.addWidget(self.clrBtn)
        hLayout.addWidget(self.svBtn)
        hLayout.addWidget(self.opnBtn)

        vLayout.addWidget(self.text)
        vLayout.addLayout(hLayout)

        self.clrBtn.clicked.connect(self.clrTxt)
        self.svBtn.clicked.connect(self.saveTxt)
        self.opnBtn.clicked.connect(self.opnTxt)

        self.setLayout(vLayout)
        self.setWindowTitle('PyQt TextEdit')

        self.show()

    def saveTxt(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            text = self.text.toPlainText()
            f.write(text)

    def clrTxt(self):
        self.text.clear()

    def opnTxt(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        with open(filename[0], 'r') as f:
            fileTxt = f.read()
            self.text.setText(fileTxt)

class Writer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.formWidget = Notepad()
        self.setCentralWidget(self.formWidget)
        self.initUI()

    def initUI(self):
        # Create Menu Bar
        bar = self.menuBar()

        # Create Root Menus
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        # Create Actions for menus
        saveAction = QAction('Save As', self)
        saveAction.setShortcut('Ctrl+S')

        openAction = QAction('Open', self)

        newAction = QAction('New', self)
        newAction.setShortcut('Ctrl+N')

        quitAction = QAction('Quit', self)
        quitAction.setShortcut('Ctrl+Q')

        findAction = QAction('Find...', self)
        replaceAction = QAction('Replace...', self)

        # Add actions to menus
        file.addAction(newAction)
        file.addAction(saveAction)
        file.addAction(openAction)
        file.addAction(quitAction)
        findMenu = edit.addMenu('Find')
        findMenu.addAction(findAction)
        findMenu.addAction(replaceAction)

        # Events
        quitAction.triggered.connect(self.quitTrigger)
        file.triggered.connect(self.respond)

        self.setWindowTitle('My Menus')
        self.resize(600, 400)
        
        self.show()

        self.show()

    def quitTrigger(self):
        qApp.quit()

    def respond(self, q):
        signal = q.text()
        if signal == 'New':
            self.formWidget.clrTxt()
        elif signal == '&Open':
            self.formWidget.opnTxt()
        elif signal == '&Save':
            self.formWidget.saveTxt()

app = QApplication(sys.argv)
writer = Writer()
sys.exit(app.exec_())
