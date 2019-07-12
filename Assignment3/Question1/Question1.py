# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Question1.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(420, 482)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.WorkspaceMdi = QtGui.QMdiArea(self.centralwidget)
        self.WorkspaceMdi.setGeometry(QtCore.QRect(10, 10, 401, 361))
        self.WorkspaceMdi.setActivationOrder(QtGui.QMdiArea.StackingOrder)
        self.WorkspaceMdi.setViewMode(QtGui.QMdiArea.SubWindowView)
        self.WorkspaceMdi.setDocumentMode(False)
        self.WorkspaceMdi.setObjectName(_fromUtf8("WorkspaceMdi"))
        self.HomeWndw = QtGui.QWidget()
        self.HomeWndw.setObjectName(_fromUtf8("HomeWndw"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.HomeWndw)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 211, 191))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.indexLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.indexLayout_2.setObjectName(_fromUtf8("indexLayout_2"))
        self.postTxt_2 = QtGui.QTextBrowser(self.verticalLayoutWidget_2)
        self.postTxt_2.setObjectName(_fromUtf8("postTxt_2"))
        self.indexLayout_2.addWidget(self.postTxt_2)
        self.attendanceLbl_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.attendanceLbl_2.setObjectName(_fromUtf8("attendanceLbl_2"))
        self.indexLayout_2.addWidget(self.attendanceLbl_2)
        self.attendanceBtnbx_2 = QtGui.QDialogButtonBox(self.verticalLayoutWidget_2)
        self.attendanceBtnbx_2.setStandardButtons(QtGui.QDialogButtonBox.No|QtGui.QDialogButtonBox.Yes)
        self.attendanceBtnbx_2.setObjectName(_fromUtf8("attendanceBtnbx_2"))
        self.indexLayout_2.addWidget(self.attendanceBtnbx_2)
        self.formInputLayout_2 = QtGui.QHBoxLayout()
        self.formInputLayout_2.setObjectName(_fromUtf8("formInputLayout_2"))
        self.petsOwnedLbl_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.petsOwnedLbl_2.setObjectName(_fromUtf8("petsOwnedLbl_2"))
        self.formInputLayout_2.addWidget(self.petsOwnedLbl_2)
        self.petsOwnedSpnbx_2 = QtGui.QSpinBox(self.verticalLayoutWidget_2)
        self.petsOwnedSpnbx_2.setObjectName(_fromUtf8("petsOwnedSpnbx_2"))
        self.formInputLayout_2.addWidget(self.petsOwnedSpnbx_2)
        self.indexLayout_2.addLayout(self.formInputLayout_2)
        self.AboutWndw = QtGui.QWidget()
        self.AboutWndw.setObjectName(_fromUtf8("AboutWndw"))
        self.aboutTxt = QtGui.QTextBrowser(self.AboutWndw)
        self.aboutTxt.setGeometry(QtCore.QRect(0, 0, 211, 191))
        self.aboutTxt.setObjectName(_fromUtf8("aboutTxt"))
        self.ContactWndw = QtGui.QWidget()
        self.ContactWndw.setObjectName(_fromUtf8("ContactWndw"))
        self.addrTxt = QtGui.QTextBrowser(self.ContactWndw)
        self.addrTxt.setGeometry(QtCore.QRect(50, 0, 141, 91))
        self.addrTxt.setObjectName(_fromUtf8("addrTxt"))
        self.emailLbl = QtGui.QLabel(self.ContactWndw)
        self.emailLbl.setGeometry(QtCore.QRect(0, 100, 41, 16))
        self.emailLbl.setObjectName(_fromUtf8("emailLbl"))
        self.addrLbl = QtGui.QLabel(self.ContactWndw)
        self.addrLbl.setGeometry(QtCore.QRect(0, 0, 51, 21))
        self.addrLbl.setObjectName(_fromUtf8("addrLbl"))
        self.cellTxt = QtGui.QLabel(self.ContactWndw)
        self.cellTxt.setGeometry(QtCore.QRect(50, 130, 151, 16))
        self.cellTxt.setObjectName(_fromUtf8("cellTxt"))
        self.cellLbl = QtGui.QLabel(self.ContactWndw)
        self.cellLbl.setGeometry(QtCore.QRect(0, 130, 41, 16))
        self.cellLbl.setObjectName(_fromUtf8("cellLbl"))
        self.emailTxt = QtGui.QLabel(self.ContactWndw)
        self.emailTxt.setGeometry(QtCore.QRect(50, 100, 141, 16))
        self.emailTxt.setObjectName(_fromUtf8("emailTxt"))
        self.ToolbarGpx = QtGui.QGroupBox(self.centralwidget)
        self.ToolbarGpx.setGeometry(QtCore.QRect(10, 380, 401, 61))
        self.ToolbarGpx.setObjectName(_fromUtf8("ToolbarGpx"))
        self.CascadeBtn = QtGui.QPushButton(self.ToolbarGpx)
        self.CascadeBtn.setGeometry(QtCore.QRect(10, 20, 191, 31))
        self.CascadeBtn.setObjectName(_fromUtf8("CascadeBtn"))
        self.TileBtn = QtGui.QPushButton(self.ToolbarGpx)
        self.TileBtn.setGeometry(QtCore.QRect(210, 20, 181, 31))
        self.TileBtn.setObjectName(_fromUtf8("TileBtn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Home = QtGui.QMenu(self.menubar)
        self.menu_Home.setObjectName(_fromUtf8("menu_Home"))
        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName(_fromUtf8("menu_About"))
        self.menu_Contact_Us = QtGui.QMenu(self.menubar)
        self.menu_Contact_Us.setObjectName(_fromUtf8("menu_Contact_Us"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOne = QtGui.QAction(MainWindow)
        self.actionOne.setObjectName(_fromUtf8("actionOne"))
        self.actionTwo = QtGui.QAction(MainWindow)
        self.actionTwo.setObjectName(_fromUtf8("actionTwo"))
        self.actionThree = QtGui.QAction(MainWindow)
        self.actionThree.setObjectName(_fromUtf8("actionThree"))
        self.actionFirst = QtGui.QAction(MainWindow)
        self.actionFirst.setObjectName(_fromUtf8("actionFirst"))
        self.actionSecond = QtGui.QAction(MainWindow)
        self.actionSecond.setObjectName(_fromUtf8("actionSecond"))
        self.actionThird = QtGui.QAction(MainWindow)
        self.actionThird.setObjectName(_fromUtf8("actionThird"))
        self.actionMore = QtGui.QAction(MainWindow)
        self.actionMore.setObjectName(_fromUtf8("actionMore"))
        self.actionPushing = QtGui.QAction(MainWindow)
        self.actionPushing.setObjectName(_fromUtf8("actionPushing"))
        self.actionPlease = QtGui.QAction(MainWindow)
        self.actionPlease.setObjectName(_fromUtf8("actionPlease"))
        self.actionHome = QtGui.QAction(MainWindow)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.openHomeActn = QtGui.QAction(MainWindow)
        self.openHomeActn.setObjectName(_fromUtf8("openHomeActn"))
        self.openAboutActn = QtGui.QAction(MainWindow)
        self.openAboutActn.setObjectName(_fromUtf8("openAboutActn"))
        self.openContactActn = QtGui.QAction(MainWindow)
        self.openContactActn.setObjectName(_fromUtf8("openContactActn"))
        self.menu_Home.addAction(self.openHomeActn)
        self.menu_About.addAction(self.openAboutActn)
        self.menu_Contact_Us.addAction(self.openContactActn)
        self.menubar.addAction(self.menu_Home.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.menubar.addAction(self.menu_Contact_Us.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.HomeWndw.setWindowTitle(_translate("MainWindow", "Subwindow", None))
        self.postTxt_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">1000 km Challenge for 2019/2020</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:10pt; color:#333333; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">Wollies is truly blessed by being nominated as the lucky beneficiary for the 1000 km Challenge for 2019/2020.</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:7pt; color:#333333; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">Thank you so much to each organizer, supporter and athlete who will take part in this special project.</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:7pt; color:#333333; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">To all involved, we invite you to our shelter to share in the love and passion we have for our furry friends.</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:7pt; color:#333333; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">Good luck with the challenge ahead, we here at Wollies, all more than 1000 of us, are supporting you all the way!</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:7pt; color:#333333; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">For more info please check out https://www.1000kmchallenge.co.za/</span></p></body></html>", None))
        self.attendanceLbl_2.setText(_translate("MainWindow", "Will you be attending?", None))
        self.petsOwnedLbl_2.setText(_translate("MainWindow", "How many pets do you own?", None))
        self.AboutWndw.setWindowTitle(_translate("MainWindow", "Subwindow", None))
        self.aboutTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:8pt;\">Wollies comes from humble beginnings.The initial purpose at Wollies was to sterilize as many animals as possible, wayback in 2003 when this all started.</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#333333; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:8pt;\">However, it did not end with this sterilization project. We became more and more involved, helping abandoned, neglected and abused animals and before we knew it, we had evolved in to a full-scale operation which is known today as WOLLIES ANIMAL SHELTER.</span></p></body></html>", None))
        self.ContactWndw.setWindowTitle(_translate("MainWindow", "Subwindow", None))
        self.addrTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Die Rondawel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">101 Rooikat Street</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Pretoria-North </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Gauteng </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">0151 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">South Africa </span></p></body></html>", None))
        self.emailLbl.setText(_translate("MainWindow", "Email:", None))
        self.addrLbl.setText(_translate("MainWindow", "Address:", None))
        self.cellTxt.setText(_translate("MainWindow", "079 916 4602 / 061 605 0002 ", None))
        self.cellLbl.setText(_translate("MainWindow", "Cell:", None))
        self.emailTxt.setText(_translate("MainWindow", "wollies.cillat@gmail.com", None))
        self.ToolbarGpx.setTitle(_translate("MainWindow", "Toolbar", None))
        self.CascadeBtn.setText(_translate("MainWindow", "Cascade", None))
        self.TileBtn.setText(_translate("MainWindow", "Tile", None))
        self.menu_Home.setTitle(_translate("MainWindow", "&Home", None))
        self.menu_About.setTitle(_translate("MainWindow", "&About", None))
        self.menu_Contact_Us.setTitle(_translate("MainWindow", "&Contact Us", None))
        self.actionOne.setText(_translate("MainWindow", "One", None))
        self.actionTwo.setText(_translate("MainWindow", "Two", None))
        self.actionThree.setText(_translate("MainWindow", "Three", None))
        self.actionFirst.setText(_translate("MainWindow", "First", None))
        self.actionSecond.setText(_translate("MainWindow", "Second", None))
        self.actionThird.setText(_translate("MainWindow", "Third", None))
        self.actionMore.setText(_translate("MainWindow", "More", None))
        self.actionPushing.setText(_translate("MainWindow", "Pushing", None))
        self.actionPlease.setText(_translate("MainWindow", "Please", None))
        self.actionHome.setText(_translate("MainWindow", "Home", None))
        self.openHomeActn.setText(_translate("MainWindow", "Open", None))
        self.openAboutActn.setText(_translate("MainWindow", "Open", None))
        self.openContactActn.setText(_translate("MainWindow", "Open", None))

