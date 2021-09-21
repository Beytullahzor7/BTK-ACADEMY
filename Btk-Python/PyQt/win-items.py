import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle('First Application')
        self.setGeometry(200,200,500,500) #pencerenin x,y ve yükseklik, genişlik koordinatı ve ölçüsü
        self.setWindowIcon(QIcon('PyQt/icon.png'))
        self.setToolTip('My Tool Tip')
        self.initUI()
    
    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText('Adınız: ')
        self.lbl_name.move(50,30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText('Soyadınız: ')
        self.lbl_surname.move(50,70)

        self.txt_name = QtWidgets.QLineEdit(self) #textbox
        self.txt_name.move(150,30)
        self.txt_name.resize(200,32)

        self.txt_surname = QtWidgets.QLineEdit(self) #textbox
        self.txt_surname.move(150,70)
        self.txt_surname.resize(200,32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Kaydet")
        self.btn_save.move(150,110)
        self.btn_save.clicked.connect(self.clicked)
        self.btn_save.resize(200,32)

    def clicked(self):
        print('Butona Tıklandı\n' +'Name:' + self.txt_name.text()+'\n'+'Surname ' + self.txt_surname.text())


def window():

    app = QApplication(sys.argv) #komut bilgisini uygulamaya aktarmmıs olacagız
    win = MyWindow()
    win.show()
    sys.exit(app.exec_()) #carpı ikonuna tıklandığında uygulama duracaktır

window()

#widgets = {QLabel,QCombox,QCheckBox,QRadioButton,QPushButton,QTableWidget,QLineEdit,QSlideBar,QProgressBar} 