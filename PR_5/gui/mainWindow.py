from gui.forms import mainWindow
from PyQt5 import QtWidgets
import json


class MainWindow(QtWidgets.QDialog, mainWindow.Ui_Dialog):
    def __init__(self, postgre, redis):
        super().__init__()
        self.setupUi(self)
        self.postgre = postgre
        self.redis = redis
        self.plain_postgre.setReadOnly(True)
        self.plain_redis.setReadOnly(True)
        test_dic = {
            'cake_0': {
                'name': 'Plain',
                'quantity': '3',
                'price': '280'
            },
            'cake_1': {
                'name': 'Apple Crumb',
                'purchases': '0',
                'price': '300'
            },
            'cake_2': {
                'name': 'Crumb Cheese',
                'quantity': '3',
                'purchases': '0',
            },
            'cake_3': {
                'name': 'Chocolate',
                'quantity': '3',
                'purchases': '0',
                'price': '310'
            }
        }
        self.plain_buffer.setPlainText(json.dumps(test_dic, indent=4, sort_keys=True))
        self.button_to_postgre.clicked.connect(self.to_postgre_ba)
        self.button_to_redis.clicked.connect(self.to_redis_ba)
        self.button_postgre.clicked.connect(self.postgre_ba)
        self.button_redis.clicked.connect(self.redis_ba)

    def print_postgre(self):
        self.plain_postgre.setPlainText(json.dumps(self.postgre.get_dic(), indent=4, sort_keys=True))

    def print_redis(self):
        self.plain_redis.setPlainText(json.dumps(self.redis.get_dic(), indent=4, sort_keys=True))

    def to_postgre_ba(self):
        self.postgre.add_dic(json.loads(self.plain_buffer.toPlainText()))
        self.print_postgre()

    def to_redis_ba(self):
        self.redis.add_dic(json.loads(self.plain_buffer.toPlainText()))
        self.print_redis()

    def postgre_ba(self):
        self.plain_buffer.setPlainText(json.dumps(self.postgre.get_dic(), indent=4, sort_keys=True))

    def redis_ba(self):
        self.plain_buffer.setPlainText(json.dumps(self.redis.get_dic(), indent=4, sort_keys=True))
