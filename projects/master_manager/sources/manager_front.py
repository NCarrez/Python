import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)


from PySide2.QtGui     import QKeySequence
from PySide2.QtCore    import Signal, Slot   
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout
from PySide2.QtWidgets import QLineEdit, QPushButton, QLabel
from PySide2.QtWidgets import QAction, QShortcut    

from keys import encrypted_ma_key
from applications_skeleton import my_app
from manager_back import get_admin_account_list


def switch_password_print_mode(we_password, wb_button):
    if (we_password.echoMode() == QLineEdit.Password):
        we_password.setEchoMode(QLineEdit.Normal)
        wb_button.setText('Hide')
    else:
        we_password.setEchoMode(QLineEdit.Password)
        wb_button.setText('Reveal')


def delete_user(widget):
    widget.hide()
    pass


def setup_userWidget(username, password):
    widget = QWidget()
    widget.layout = QHBoxLayout()
    widget.layout.setMargin(0)

    widget.username = QLineEdit(username)
    widget.username.setReadOnly(True)
    widget.password = QLineEdit(password)
    widget.password.setReadOnly(True)
    widget.password.setEchoMode(QLineEdit.Password)

    widget.reveal = QPushButton('Reveal')
    widget.reveal.pressed.connect(
        lambda arg1=widget.password,
        arg2=widget.reveal:
        switch_password_print_mode(arg1, arg2)
        )

    widget.delete = QPushButton('Delete')
    widget.delete.pressed.connect(
        lambda arg1=widget:
        delete_user(arg1)
        )

    widget.layout.addWidget(widget.username)
    widget.layout.addWidget(widget.password)
    widget.layout.addWidget(widget.reveal)
    widget.layout.addWidget(widget.delete)

    widget.setLayout(widget.layout)
    widget.setContentsMargins(1, 1, 1, 1)
    return widget
    pass


def build_centralwidget(widget):
    key = encrypted_ma_key
    widget.layout = QVBoxLayout()
    widget.layout.setMargin(10)

    account_list = get_admin_account_list()

    user_widget_list = []
    for account in account_list:
        user_widget_list.append(setup_userWidget(account.get_username(key), account.get_password(key)))

    for user_widget in user_widget_list:
        widget.layout.addWidget(user_widget)

    widget.setLayout(widget.layout)
    widget.setContentsMargins(1, 1, 1, 1)


class ui_mastermanager(my_app):
    '''Menubar functions'''
    def make_menubar(self, topWidget):
        pass

    '''Central widget functions'''
    def make_centralwidget(self, centralWidget):
        build_centralwidget(centralWidget)
        pass

    '''Shortcuts functions'''
    def make_shortcut(self, shortcut_item):
        pass