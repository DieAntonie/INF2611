import sys
from Question2 import *

SCALE_CONST = 0.95
DAY_IMAGE = "day.jpg"
NIGHT_IMAGE = "night.jpg"

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Question2()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.CalculateBtn, QtCore.SIGNAL('clicked()'), self.displayDaysRemaining)

    def displayDaysRemaining(self):
        dateSeleted = self.ui.CalendarWidget.selectedDate()
        currentDate = QtCore.QDate.currentDate()
        endOfThisYear = QtCore.QDate(currentDate.year(), 12, 31)
        days_remaining = dateSeleted.daysTo(endOfThisYear)
        self.ui.DaysRemainingTxt.setText("{0} Days remaining in this year".format(str(days_remaining)) )

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myApp = MyForm()
    myApp.show()
    sys.exit(app.exec_())