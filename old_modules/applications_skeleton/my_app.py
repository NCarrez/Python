import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if not (file_path in sys.path):
    sys.path.append(file_path)


from PySide2.QtGui import QKeySequence
from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QLineEdit, QPushButton, QLabel
from PySide2.QtWidgets import QAction, QShortcut


class my_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_menubar()
        self.setup_centralwidget()
        self.setup_shortcuts()
        self.setup_connections()
        self.setup_closeEvent()

    def closeEvent(self, event, value):
        exit(value)

    def setup_menubar(self):
        self.topWidget = QWidget()  # MenuBar widget
        self.topWidget.menubar = self.menuBar()
        self.make_menubar(self.topWidget)
        self.topWidget.menubar.show()
        pass

    def setup_centralwidget(self):
        self.centralWidget = QWidget()  # Central widget
        self.make_centralwidget(self.centralWidget)
        self.setCentralWidget(self.centralWidget)
        pass

    def setup_shortcuts(self):
        self.shortcuts = QWidget()  # ShortcutsHandler widget
        self.make_shortcut(self.shortcuts)
        pass
