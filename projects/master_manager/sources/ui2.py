import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if not (file_path in sys.path):
    sys.path.append(file_path)


from PySide2.QtGui import QKeySequence
from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import QApplication, QMainWindow, QGroupBox, QWidget
from PySide2.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PySide2.QtWidgets import QLineEdit, QPushButton, QLabel
from PySide2.QtWidgets import QAction, QShortcut
from PySide2.QtWidgets import QListWidget, QListWidgetItem
from PySide2.QtWidgets import QFrame, QStyle

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
    users = [
        ["admin", "admin"],
        ["admin1", "admin1"],
        ["admin2", "admin2"],
        ["admin3", "admin3"],
        ["admin4", "admin4"],
        ["admin5", "admin5"],
    ]

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


def build_adminpanelwidget():
    widget = QFrame()
    widget.setFrameStyle(QFrame.Panel | QFrame.Raised)
    # widget = QWidget()
    # widget.setStyleSheet(
    #    "background-color: rgb(255,0,0); margin:5px; border:1px solid rgb(0, 255, 0); "
    # )
    # widget.setStyle(QStyle.PE_FrameWindow)
    widget.layout = QVBoxLayout()
    widget.we_username = QLineEdit("username")
    widget.wl_username = QLabel("username")
    widget.wl_username.setBuddy(widget.we_username)
    widget.we_username.setReadOnly(True)

    widget.pas_layout = QHBoxLayout()
    widget.we_password = QLineEdit("password")
    widget.wl_password = QLabel("password")
    widget.wl_password.setBuddy(widget.we_password)
    widget.we_password.setReadOnly(True)
    widget.we_password.setEchoMode(QLineEdit.Password)
    widget.reveal = QPushButton("Reveal")

    widget.btn_layout = QHBoxLayout()
    widget.update = QPushButton("Update")
    widget.delete = QPushButton("Delete")

    widget.layout.addWidget(widget.wl_username)
    widget.layout.addWidget(widget.we_username)
    widget.layout.addWidget(widget.wl_password)
    widget.layout.insertLayout(-1, widget.pas_layout)
    widget.pas_layout.addWidget(widget.we_password)
    widget.pas_layout.addWidget(widget.reveal)
    widget.layout.addStretch()
    widget.layout.insertLayout(-1, widget.btn_layout)
    widget.btn_layout.addWidget(widget.update)
    widget.btn_layout.addWidget(widget.delete)
    widget.setLayout(widget.layout)
    return widget
    pass


def build_adminaddwidget():
    widget = QWidget()
    widget.layout = QVBoxLayout()
    widget.add = QPushButton("Add")

    widget.layout.addWidget(widget.add)
    widget.setLayout(widget.layout)
    return widget
    pass


def build_centralwidget(widget):
    widget.mlayout = QHBoxLayout()
    widget.gbox = QGroupBox("Admin Manager")
    widget.mlayout.addWidget(widget.gbox)
    widget.layout = QHBoxLayout()

    widget.lst_layout = QVBoxLayout()
    widget.layout.admin_list_widget = build_adminlistwidget()
    widget.lst_layout.addWidget(widget.layout.admin_list_widget)
    widget.layout.admin_add_widget = build_adminaddwidget()
    widget.lst_layout.addWidget(widget.layout.admin_add_widget)
    widget.layout.insertLayout(-1, widget.lst_layout)

    widget.layout.insertSpacing(-1, 5)

    widget.layout.admin_panel_widget = build_adminpanelwidget()
    widget.layout.addWidget(widget.layout.admin_panel_widget)
    widget.gbox.setLayout(widget.layout)
    widget.setLayout(widget.mlayout)
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

