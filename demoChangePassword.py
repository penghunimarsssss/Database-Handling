# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoChangePassword.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 253)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 121, 16))
        self.label_4.setObjectName("label_4")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(10, 200, 371, 31))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.pushButtonChangePassword = QtWidgets.QPushButton(Dialog)
        self.pushButtonChangePassword.setGeometry(QtCore.QRect(230, 150, 111, 31))
        self.pushButtonChangePassword.setObjectName("pushButtonChangePassword")
        self.lineEditEmailAddress = QtWidgets.QLineEdit(Dialog)
        self.lineEditEmailAddress.setGeometry(QtCore.QRect(150, 20, 231, 20))
        self.lineEditEmailAddress.setObjectName("lineEditEmailAddress")
        self.lineEditOldPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditOldPassword.setGeometry(QtCore.QRect(150, 50, 231, 20))
        self.lineEditOldPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditOldPassword.setObjectName("lineEditOldPassword")
        self.lineEditNewPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditNewPassword.setGeometry(QtCore.QRect(150, 80, 231, 20))
        self.lineEditNewPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditNewPassword.setObjectName("lineEditNewPassword")
        self.lineEditRePassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditRePassword.setGeometry(QtCore.QRect(150, 110, 231, 20))
        self.lineEditRePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditRePassword.setObjectName("lineEditRePassword")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Email Address"))
        self.label_2.setText(_translate("Dialog", "Old Password"))
        self.label_3.setText(_translate("Dialog", "New Password"))
        self.label_4.setText(_translate("Dialog", "Re-enter New Password"))
        self.pushButtonChangePassword.setText(_translate("Dialog", "Change Password"))
