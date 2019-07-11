# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Assignment1\Assignment1.ui'
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
        Dialog.resize(240, 320)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 221, 301))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.formLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.titleLbl = QtGui.QLabel(self.verticalLayoutWidget)
        self.titleLbl.setTextFormat(QtCore.Qt.AutoText)
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName(_fromUtf8("titleLbl"))
        self.formLayout.addWidget(self.titleLbl)
        self.tabNavigation = QtGui.QTabWidget(self.verticalLayoutWidget)
        self.tabNavigation.setObjectName(_fromUtf8("tabNavigation"))
        self.indexTab = QtGui.QWidget()
        self.indexTab.setObjectName(_fromUtf8("indexTab"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.indexTab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 211, 191))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.indexLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.indexLayout.setObjectName(_fromUtf8("indexLayout"))
        self.postTxt = QtGui.QTextBrowser(self.verticalLayoutWidget_2)
        self.postTxt.setObjectName(_fromUtf8("postTxt"))
        self.indexLayout.addWidget(self.postTxt)
        self.attendanceLbl = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.attendanceLbl.setObjectName(_fromUtf8("attendanceLbl"))
        self.indexLayout.addWidget(self.attendanceLbl)
        self.attendanceBtnbx = QtGui.QDialogButtonBox(self.verticalLayoutWidget_2)
        self.attendanceBtnbx.setStandardButtons(QtGui.QDialogButtonBox.No|QtGui.QDialogButtonBox.Yes)
        self.attendanceBtnbx.setObjectName(_fromUtf8("attendanceBtnbx"))
        self.indexLayout.addWidget(self.attendanceBtnbx)
        self.formInputLayout = QtGui.QHBoxLayout()
        self.formInputLayout.setObjectName(_fromUtf8("formInputLayout"))
        self.petsOwnedLbl = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.petsOwnedLbl.setObjectName(_fromUtf8("petsOwnedLbl"))
        self.formInputLayout.addWidget(self.petsOwnedLbl)
        self.petsOwnedSpnbx = QtGui.QSpinBox(self.verticalLayoutWidget_2)
        self.petsOwnedSpnbx.setObjectName(_fromUtf8("petsOwnedSpnbx"))
        self.formInputLayout.addWidget(self.petsOwnedSpnbx)
        self.indexLayout.addLayout(self.formInputLayout)
        self.tabNavigation.addTab(self.indexTab, _fromUtf8(""))
        self.aboutTab = QtGui.QWidget()
        self.aboutTab.setObjectName(_fromUtf8("aboutTab"))
        self.aboutTxt = QtGui.QTextBrowser(self.aboutTab)
        self.aboutTxt.setGeometry(QtCore.QRect(0, 0, 211, 191))
        self.aboutTxt.setObjectName(_fromUtf8("aboutTxt"))
        self.tabNavigation.addTab(self.aboutTab, _fromUtf8(""))
        self.contactTab = QtGui.QWidget()
        self.contactTab.setObjectName(_fromUtf8("contactTab"))
        self.addrLbl = QtGui.QLabel(self.contactTab)
        self.addrLbl.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.addrLbl.setObjectName(_fromUtf8("addrLbl"))
        self.addrTxt = QtGui.QTextBrowser(self.contactTab)
        self.addrTxt.setGeometry(QtCore.QRect(60, 10, 141, 91))
        self.addrTxt.setObjectName(_fromUtf8("addrTxt"))
        self.emailLbl = QtGui.QLabel(self.contactTab)
        self.emailLbl.setGeometry(QtCore.QRect(10, 110, 41, 16))
        self.emailLbl.setObjectName(_fromUtf8("emailLbl"))
        self.emailTxt = QtGui.QLabel(self.contactTab)
        self.emailTxt.setGeometry(QtCore.QRect(60, 110, 141, 16))
        self.emailTxt.setObjectName(_fromUtf8("emailTxt"))
        self.cellLbl = QtGui.QLabel(self.contactTab)
        self.cellLbl.setGeometry(QtCore.QRect(10, 140, 41, 16))
        self.cellLbl.setObjectName(_fromUtf8("cellLbl"))
        self.cellTxt = QtGui.QLabel(self.contactTab)
        self.cellTxt.setGeometry(QtCore.QRect(60, 140, 151, 16))
        self.cellTxt.setObjectName(_fromUtf8("cellTxt"))
        self.tabNavigation.addTab(self.contactTab, _fromUtf8(""))
        self.formLayout.addWidget(self.tabNavigation)
        self.nameLbl = QtGui.QLabel(self.verticalLayoutWidget)
        self.nameLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameLbl.setObjectName(_fromUtf8("nameLbl"))
        self.formLayout.addWidget(self.nameLbl)
        self.studentNrLbl = QtGui.QLabel(self.verticalLayoutWidget)
        self.studentNrLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.studentNrLbl.setObjectName(_fromUtf8("studentNrLbl"))
        self.formLayout.addWidget(self.studentNrLbl)
        self.urlLbl = QtGui.QLabel(self.verticalLayoutWidget)
        self.urlLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.urlLbl.setObjectName(_fromUtf8("urlLbl"))
        self.formLayout.addWidget(self.urlLbl)

        self.retranslateUi(Dialog)
        self.tabNavigation.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.titleLbl.setText(_translate("Dialog", "Wollies", None))
        self.postTxt.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">1000 km Challenge for 2019/2020</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:10pt; color:#333333; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">Wollies is truly blessed by being nominated as the lucky beneficiary for the 1000 km Challenge for 2019/2020.</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:7pt; color:#333333; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">Thank you so much to each organizer, supporter and athlete who will take part in this special project.</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:7pt; color:#333333; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">To all involved, we invite you to our shelter to share in the love and passion we have for our furry friends.</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:7pt; color:#333333; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">Good luck with the challenge ahead, we here at Wollies, all more than 1000 of us, are supporting you all the way!</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:7pt; color:#333333; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">For more info please check out https://www.1000kmchallenge.co.za/</span></p></body></html>", None))
        self.attendanceLbl.setText(_translate("Dialog", "Will you be attending?", None))
        self.petsOwnedLbl.setText(_translate("Dialog", "How many pets do you own?", None))
        self.tabNavigation.setTabText(self.tabNavigation.indexOf(self.indexTab), _translate("Dialog", "Home", None))
        self.aboutTxt.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:8pt;\">Wollies comes from humble beginnings.The initial purpose at Wollies was to sterilize as many animals as possible, wayback in 2003 when this all started.</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#333333; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:8pt;\">However, it did not end with this sterilization project. We became more and more involved, helping abandoned, neglected and abused animals and before we knew it, we had evolved in to a full-scale operation which is known today as WOLLIES ANIMAL SHELTER.</span></p></body></html>", None))
        self.tabNavigation.setTabText(self.tabNavigation.indexOf(self.aboutTab), _translate("Dialog", "About Us", None))
        self.addrLbl.setText(_translate("Dialog", "Address:", None))
        self.addrTxt.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Die Rondawel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">101 Rooikat Street</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Pretoria-North </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Gauteng </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">0151 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">South Africa </span></p></body></html>", None))
        self.emailLbl.setText(_translate("Dialog", "Email:", None))
        self.emailTxt.setText(_translate("Dialog", "wollies.cillat@gmail.com", None))
        self.cellLbl.setText(_translate("Dialog", "Cell:", None))
        self.cellTxt.setText(_translate("Dialog", "079 916 4602 / 061 605 0002 ", None))
        self.tabNavigation.setTabText(self.tabNavigation.indexOf(self.contactTab), _translate("Dialog", "Contact Us", None))
        self.nameLbl.setText(_translate("Dialog", "Chris Antonie Pieterse", None))
        self.studentNrLbl.setText(_translate("Dialog", "5179-012-2", None))
        self.urlLbl.setText(_translate("Dialog", "http://wollies.org/", None))

