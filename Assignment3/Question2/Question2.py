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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(360, 186)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.WorkspaceMdi = QtGui.QMdiArea(self.centralwidget)
        self.WorkspaceMdi.setGeometry(QtCore.QRect(0, 0, 361, 161))
        self.WorkspaceMdi.setViewMode(QtGui.QMdiArea.TabbedView)
        self.WorkspaceMdi.setObjectName(_fromUtf8("WorkspaceMdi"))
        self.AddWndw = QtGui.QWidget()
        self.AddWndw.setObjectName(_fromUtf8("AddWndw"))
        self.formLayoutWidget = QtGui.QWidget(self.AddWndw)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 81))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.FormLyt = QtGui.QFormLayout(self.formLayoutWidget)
        self.FormLyt.setObjectName(_fromUtf8("FormLyt"))
        self.SurnameLbl = QtGui.QLabel(self.formLayoutWidget)
        self.SurnameLbl.setObjectName(_fromUtf8("SurnameLbl"))
        self.FormLyt.setWidget(0, QtGui.QFormLayout.LabelRole, self.SurnameLbl)
        self.SurnameEdt = QtGui.QLineEdit(self.formLayoutWidget)
        self.SurnameEdt.setObjectName(_fromUtf8("SurnameEdt"))
        self.FormLyt.setWidget(0, QtGui.QFormLayout.FieldRole, self.SurnameEdt)
        self.NameLbl = QtGui.QLabel(self.formLayoutWidget)
        self.NameLbl.setObjectName(_fromUtf8("NameLbl"))
        self.FormLyt.setWidget(1, QtGui.QFormLayout.LabelRole, self.NameLbl)
        self.NameEdt = QtGui.QLineEdit(self.formLayoutWidget)
        self.NameEdt.setObjectName(_fromUtf8("NameEdt"))
        self.FormLyt.setWidget(1, QtGui.QFormLayout.FieldRole, self.NameEdt)
        self.DobLbl = QtGui.QLabel(self.formLayoutWidget)
        self.DobLbl.setObjectName(_fromUtf8("DobLbl"))
        self.FormLyt.setWidget(2, QtGui.QFormLayout.LabelRole, self.DobLbl)
        self.DobDate = QtGui.QDateEdit(self.formLayoutWidget)
        self.DobDate.setObjectName(_fromUtf8("DobDate"))
        self.FormLyt.setWidget(2, QtGui.QFormLayout.FieldRole, self.DobDate)
        self.AddBtnbx = QtGui.QDialogButtonBox(self.AddWndw)
        self.AddBtnbx.setGeometry(QtCore.QRect(190, 100, 161, 21))
        self.AddBtnbx.setStandardButtons(QtGui.QDialogButtonBox.Discard|QtGui.QDialogButtonBox.Save)
        self.AddBtnbx.setObjectName(_fromUtf8("AddBtnbx"))
        self.EditWndw = QtGui.QWidget()
        self.EditWndw.setObjectName(_fromUtf8("EditWndw"))
        self.ExistingTbl = QtGui.QTableWidget(self.EditWndw)
        self.ExistingTbl.setGeometry(QtCore.QRect(10, 10, 341, 111))
        self.ExistingTbl.setObjectName(_fromUtf8("ExistingTbl"))
        self.ExistingTbl.setColumnCount(4)
        self.ExistingTbl.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.ExistingTbl.setItem(2, 3, item)
        self.ExistingTbl.horizontalHeader().setDefaultSectionSize(84)
        self.ExistingTbl.verticalHeader().setVisible(False)
        self.ExistingTbl.verticalHeader().setDefaultSectionSize(28)
        self.DeleteWndw = QtGui.QWidget()
        self.DeleteWndw.setObjectName(_fromUtf8("DeleteWndw"))
        self.DeleteLst = QtGui.QListWidget(self.DeleteWndw)
        self.DeleteLst.setGeometry(QtCore.QRect(10, 10, 211, 111))
        self.DeleteLst.setObjectName(_fromUtf8("DeleteLst"))
        item = QtGui.QListWidgetItem()
        self.DeleteLst.addItem(item)
        item = QtGui.QListWidgetItem()
        self.DeleteLst.addItem(item)
        item = QtGui.QListWidgetItem()
        self.DeleteLst.addItem(item)
        self.DeleteBtn = QtGui.QPushButton(self.DeleteWndw)
        self.DeleteBtn.setGeometry(QtCore.QRect(230, 90, 121, 31))
        self.DeleteBtn.setObjectName(_fromUtf8("DeleteBtn"))
        self.ConfirmLbl = QtGui.QLabel(self.DeleteWndw)
        self.ConfirmLbl.setGeometry(QtCore.QRect(230, 60, 121, 31))
        self.ConfirmLbl.setObjectName(_fromUtf8("ConfirmLbl"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuData_Maintenance = QtGui.QMenu(self.menubar)
        self.menuData_Maintenance.setObjectName(_fromUtf8("menuData_Maintenance"))
        self.menuReporting = QtGui.QMenu(self.menubar)
        self.menuReporting.setObjectName(_fromUtf8("menuReporting"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.AddActn = QtGui.QAction(MainWindow)
        self.AddActn.setObjectName(_fromUtf8("AddActn"))
        self.EditActn = QtGui.QAction(MainWindow)
        self.EditActn.setObjectName(_fromUtf8("EditActn"))
        self.DeleteActn = QtGui.QAction(MainWindow)
        self.DeleteActn.setObjectName(_fromUtf8("DeleteActn"))
        self.menuData_Maintenance.addAction(self.AddActn)
        self.menuData_Maintenance.addAction(self.EditActn)
        self.menuData_Maintenance.addAction(self.DeleteActn)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuData_Maintenance.menuAction())
        self.menubar.addAction(self.menuReporting.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.SurnameLbl.setBuddy(self.SurnameEdt)
        self.NameLbl.setBuddy(self.NameEdt)
        self.DobLbl.setBuddy(self.DobDate)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.AddWndw.setWindowTitle(_translate("MainWindow", "Subwindow", None))
        self.SurnameLbl.setText(_translate("MainWindow", "Surname", None))
        self.NameLbl.setText(_translate("MainWindow", "First Name(s)", None))
        self.DobLbl.setText(_translate("MainWindow", "Date of Birth", None))
        self.EditWndw.setWindowTitle(_translate("MainWindow", "Subwindow", None))
        item = self.ExistingTbl.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.ExistingTbl.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.ExistingTbl.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3", None))
        item = self.ExistingTbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id", None))
        item = self.ExistingTbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Surname", None))
        item = self.ExistingTbl.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.ExistingTbl.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "DateOfBirth", None))
        __sortingEnabled = self.ExistingTbl.isSortingEnabled()
        self.ExistingTbl.setSortingEnabled(False)
        item = self.ExistingTbl.item(0, 0)
        item.setText(_translate("MainWindow", "10", None))
        item = self.ExistingTbl.item(0, 1)
        item.setText(_translate("MainWindow", "Sneeubal", None))
        item = self.ExistingTbl.item(0, 2)
        item.setText(_translate("MainWindow", "Jaap", None))
        item = self.ExistingTbl.item(0, 3)
        item.setText(_translate("MainWindow", "1993/03/09", None))
        item = self.ExistingTbl.item(1, 0)
        item.setText(_translate("MainWindow", "11", None))
        item = self.ExistingTbl.item(1, 1)
        item.setText(_translate("MainWindow", "Sneeubal", None))
        item = self.ExistingTbl.item(1, 2)
        item.setText(_translate("MainWindow", "Japomina", None))
        item = self.ExistingTbl.item(1, 3)
        item.setText(_translate("MainWindow", "1989/12/27", None))
        item = self.ExistingTbl.item(2, 0)
        item.setText(_translate("MainWindow", "12", None))
        item = self.ExistingTbl.item(2, 1)
        item.setText(_translate("MainWindow", "Sneeubal", None))
        item = self.ExistingTbl.item(2, 2)
        item.setText(_translate("MainWindow", "Japie", None))
        item = self.ExistingTbl.item(2, 3)
        item.setText(_translate("MainWindow", "1994/04/10", None))
        self.ExistingTbl.setSortingEnabled(__sortingEnabled)
        self.DeleteWndw.setWindowTitle(_translate("MainWindow", "Subwindow", None))
        __sortingEnabled = self.DeleteLst.isSortingEnabled()
        self.DeleteLst.setSortingEnabled(False)
        item = self.DeleteLst.item(0)
        item.setText(_translate("MainWindow", "Jaap", None))
        item = self.DeleteLst.item(1)
        item.setText(_translate("MainWindow", "Japomina", None))
        item = self.DeleteLst.item(2)
        item.setText(_translate("MainWindow", "Japie", None))
        self.DeleteLst.setSortingEnabled(__sortingEnabled)
        self.DeleteBtn.setText(_translate("MainWindow", "Delete", None))
        self.ConfirmLbl.setText(_translate("MainWindow", "Confirm Removal?", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuData_Maintenance.setTitle(_translate("MainWindow", "&Data Maintenance", None))
        self.menuReporting.setTitle(_translate("MainWindow", "&Reporting", None))
        self.menuAbout.setTitle(_translate("MainWindow", "&About", None))
        self.AddActn.setText(_translate("MainWindow", "Add new record", None))
        self.EditActn.setText(_translate("MainWindow", "Edit existing record", None))
        self.DeleteActn.setText(_translate("MainWindow", "Delete existing record", None))

