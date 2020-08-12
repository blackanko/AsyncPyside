# -*- coding: <utf-8> -*-

import sys
import os

from PySide import QtGui

CURRENT_PATH = os.path.dirname(os.path.dirname(__file__)).replace("\\", "/")
if not CURRENT_PATH in sys.path:
    sys.path[0:0] = [CURRENT_PATH]

import AsyncPyside.main as asyncMain
reload(asyncMain)

def main():
    app = QtGui.QApplication(sys.argv)
    ui = asyncMain.AsyncPysideMainWindowUI()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
