import sys
from FirstApp import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.ClickMeButton, QtCore.SIGNAL('clicked()'), self.displayMessage)

    def displayMessage(self):
        self.ui.labelMessage.setText("Hello " + self.ui.lineUserName.text())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myApp = MyForm()
    myApp.show()
    sys.exit(app.exec_())