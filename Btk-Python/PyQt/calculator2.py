import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from MainWindow import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def hesapla(self):
        sender = self.sender().text() #hangi butona tıklandığının anlaşılması
        result = 0

        if sender == 'Toplama':
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())

        elif sender == 'Cıkarma':
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
            
        elif sender == 'Carpma':
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        
        elif sender == 'Bölme':
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())

        self.lbl_result.setText('Sonuc: ' + str(result))

def app():

    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()


