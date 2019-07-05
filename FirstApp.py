# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\FirstApp.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 121)
        self.labelEnterName = QtGui.QLabel(Dialog)
        self.labelEnterName.setGeometry(QtCore.QRect(20, 30, 81, 20))
        self.labelEnterName.setObjectName(_fromUtf8("labelEnterName"))
        self.labelMessage = QtGui.QLabel(Dialog)
        self.labelMessage.setGeometry(QtCore.QRect(20, 60, 361, 20))
        self.labelMessage.setText(_fromUtf8(""))
        self.labelMessage.setObjectName(_fromUtf8("labelMessage"))
        self.lineUserName = QtGui.QLineEdit(Dialog)
        self.lineUserName.setGeometry(QtCore.QRect(110, 30, 271, 20))
        self.lineUserName.setText(_fromUtf8(""))
        self.lineUserName.setObjectName(_fromUtf8("lineUserName"))
        self.ClickMeButton = QtGui.QPushButton(Dialog)
        self.ClickMeButton.setGeometry(QtCore.QRect(154, 90, 91, 23))
        self.ClickMeButton.setObjectName(_fromUtf8("ClickMeButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelEnterName.setText(_translate("Dialog", "Enter your name", None))
        self.ClickMeButton.setText(_translate("Dialog", "Click Me", None))

