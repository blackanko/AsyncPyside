# -*- coding: utf-8 -*-
import os
from time import sleep

try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from PySide2.QtUiTools import QUiLoader
    from PySide2 import QtCore, QtGui
    from AsyncPyside.ui.asyncPysideWindows2 import Ui_AsyncPysideMainWindow
except ImportError:
    from PySide.QtCore import *
    from PySide.QtGui import *
    from PySide.QtUiTools import QUiLoader
    from PySide import QtCore, QtGui
    from AsyncPyside.ui.asyncPysideWindows import Ui_AsyncPysideMainWindow



class AsyncProc(QObject):

    resultProc = QtCore.Signal()

    def __init__(self, statThread):
        super(AsyncProc, self).__init__()
        self.statThread = statThread

    def doProc(self):
        print "do something"
        for i in range(50):
            print "statThread: %s" % self.statThread.isRunning()
            if not self.statThread.isRunning():
                break
            print i
            sleep(2)
        self.resultProc.emit()

    def doCancel(self):
        self._isCancel = True


class AsyncProcController(QObject):

    operate = QtCore.Signal()
    canceled = QtCore.Signal()

    def __init__(self, data=None, callback=None, cancelCallback=None):
        super(AsyncProcController, self).__init__()
        self._thread = QThread()
        self.statThread = QThread()
        self._asyncProc = AsyncProc(self.statThread)
        self._asyncProc.moveToThread(self._thread)
        self.operate.connect(self._asyncProc.doProc)
        self.canceled.connect(self.cancel)
        self._asyncProc.resultProc.connect(self.handleResults)
        self.statThread.start()
        self._thread.start()

    def cancel(self):
        self._isCancel = True
        print "cancel proc"
        self.statThread.quit()
        self._thread.quit()

    def handleResults(self):
        print "fin"


class AsyncPysideMainWindowUI(QMainWindow, Ui_AsyncPysideMainWindow):

    def __init__(self):
        super(AsyncPysideMainWindowUI, self).__init__()
        self.setupUi(self)

        self._proc = AsyncProcController()

        self.runBT.clicked.connect(self.runProc)
        self.cancelBT.clicked.connect(self.cancelProc)

    def runProc(self):
        print "run botton"
        self._proc.operate.emit()

    def cancelProc(self):
        print "cancel botton"
        self._proc.canceled.emit()
