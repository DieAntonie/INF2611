import sys
from Question2 import *

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.AddWndw = self.setupSubWindow(self.ui.AddWndw, "Add New Record")
        self.EditWndw = self.setupSubWindow(self.ui.EditWndw, "Edit Existing Record")
        self.DeleteWndw = self.setupSubWindow(self.ui.DeleteWndw, "Delete Existing Record")
        QtCore.QObject.connect(self.ui.AddActn, QtCore.SIGNAL('triggered()'), self.openAddWindow)
        QtCore.QObject.connect(self.ui.EditActn, QtCore.SIGNAL('triggered()'), self.openEditWindow)
        QtCore.QObject.connect(self.ui.DeleteActn, QtCore.SIGNAL('triggered()'), self.openDeleteWindow)

    def setupSubWindow(self, widget, title):
        subWindow = self.ui.WorkspaceMdi.addSubWindow(widget)
        subWindow.setWindowTitle(title)
        return subWindow

    def openAddWindow(self):
        self.ui.WorkspaceMdi.setActiveSubWindow(self.AddWndw)

    def openEditWindow(self):
        self.ui.WorkspaceMdi.setActiveSubWindow(self.EditWndw)

    def openDeleteWindow(self):
        self.ui.WorkspaceMdi.setActiveSubWindow(self.DeleteWndw)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myApp = MyForm()
    myApp.show()
    sys.exit(app.exec_())