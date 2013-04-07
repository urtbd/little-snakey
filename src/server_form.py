# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created: Sun Apr  7 23:24:34 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(417, 230)
        self.serverAddress = QtGui.QLineEdit(Form)
        self.serverAddress.setGeometry(QtCore.QRect(50, 30, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.serverAddress.setFont(font)
        self.serverAddress.setAlignment(QtCore.Qt.AlignCenter)
        self.serverAddress.setObjectName("serverAddress")
        self.serverName = QtGui.QLineEdit(Form)
        self.serverName.setGeometry(QtCore.QRect(50, 90, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.serverName.setFont(font)
        self.serverName.setAlignment(QtCore.Qt.AlignCenter)
        self.serverName.setObjectName("serverName")
        self.cancelButton = QtGui.QPushButton(Form)
        self.cancelButton.setGeometry(QtCore.QRect(170, 160, 111, 51))
        self.cancelButton.setObjectName("cancelButton")
        self.okButton = QtGui.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(280, 160, 111, 51))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Server Details", None, QtGui.QApplication.UnicodeUTF8))
        self.serverAddress.setText(QtGui.QApplication.translate("Form", "example.com:27960", None, QtGui.QApplication.UnicodeUTF8))
        self.serverName.setText(QtGui.QApplication.translate("Form", "Server Name", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Form", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("Form", "OK", None, QtGui.QApplication.UnicodeUTF8))

