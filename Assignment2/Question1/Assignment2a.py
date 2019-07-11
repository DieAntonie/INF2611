# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Assignment2a.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Question1(object):
    def setupUi(self, Question1):
        Question1.setObjectName(_fromUtf8("Question1"))
        Question1.resize(240, 320)
        self.sysClockLcd = QtGui.QLCDNumber(Question1)
        self.sysClockLcd.setGeometry(QtCore.QRect(10, 40, 221, 91))
        self.sysClockLcd.setObjectName(_fromUtf8("sysClockLcd"))
        self.sysClockLbl = QtGui.QLabel(Question1)
        self.sysClockLbl.setGeometry(QtCore.QRect(10, 10, 221, 21))
        self.sysClockLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.sysClockLbl.setObjectName(_fromUtf8("sysClockLbl"))
        self.currentTimeVisualization = QtGui.QGraphicsView(Question1)
        self.currentTimeVisualization.setGeometry(QtCore.QRect(10, 140, 221, 171))
        self.currentTimeVisualization.setObjectName(_fromUtf8("currentTimeVisualization"))

        self.retranslateUi(Question1)
        QtCore.QMetaObject.connectSlotsByName(Question1)

    def retranslateUi(self, Question1):
        Question1.setWindowTitle(_translate("Question1", "Question 1", None))
        self.sysClockLbl.setText(_translate("Question1", "THE TIME IS:", None))

