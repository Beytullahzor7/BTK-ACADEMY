import sys
from PyQt5 import QtWidgets
from dateForm import Ui_MainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalculate.clicked.connect(self.calculate)

    def calculate(self):
        start = self.ui.dateStart.date()
        end = self.ui.dateEnd.date()
        print(start, end)

        print('Days in Month: {0}'.format(start.daysInMonth()))
        print('Days in Year: {0}'.format(start.daysInYear()))

        print('Total days: {}'.format(start.daysTo(end)))
        
        now = QDate.currentDate()

        print('Total days from now: {}'.format(start.daysTo(now)))


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()