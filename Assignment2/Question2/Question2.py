# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Question2.ui'
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

class Ui_Question2(object):
    def setupUi(self, Question2):
        Question2.setObjectName(_fromUtf8("Question2"))
        Question2.resize(341, 281)
        self.CalendarWidget = QtGui.QCalendarWidget(Question2)
        self.CalendarWidget.setGeometry(QtCore.QRect(10, 40, 321, 191))
        self.CalendarWidget.setObjectName(_fromUtf8("CalendarWidget"))
        self.TitleLbl = QtGui.QLabel(Question2)
        self.TitleLbl.setGeometry(QtCore.QRect(10, 10, 321, 16))
        self.TitleLbl.setObjectName(_fromUtf8("TitleLbl"))
        self.CalculateBtn = QtGui.QPushButton(Question2)
        self.CalculateBtn.setGeometry(QtCore.QRect(10, 240, 81, 31))
        self.CalculateBtn.setObjectName(_fromUtf8("CalculateBtn"))
        self.DaysRemainingTxt = QtGui.QLabel(Question2)
        self.DaysRemainingTxt.setGeometry(QtCore.QRect(100, 240, 231, 31))
        self.DaysRemainingTxt.setObjectName(_fromUtf8("DaysRemainingTxt"))

        self.retranslateUi(Question2)
        QtCore.QObject.connect(self.CalendarWidget, QtCore.SIGNAL(_fromUtf8("selectionChanged()")), self.CalculateBtn.toggle)
        QtCore.QMetaObject.connectSlotsByName(Question2)

    def retranslateUi(self, Question2):
        Question2.setWindowTitle(_translate("Question2", "Question2", None))
        self.TitleLbl.setText(_translate("Question2", "Select a date to determine the days remaining in this year:", None))
        self.CalculateBtn.setText(_translate("Question2", "Calculate", None))
        self.DaysRemainingTxt.setText(_translate("Question2", "Days remaining in this year...", None))

