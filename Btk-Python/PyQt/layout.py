import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(300,300,500,500)

        layout = QtWidgets.QVBoxLayout()
        hlayout1 = QtWidgets.QHBoxLayout()
        hlayout1.addWidget(Color('yellow'))  
        hlayout1.addWidget(Color('red'))  
        hlayout1.addWidget(Color('black'))  
        # hlayout1.setContentsMargins(50,0,0,0) #boşluk bırakma
        hlayout1.setSpacing(50) #herbir eleman arasında 50 piksellik boşluk oluşturur

        hlayout2 = QtWidgets.QHBoxLayout()
        hlayout2.addWidget(Color('red'))  
        hlayout2.addWidget(Color('yellow'))  

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        # layout = QtWidgets.QGridLayout()
        # layout.addWidget(Color('green'),0,0)
        # layout.addWidget(Color('yellow'),1,0)
        # layout.addWidget(Color('black'),1,1)
        # layout.addWidget(Color('red'),0,2)
        # layout.addWidget(Color('orange'),2,2)

        widget = QWidget()  
        widget.setLayout(vlayout)

        self.setCentralWidget(widget)

def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()



