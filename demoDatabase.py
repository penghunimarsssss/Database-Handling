# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDatabase.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 241)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 21))
        self.label.setObjectName("label")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(20, 160, 361, 41))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.pushButtonCreateDB = QtWidgets.QPushButton(Dialog)
        self.pushButtonCreateDB.setGeometry(QtCore.QRect(190, 70, 101, 21))
        self.pushButtonCreateDB.setObjectName("pushButtonCreateDB")
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setGeometry(QtCore.QRect(130, 20, 251, 21))
        self.lineEditDBName.setObjectName("lineEditDBName")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Database Name"))
        self.pushButtonCreateDB.setText(_translate("Dialog", "Create Database"))
