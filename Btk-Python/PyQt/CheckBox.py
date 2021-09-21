import sys
from PyQt5 import QtWidgets
from CheckBoxForm3 import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #checkBoxlara Ulaşalım ve onlar üzerinden işlem yapalım
        self.ui.cbSinema.stateChanged.connect(self.show_state)
        self.ui.cbKitap.stateChanged.connect(self.show_state)
        self.ui.cbSpor.stateChanged.connect(self.show_state)

        self.ui.btnHobilerSecilenleriAl.clicked.connect(self.getAllHobiler)
        self.ui.btnDerslerSecilenleriAl.clicked.connect(self.getAllDersler)
    
    def getAllHobiler(self):
        result = ''
        items = self.ui.groupHobiler.findChildren(QtWidgets.QCheckBox) #widget altında yer alan elemanları verir
        
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'

        self.ui.lblResultHobiler.setText(result)
    
    def getAllDersler(self):
        result = ''
        items = self.ui.groupDersler.findChildren(QtWidgets.QCheckBox) #widget altında yer alan elemanları verir
        
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'

        self.ui.lblResultDersler.setText(result)
               


    def show_state(self, value):
        cb = self.sender()
        print(cb.isChecked())

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

app()
