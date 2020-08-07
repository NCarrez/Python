import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if not (file_path in sys.path):
    sys.path.append(file_path)


from PySide2.QtGui import QKeySequence
from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtWidgets import QGridLayout, QVBoxLayout
from PySide2.QtWidgets import QLineEdit, QPushButton, QLabel
from PySide2.QtWidgets import QAction, QShortcut
from PySide2.QtWidgets import QListWidget, QListWidgetItem

from applications_skeleton import my_app


def make_adminlist_item(username):
    widget = QWidget()
    widget.layout = QVBoxLayout()

    widget.label = QLabel()
    widget.label.setText(username)
    widget.layout.addWidget(widget.label)
    widget.setLayout(widget.layout)
    return widget


def build_adminlistwidget():
    list_widget = QListWidget()
    list_widget.items = []
    users = [["admin", "admin"], ["admin1", "admin1"]]

    for username, password in users:
        item = make_adminlist_item(username)
        list_widget.items.append(item)
        last_item_indice = len(list_widget.items) - 1
        list_widget_item = QListWidgetItem(list_widget)
        list_widget_item.setSizeHint(list_widget.items[last_item_indice].sizeHint())
        list_widget.addItem(list_widget_item)
        list_widget.setItemWidget(list_widget_item, list_widget.items[last_item_indice])
    return list_widget
    pass


def build_centralwidget(widget):
    widget.layout = QGridLayout()

    widget.layout.admin_list_widget = build_adminlistwidget()
    widget.layout.addWidget(widget.layout.admin_list_widget)
    widget.setLayout(widget.layout)
    pass


class ui_mastermanager(my_app):
    """Menubar functions"""

    def make_menubar(self, topWidget):
        pass

    """Central widget functions"""

    def make_centralwidget(self, centralWidget):
        build_centralwidget(centralWidget)
        pass

    """Shortcuts functions"""

    def make_shortcut(self, shortcut_item):
        pass

