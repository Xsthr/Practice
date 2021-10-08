import resources
import gui.py_form.connect
from PyQt5 import QtWidgets
from gui.logics.main_window import MainWindow
from cake_shop import CakeShop


class ConnectWindow(QtWidgets.QDialog, gui.py_form.connect.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Подключение к базе данных')
        self.spin_box_db_number.setMinimum(0)
        self.spin_box_db_number.setMaximum(3)
        self.button_connect.clicked.connect(self.button_connect_action)

    def button_connect_action(self):
        resources.shop = CakeShop(int(self.spin_box_db_number.text()))
        self.ui = MainWindow()
        self.close()
        self.ui.show()