import datetime
import resources
import gui.py_form.main_window
import gui.logics.abstract as aui
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal as Signal


class OutputLogger(QObject):
    emit_write = Signal(str, int)

    class Severity:
        DEBUG = 0
        ERROR = 1

    def __init__(self, io_stream, severity):
        super().__init__()

        self.io_stream = io_stream
        self.severity = severity

    def write(self, text):
        self.io_stream.write(text)
        self.emit_write.emit(text, self.severity)

    def flush(self):
        self.io_stream.flush()


OUTPUT_LOGGER_STDOUT = OutputLogger(sys.stdout, OutputLogger.Severity.DEBUG)
OUTPUT_LOGGER_STDERR = OutputLogger(sys.stderr, OutputLogger.Severity.ERROR)

sys.stdout = OUTPUT_LOGGER_STDOUT
sys.stderr = OUTPUT_LOGGER_STDERR


class MainWindow(QtWidgets.QDialog, gui.py_form.main_window.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Магазин')

        OUTPUT_LOGGER_STDOUT.emit_write.connect(self.append_log)
        OUTPUT_LOGGER_STDERR.emit_write.connect(self.append_log)

        self.button_update.clicked.connect(self.update_table_and_resort)
        self.button_exit.clicked.connect(self.button_exit_action)
        self.table_info.cellDoubleClicked.connect(self.buy_item)

        self.labels_table = ['ID  ', 'Название  ', 'Колличество  ', 'Продано  ', 'Цена  ']
        self.sort_flags = [None] * len(self.labels_table)

        self.table_info.horizontalHeader().sectionClicked.connect(self.sort_table)
        self.line_edit_search.textChanged.connect(self.update_table_and_resort)

        aui.set_abstract_table(self.table_info, self.labels_table)

        resources.shop.clear()
        resources.shop.add_dic()

        self.update_table()
        self.sort_table(0)

    def append_log(self, text, severity):
        text = repr(text)

        if severity == OutputLogger.Severity.ERROR:
            self.text_logs.append('<b>{}</b>'.format(text))
        else:
            self.text_logs.append(text)

    def update_table_and_resort(self):
        self.update_table()
        aui.resort_abstract_table(self.table_info, self.sort_flags)

    def update_table(self):
        result = []
        keys = resources.shop.get_keys()
        for key in keys:
            item = [key]
            values = resources.shop.get_value(key)
            for value in values:
                item.append(values[value])
            result.append(item)
        aui.update_abstract_table(self.table_info, result, filter=self.line_edit_search.text())
        self.label_update.setText(str(datetime.datetime.now()))

    def sort_table(self, column):
        self.update_table()
        aui.sort_abstract_table(self.table_info, self.sort_flags, self.labels_table, column)

    def button_exit_action(self):
        self.close()

    def buy_item(self):
        id = self.table_info.item(self.table_info.currentRow(), 0).text()
        name = self.table_info.item(self.table_info.currentRow(), 1).text()
        message = "Вы хотите купить %s(%s)?" % (name, id)
        button_reply = QtWidgets.QMessageBox.question(self, 'Покупка', message,
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if button_reply == QtWidgets.QMessageBox.Yes:
            resources.shop.buy_cake(id)
        self.update_table_and_resort()