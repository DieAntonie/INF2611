import sys
from FirstApp import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.Add, QtCore.SIGNAL('clicked()'), self.displaySum)

    def displaySum(self):
        firstNumber = self.convertToInt(self.ui.lineFirstNumber.text())
        secondNumber = self.convertToInt(self.ui.lineSecondNumber.text())
        self.ui.labelAddition.setText("Addition: " + str(firstNumber + secondNumber))

    def convertToInt(self, text):
        return int(text) if len(text) else 0

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myApp = MyForm()
    myApp.show()
    sys.exit(app.exec_())