# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/lupeng/Desktop/dev/AsyncPyside/ui/asyncPysideWindows.ui'
#
# Created: Wed Aug 12 16:11:06 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AsyncPysideMainWindow(object):
    def setupUi(self, AsyncPysideMainWindow):
        AsyncPysideMainWindow.setObjectName("AsyncPysideMainWindow")
        AsyncPysideMainWindow.resize(300, 203)
        self.centralwidget = QtGui.QWidget(AsyncPysideMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.runBT = QtGui.QPushButton(self.centralwidget)
        self.runBT.setObjectName("runBT")
        self.verticalLayout.addWidget(self.runBT)
        self.cancelBT = QtGui.QPushButton(self.centralwidget)
        self.cancelBT.setObjectName("cancelBT")
        self.verticalLayout.addWidget(self.cancelBT)
        self.runProgressBarBT = QtGui.QPushButton(self.centralwidget)
        self.runProgressBarBT.setObjectName("runProgressBarBT")
        self.verticalLayout.addWidget(self.runProgressBarBT)
        AsyncPysideMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(AsyncPysideMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        AsyncPysideMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(AsyncPysideMainWindow)
        self.statusbar.setObjectName("statusbar")
        AsyncPysideMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AsyncPysideMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AsyncPysideMainWindow)

    def retranslateUi(self, AsyncPysideMainWindow):
        AsyncPysideMainWindow.setWindowTitle(QtGui.QApplication.translate("AsyncPysideMainWindow", "AsyncPysideWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.runBT.setText(QtGui.QApplication.translate("AsyncPysideMainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBT.setText(QtGui.QApplication.translate("AsyncPysideMainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.runProgressBarBT.setText(QtGui.QApplication.translate("AsyncPysideMainWindow", "RunProgressBar", None, QtGui.QApplication.UnicodeUTF8))

