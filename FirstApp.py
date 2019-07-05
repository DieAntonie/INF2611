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
        self.labelFirstNumber = QtGui.QLabel(Dialog)
        self.labelFirstNumber.setGeometry(QtCore.QRect(20, 30, 91, 20))
        self.labelFirstNumber.setObjectName(_fromUtf8("labelFirstNumber"))
        self.labelSecondNumber = QtGui.QLabel(Dialog)
        self.labelSecondNumber.setGeometry(QtCore.QRect(20, 60, 111, 20))
        self.labelSecondNumber.setObjectName(_fromUtf8("labelSecondNumber"))
        self.lineFirstNumber = QtGui.QLineEdit(Dialog)
        self.lineFirstNumber.setGeometry(QtCore.QRect(130, 30, 131, 20))
        self.lineFirstNumber.setText(_fromUtf8(""))
        self.lineFirstNumber.setObjectName(_fromUtf8("lineFirstNumber"))
        self.Add = QtGui.QPushButton(Dialog)
        self.Add.setGeometry(QtCore.QRect(154, 90, 91, 23))
        self.Add.setObjectName(_fromUtf8("Add"))
        self.labelAddition = QtGui.QLabel(Dialog)
        self.labelAddition.setGeometry(QtCore.QRect(276, 40, 111, 21))
        self.labelAddition.setText(_fromUtf8(""))
        self.labelAddition.setObjectName(_fromUtf8("labelAddition"))
        self.lineSecondNumber = QtGui.QLineEdit(Dialog)
        self.lineSecondNumber.setGeometry(QtCore.QRect(130, 60, 131, 20))
        self.lineSecondNumber.setText(_fromUtf8(""))
        self.lineSecondNumber.setObjectName(_fromUtf8("lineSecondNumber"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelFirstNumber.setText(_translate("Dialog", "Enter First Number", None))
        self.labelSecondNumber.setText(_translate("Dialog", "Enter Second Number", None))
        self.Add.setText(_translate("Dialog", "Add", None))

