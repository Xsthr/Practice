# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_form\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(781, 451)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_update = QtWidgets.QLabel(Dialog)
        self.label_update.setObjectName("label_update")
        self.horizontalLayout.addWidget(self.label_update)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_update = QtWidgets.QPushButton(Dialog)
        self.button_update.setObjectName("button_update")
        self.horizontalLayout.addWidget(self.button_update)
        self.button_exit = QtWidgets.QPushButton(Dialog)
        self.button_exit.setObjectName("button_exit")
        self.horizontalLayout.addWidget(self.button_exit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line_edit_search = QtWidgets.QLineEdit(Dialog)
        self.line_edit_search.setObjectName("line_edit_search")
        self.verticalLayout.addWidget(self.line_edit_search)
        self.table_info = QtWidgets.QTableWidget(Dialog)
        self.table_info.setObjectName("table_info")
        self.table_info.setColumnCount(0)
        self.table_info.setRowCount(0)
        self.verticalLayout.addWidget(self.table_info)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.text_logs = QtWidgets.QTextEdit(Dialog)
        self.text_logs.setObjectName("text_logs")
        self.verticalLayout_2.addWidget(self.text_logs)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Время обновления: "))
        self.label_update.setText(_translate("Dialog", "TIME"))
        self.button_update.setText(_translate("Dialog", "Обновить"))
        self.button_exit.setText(_translate("Dialog", "Выход"))
        self.label_2.setText(_translate("Dialog", "Информация о товарах"))
        self.label_3.setText(_translate("Dialog", "Логи"))
        self.label_4.setText(_translate("Dialog", "Дважды нажмите на товар для покупки"))
