import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)


from PySide2.QtGui     import QKeySequence
from PySide2.QtCore    import Signal, Slot   
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QLineEdit, QPushButton, QLabel
from PySide2.QtWidgets import QAction, QShortcut      

from applications_skeleton import my_app
from login_back import check_login


def check_succesfull_login(centralWidget):
    username = centralWidget.we_username.text() 
    password = centralWidget.we_password.text()
    if(username == '' or password == ''):
        centralWidget.wl_loginHint.setText('Missing Field !')
        centralWidget.wl_loginHint.show()
        return 1 
    if not(check_login(username, password)):
        centralWidget.wl_loginHint.setText('Wrong Username or Password !')
        centralWidget.wl_loginHint.show()
        return 2
    centralWidget.wl_loginHint.hide()
    exit(0)
    return 0


def build_menu(widget_to_fill, menu_name, actions_list, shortcuts_list):
    if not(len(actions_list) == len(shortcuts_list)):
        return -1
    new_menu = widget_to_fill.addMenu(menu_name)
    widget_actions_list = []
    for i in range(len(actions_list)):
        action = actions_list[i]
        shortcut = shortcuts_list[i]

        widget_actions_list.append(QAction(action))
        widget_actions_list[-1].setShortcut(shortcut)
        new_menu.addAction(widget_actions_list[-1])
    return widget_actions_list


def build_centralwidget(centralWidget):
    centralWidget.layout = QVBoxLayout()

    centralWidget.we_username  = QLineEdit()
    centralWidget.we_password  = QLineEdit()
    centralWidget.wb_login     = QPushButton('Login !')
    centralWidget.wl_loginHint = QLabel('')

    centralWidget.layout.addWidget(centralWidget.we_username )
    centralWidget.layout.addWidget(centralWidget.we_password )
    centralWidget.layout.addWidget(centralWidget.wb_login    )
    centralWidget.layout.addWidget(centralWidget.wl_loginHint)

    centralWidget.setLayout(centralWidget.layout)


def style_centralwidget(centralWidget):
    centralWidget.we_password.setEchoMode(QLineEdit.Password)
    centralWidget.wb_login.setEnabled(False)
    centralWidget.wl_loginHint.setStyleSheet('color: red')
    centralWidget.wl_loginHint.hide()


def connect_centralwidget(centralWidget):
    we_username = centralWidget.we_username
    we_password = centralWidget.we_password
    wb_login = centralWidget.wb_login

    lambda_button_update = lambda val1, arg1=centralWidget: \
        update_button_state(centralWidget=arg1)             

    lambda_check_login = lambda arg1=centralWidget:         \
        check_succesfull_login(centralWidget=arg1)

    we_username.textChanged.connect(lambda_button_update)
    we_password.textChanged.connect(lambda_button_update)

    we_username.returnPressed.connect(lambda_check_login)
    we_password.returnPressed.connect(lambda_check_login)
    wb_login.pressed.connect(lambda_check_login)
    pass


def update_button_state(centralWidget):
    username = centralWidget.we_username.text() 
    password = centralWidget.we_password.text()
    wb_login   = centralWidget.wb_login 
    if(username != '' and password != ''):
        wb_login.setEnabled(True)
    else:
        wb_login.setEnabled(False)
    pass


class ui_masterlogin(my_app):
    '''Menubar functions'''
    def make_menubar(self, topWidget):
        actions   = ['Access Manager']
        shortcuts = ['Ctrl+M']

        topWidget.menu_actions = build_menu(
            topWidget.menubar, 
            'Options', 
            actions, 
            shortcuts
            )
        pass

    '''Central widget functions'''
    def make_centralwidget(self, centralWidget):
        build_centralwidget(centralWidget)
        style_centralwidget(centralWidget)
        connect_centralwidget(self.centralWidget)
        pass

    '''Shortcuts functions'''
    def make_shortcut(self, shortcut_item):
        pass
        '''shortcut_item.login = QShortcut(
            QKeySequence('Ctrl+M'),
            self,
            lambda arg1=ui_item: check_succesfull_login(ui_item=arg1)
            )'''