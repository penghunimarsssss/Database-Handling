# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoInsertRow.ui'
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
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 112, 51, 21))
        self.label_4.setObjectName("label_4")
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setGeometry(QtCore.QRect(130, 20, 241, 20))
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.lineEditTableName = QtWidgets.QLineEdit(Dialog)
        self.lineEditTableName.setGeometry(QtCore.QRect(130, 50, 241, 20))
        self.lineEditTableName.setObjectName("lineEditTableName")
        self.lineEditEmailAddress = QtWidgets.QLineEdit(Dialog)
        self.lineEditEmailAddress.setGeometry(QtCore.QRect(130, 80, 241, 20))
        self.lineEditEmailAddress.setObjectName("lineEditEmailAddress")
        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setGeometry(QtCore.QRect(130, 110, 241, 20))
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonInsertRow = QtWidgets.QPushButton(Dialog)
        self.pushButtonInsertRow.setGeometry(QtCore.QRect(190, 170, 75, 23))
        self.pushButtonInsertRow.setObjectName("pushButtonInsertRow")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(20, 240, 351, 31))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Database Name"))
        self.label_2.setText(_translate("Dialog", "Enter Table Name"))
        self.label_3.setText(_translate("Dialog", "Email Address"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.pushButtonInsertRow.setText(_translate("Dialog", "Insert Row"))
