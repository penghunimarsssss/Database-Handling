# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCreateTable.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(190, 100, 61, 16))
        self.label_4.setObjectName("label_4")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(20, 250, 361, 31))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setGeometry(QtCore.QRect(130, 20, 241, 20))
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.lineEditTableName = QtWidgets.QLineEdit(Dialog)
        self.lineEditTableName.setGeometry(QtCore.QRect(130, 60, 241, 20))
        self.lineEditTableName.setObjectName("lineEditTableName")
        self.lineEditColumnName = QtWidgets.QLineEdit(Dialog)
        self.lineEditColumnName.setGeometry(QtCore.QRect(10, 130, 141, 20))
        self.lineEditColumnName.setObjectName("lineEditColumnName")
        self.comboBoxDataType = QtWidgets.QComboBox(Dialog)
        self.comboBoxDataType.setGeometry(QtCore.QRect(180, 130, 81, 22))
        self.comboBoxDataType.setObjectName("comboBoxDataType")
        self.comboBoxDataType.addItem("")
        self.comboBoxDataType.addItem("")
        self.pushButtonAddColumn = QtWidgets.QPushButton(Dialog)
        self.pushButtonAddColumn.setGeometry(QtCore.QRect(300, 130, 81, 23))
        self.pushButtonAddColumn.setObjectName("pushButtonAddColumn")
        self.pushButtonCreateTable = QtWidgets.QPushButton(Dialog)
        self.pushButtonCreateTable.setGeometry(QtCore.QRect(140, 190, 91, 23))
        self.pushButtonCreateTable.setObjectName("pushButtonCreateTable")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Database Name"))
        self.label_2.setText(_translate("Dialog", "Enter Table Name"))
        self.label_3.setText(_translate("Dialog", "Column Name"))
        self.label_4.setText(_translate("Dialog", "Data Type"))
        self.comboBoxDataType.setItemText(0, _translate("Dialog", "integer"))
        self.comboBoxDataType.setItemText(1, _translate("Dialog", "text"))
        self.pushButtonAddColumn.setText(_translate("Dialog", "Add Column"))
        self.pushButtonCreateTable.setText(_translate("Dialog", "Create Table"))
