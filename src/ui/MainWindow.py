# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui-files/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.serverList = QtWidgets.QListWidget(self.centralwidget)
        self.serverList.setGeometry(QtCore.QRect(90, 50, 321, 281))
        self.serverList.setObjectName("serverList")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(120, 330, 91, 32))
        self.addButton.setObjectName("addButton")
        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(300, 330, 91, 32))
        self.delButton.setObjectName("delButton")
        self.toggleButton = QtWidgets.QPushButton(self.centralwidget)
        self.toggleButton.setGeometry(QtCore.QRect(200, 410, 114, 32))
        self.toggleButton.setObjectName("toggleButton")
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(210, 330, 91, 32))
        self.editButton.setObjectName("editButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 22))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Server = QtWidgets.QAction(MainWindow)
        self.actionAdd_Server.setObjectName("actionAdd_Server")
        self.actionStart_Monitoring = QtWidgets.QAction(MainWindow)
        self.actionStart_Monitoring.setObjectName("actionStart_Monitoring")
        self.actionStop_Monitoring = QtWidgets.QAction(MainWindow)
        self.actionStop_Monitoring.setObjectName("actionStop_Monitoring")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuMain.addAction(self.actionAdd_Server)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionStart_Monitoring)
        self.menuMain.addAction(self.actionStop_Monitoring)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UrT PyMonitor"))
        self.addButton.setText(_translate("MainWindow", "ADD"))
        self.delButton.setText(_translate("MainWindow", "DEL"))
        self.toggleButton.setText(_translate("MainWindow", "START"))
        self.editButton.setText(_translate("MainWindow", "EDIT"))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.actionAdd_Server.setText(_translate("MainWindow", "Add Server"))
        self.actionStart_Monitoring.setText(_translate("MainWindow", "Start Monitoring"))
        self.actionStop_Monitoring.setText(_translate("MainWindow", "Stop Monitoring"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

