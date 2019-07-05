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
        Dialog.resize(391, 142)
        self.labelFirstNumber = QtGui.QLabel(Dialog)
        self.labelFirstNumber.setGeometry(QtCore.QRect(20, 10, 91, 20))
        self.labelFirstNumber.setObjectName(_fromUtf8("labelFirstNumber"))
        self.quantity = QtGui.QLineEdit(Dialog)
        self.quantity.setGeometry(QtCore.QRect(110, 10, 41, 20))
        self.quantity.setText(_fromUtf8(""))
        self.quantity.setObjectName(_fromUtf8("quantity"))
        self.labelSecondNumber = QtGui.QLabel(Dialog)
        self.labelSecondNumber.setGeometry(QtCore.QRect(180, 10, 71, 20))
        self.labelSecondNumber.setObjectName(_fromUtf8("labelSecondNumber"))
        self.rate = QtGui.QLineEdit(Dialog)
        self.rate.setGeometry(QtCore.QRect(260, 10, 121, 20))
        self.rate.setText(_fromUtf8(""))
        self.rate.setObjectName(_fromUtf8("rate"))
        self.labelAddition = QtGui.QLabel(Dialog)
        self.labelAddition.setGeometry(QtCore.QRect(20, 50, 111, 21))
        self.labelAddition.setObjectName(_fromUtf8("labelAddition"))
        self.discount = QtGui.QLineEdit(Dialog)
        self.discount.setGeometry(QtCore.QRect(130, 50, 41, 20))
        self.discount.setText(_fromUtf8(""))
        self.discount.setObjectName(_fromUtf8("discount"))
        self.result = QtGui.QLabel(Dialog)
        self.result.setGeometry(QtCore.QRect(0, 110, 391, 20))
        self.result.setText(_fromUtf8(""))
        self.result.setObjectName(_fromUtf8("result"))
        self.Add = QtGui.QPushButton(Dialog)
        self.Add.setGeometry(QtCore.QRect(160, 80, 101, 23))
        self.Add.setObjectName(_fromUtf8("Add"))
        self.labelFirstNumber.setBuddy(self.quantity)
        self.labelSecondNumber.setBuddy(self.rate)
        self.labelAddition.setBuddy(self.discount)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.quantity, self.discount)
        Dialog.setTabOrder(self.discount, self.rate)
        Dialog.setTabOrder(self.rate, self.Add)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelFirstNumber.setText(_translate("Dialog", "&Number of items", None))
        self.labelSecondNumber.setText(_translate("Dialog", "&Price per item", None))
        self.labelAddition.setText(_translate("Dialog", "&Discount Percentage", None))
        self.Add.setText(_translate("Dialog", "Calculate Amount", None))

