#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
import os
from PyQt5.QtCore import QUrl, Qt, QTimer, QMetaObject, QObject
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from dataProc import GraphRefresh

if __name__ == '__main__':
    myApp = QGuiApplication(sys.argv)
    appLabel = QQmlApplicationEngine()
    appLabel.addImportPath('.')
    appLabel.addImportPath('./qml')
    appLabel.load('splash.qml')
    root = appLabel.rootObjects()
    g = GraphRefresh("COM9", 115200, 1, root)
    myApp.exec_()
    sys.exit()