import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

def window():
    
    app = QApplication(sys.argv) #komut bilgisini uygulamaya aktarmmıs olacagız
    win = QMainWindow()

    win.setWindowTitle('First Application')
    win.setGeometry(200,200,500,500) #pencerenin x,y ve yükseklik, genişlik koordinatı ve ölçüsü
    win.setWindowIcon(QIcon('PyQt/icon.png'))
    win.setToolTip('My Tool Tip')
    win.show()
    sys.exit(app.exec_()) #carpı ikonuna tıklandığında uygulama duracaktır

window()