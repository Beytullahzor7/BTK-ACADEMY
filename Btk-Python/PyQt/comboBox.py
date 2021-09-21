from PyQt5 import QtWidgets
import sys
from comboBoxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        combo = self.ui.cbSehirler

        # combo.addItem('Ankara')
        # combo.addItem('Samsun')
        # combo.addItem('Bursa')
        # combo.addItems(['Adana','Kocaeli','Ordu'])

        self.ui.btnLoadItems.clicked.connect(self.LoadItems)
        self.ui.btnGetItem.clicked.connect(self.GetItems)
        self.ui.btnClear.clicked.connect(self.ClearItems)

        self.ui.cbSehirler.currentIndexChanged.connect(self.selectedChangedIndex)
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.selectedChangedText)

    def selectedChangedIndex(self, index):
        print(index)
        print('*****')

    def selectedChangedText(self, text):
        print(text)

    def ClearItems(self):
        self.ui.cbSehirler.clear()

    def GetItems(self):
        print(self.ui.cbSehirler.currentIndex())
        print(self.ui.cbSehirler.currentText())

    def LoadItems(self):
        sehirler = ['Adana','Kocaeli','Ordu']
        self.ui.cbSehirler.addItems(sehirler)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()
