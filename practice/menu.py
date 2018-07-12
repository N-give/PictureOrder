import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp

class MenuDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create Menu Bar
        bar = self.menuBar()

        # Create Root Menus
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        # Create Actions for menus
        saveAction = QAction('Save As', self)
        saveAction.setShortcut('Ctrl+S')

        newAction = QAction('New', self)
        newAction.setShortcut('Ctrl+N')

        quitAction = QAction('Quit', self)
        quitAction.setShortcut('Ctrl+Q')

        findAction = QAction('Find...', self)

        replaceAction = QAction('Replace...', self)

        # Add actions to menus
        file.addAction(newAction)
        file.addAction(saveAction)
        file.addAction(quitAction)
        findMenu = edit.addMenu('Find')
        findMenu.addAction(findAction)
        findMenu.addAction(replaceAction)

        # Events
        quitAction.triggered.connect(self.quitTrigger)
        file.triggered.connect(self.selected)

        self.setWindowTitle('My Menus')
        self.resize(600, 400)
        
        self.show()

    def quitTrigger(self):
        qApp.quit()

    def selected(self, q):
        print(q.text() + ' selected')

app = QApplication(sys.argv)
menus = MenuDemo()
sys.exit(app.exec_())
