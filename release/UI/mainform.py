# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class mainForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(758, 317)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QTableWidget(Form)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayout.addWidget(self.table)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 0, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Инфа о кофе"))
        self.addButton.setText(_translate("Form", "Добавить инфу"))
        self.saveButton.setText(_translate("Form", "Сохранить"))
