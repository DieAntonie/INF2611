import sys
from Question1 import *

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.WorkspaceMdi.addSubWindow(self.ui.HomeWndw)
        self.ui.WorkspaceMdi.addSubWindow(self.ui.ContactWndw)
        QtCore.QObject.connect(self.ui.openHomeActn, QtCore.SIGNAL('triggered()'), self.openHomeWindow)
        QtCore.QObject.connect(self.ui.openAboutActn, QtCore.SIGNAL('triggered()'), self.openAboutWindow)
        QtCore.QObject.connect(self.ui.openContactActn, QtCore.SIGNAL('triggered()'), self.openContactUsWindow)
        QtCore.QObject.connect(self.ui.CascadeBtn, QtCore.SIGNAL('clicked()'), self.cascadeArrange)
        QtCore.QObject.connect(self.ui.TileBtn, QtCore.SIGNAL('clicked()'), self.tileArrange)

    def openHomeWindow(self):
        self.ui.WorkspaceMdi.addSubWindow(self.ui.HomeWndw)

    def openAboutWindow(self):
        self.ui.WorkspaceMdi.addSubWindow(self.ui.AboutWndw)

    def openContactUsWindow(self):
        self.ui.WorkspaceMdi.addSubWindow(self.ui.ContactWndw)

    def cascadeArrange(self):
        self.ui.WorkspaceMdi.cascadeSubWindows()

    def tileArrange(self):
        self.ui.WorkspaceMdi.tileSubWindows()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myApp = MyForm()
    myApp.show()
    sys.exit(app.exec_())