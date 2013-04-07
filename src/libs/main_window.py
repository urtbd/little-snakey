# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sun Apr  7 22:23:12 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 505)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.serverList = QtGui.QListWidget(self.centralwidget)
        self.serverList.setGeometry(QtCore.QRect(90, 50, 321, 281))
        self.serverList.setObjectName("serverList")
        self.addButton = QtGui.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(120, 330, 91, 32))
        self.addButton.setObjectName("addButton")
        self.delButton = QtGui.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(300, 330, 91, 32))
        self.delButton.setObjectName("delButton")
        self.toggleButton = QtGui.QPushButton(self.centralwidget)
        self.toggleButton.setGeometry(QtCore.QRect(200, 410, 114, 32))
        self.toggleButton.setObjectName("toggleButton")
        self.editButton = QtGui.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(210, 330, 91, 32))
        self.editButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 22))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtGui.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Server = QtGui.QAction(MainWindow)
        self.actionAdd_Server.setObjectName("actionAdd_Server")
        self.actionStart_Monitoring = QtGui.QAction(MainWindow)
        self.actionStart_Monitoring.setObjectName("actionStart_Monitoring")
        self.actionStop_Monitoring = QtGui.QAction(MainWindow)
        self.actionStop_Monitoring.setObjectName("actionStop_Monitoring")
        self.actionQuit = QtGui.QAction(MainWindow)
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
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "UrT PyMonitor", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("MainWindow", "ADD", None, QtGui.QApplication.UnicodeUTF8))
        self.delButton.setText(QtGui.QApplication.translate("MainWindow", "DEL", None, QtGui.QApplication.UnicodeUTF8))
        self.toggleButton.setText(QtGui.QApplication.translate("MainWindow", "START", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("MainWindow", "EDIT", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMain.setTitle(QtGui.QApplication.translate("MainWindow", "Main", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Server.setText(QtGui.QApplication.translate("MainWindow", "Add Server", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart_Monitoring.setText(QtGui.QApplication.translate("MainWindow", "Start Monitoring", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop_Monitoring.setText(QtGui.QApplication.translate("MainWindow", "Stop Monitoring", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

