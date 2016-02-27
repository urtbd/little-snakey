# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui-files/server.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(417, 230)
        self.serverAddress = QtWidgets.QLineEdit(Form)
        self.serverAddress.setGeometry(QtCore.QRect(50, 30, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.serverAddress.setFont(font)
        self.serverAddress.setAlignment(QtCore.Qt.AlignCenter)
        self.serverAddress.setObjectName("serverAddress")
        self.serverName = QtWidgets.QLineEdit(Form)
        self.serverName.setGeometry(QtCore.QRect(50, 90, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.serverName.setFont(font)
        self.serverName.setAlignment(QtCore.Qt.AlignCenter)
        self.serverName.setObjectName("serverName")
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setGeometry(QtCore.QRect(170, 160, 111, 51))
        self.cancelButton.setObjectName("cancelButton")
        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(280, 160, 111, 51))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Server Details"))
        self.serverAddress.setText(_translate("Form", "example.com:27960"))
        self.serverName.setText(_translate("Form", "Server Name"))
        self.cancelButton.setText(_translate("Form", "Cancel"))
        self.okButton.setText(_translate("Form", "OK"))

