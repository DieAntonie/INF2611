from __future__ import division
import sys
from FirstApp import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.Add, QtCore.SIGNAL('clicked()'), self.calculate)

    def calculate(self):
        quantity = self.convertToInt(self.ui.quantity.text())
        rate = self.convertToInt(self.ui.rate.text())
        discount = self.convertToInt(self.ui.discount.text())
        disp = self.generateOutput(quantity, rate, discount)
        self.ui.result.setText(disp["totalText"] + disp["discountText"] + disp["netText"])

    def convertToInt(self, text):
        return int(text) if len(text) else 0

    def generateOutput(self, quantity, rate, discount):
        totalAmt = quantity * rate
        discountAmt = totalAmt * (discount / 100)
        netAmt = totalAmt - discountAmt
        return {
            "totalText": "Total Amount: R" + str(totalAmt) + "; ",
            "discountText": "Discount: R" + str(discountAmt) + "; ",
            "netText": "Net: R" + str(netAmt) + "; ",
        }

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myApp = MyForm()
    myApp.show()
    sys.exit(app.exec_())