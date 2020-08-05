import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)


from PySide2.QtWidgets import QApplication
from sources.login_front import ui_masterlogin


if __name__ == "__main__":
    app = QApplication([])
    window = ui_masterlogin()
    window.show()
    sys.exit(app.exec_())