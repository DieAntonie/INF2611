from __future__ import division
import sys
from Assignment1Form import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myApp = MyForm()
    myApp.show()
    sys.exit(app.exec_())