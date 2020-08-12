# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/lupeng/Desktop/dev/AsyncPyside/ui/asyncPysideWindows.ui',
# licensing of 'C:/Users/lupeng/Desktop/dev/AsyncPyside/ui/asyncPysideWindows.ui' applies.
#
# Created: Wed Aug 12 16:11:37 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_AsyncPysideMainWindow(object):
    def setupUi(self, AsyncPysideMainWindow):
        AsyncPysideMainWindow.setObjectName("AsyncPysideMainWindow")
        AsyncPysideMainWindow.resize(300, 203)
        self.centralwidget = QtWidgets.QWidget(AsyncPysideMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.runBT = QtWidgets.QPushButton(self.centralwidget)
        self.runBT.setObjectName("runBT")
        self.verticalLayout.addWidget(self.runBT)
        self.cancelBT = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBT.setObjectName("cancelBT")
        self.verticalLayout.addWidget(self.cancelBT)
        self.runProgressBarBT = QtWidgets.QPushButton(self.centralwidget)
        self.runProgressBarBT.setObjectName("runProgressBarBT")
        self.verticalLayout.addWidget(self.runProgressBarBT)
        AsyncPysideMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AsyncPysideMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        AsyncPysideMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AsyncPysideMainWindow)
        self.statusbar.setObjectName("statusbar")
        AsyncPysideMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AsyncPysideMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AsyncPysideMainWindow)

    def retranslateUi(self, AsyncPysideMainWindow):
        AsyncPysideMainWindow.setWindowTitle(QtWidgets.QApplication.translate("AsyncPysideMainWindow", "AsyncPysideWindow", None, -1))
        self.runBT.setText(QtWidgets.QApplication.translate("AsyncPysideMainWindow", "Run", None, -1))
        self.cancelBT.setText(QtWidgets.QApplication.translate("AsyncPysideMainWindow", "Cancel", None, -1))
        self.runProgressBarBT.setText(QtWidgets.QApplication.translate("AsyncPysideMainWindow", "RunProgressBar", None, -1))

