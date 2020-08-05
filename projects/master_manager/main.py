import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)


from PySide2.QtWidgets import QApplication
from sources.manager_front import ui_mastermanager


if __name__ == "__main__":
    app = QApplication([])
    window = ui_mastermanager()
    window.show()
    sys.exit(app.exec_())
