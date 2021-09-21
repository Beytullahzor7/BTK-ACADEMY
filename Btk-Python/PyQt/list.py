import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from listForm import Ui_MainWindow
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
    
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #load Students
        self.loadStudents()

        #Add Students
        self.ui.btnAdd.clicked.connect(self.addStudents)

        #Edit Students
        self.ui.btnEdit.clicked.connect(self.editStudents)

        #Delete Students
        self.ui.btnRemove.clicked.connect(self.removeStudents)

        #Up
        self.ui.btnUp.clicked.connect(self.Up)

        #Down
        self.ui.btnDown.clicked.connect(self.Down)

        #Sort
        self.ui.btnSort.clicked.connect(self.sortStudents)

        #Close
        self.ui.btnExit.clicked.connect(self.close)
        

    def Up(self):
        index = self.ui.listItems.currentRow()
        if index >= 1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1, item)
            self.ui.listItems.setCurrentItem(item)


    def Down(self):
        index = self.ui.listItems.currentRow()
        if index < self.ui.listItems.count() - 1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index+1, item)
            self.ui.listItems.setCurrentItem(item)


    def removeStudents(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)
        if item is None:
            return
        
        question = QMessageBox.question(self, "Remove Student", "Do you want to remove student: " + item.text(), QMessageBox.Yes | QMessageBox.No) #ilk yazı pencere baslıgı, 2. olan alt pencere ekranı
        
        if question == QMessageBox.Yes:
            item = self.ui.listItems.takeItem(index)
            del item
  
    def editStudents(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)

        if item is not None:
            text, ok = QInputDialog.getText(self, "Edit Student", "Student Name", QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)

    def loadStudents(self):
        self.ui.listItems.addItems(['Ahmet','Ali','Cinar'])
        self.ui.listItems.setCurrentRow(0)
         
    def addStudents(self):
        currentIndex = self.ui.listItems.currentRow() #seçili olan row numarasını alıp current indexi onun yerine koyacağız
        text, ok = QInputDialog.getText(self, "New Student", "Student Name")
        if ok and text is not None:
            # self.ui.listItems.insertItem(0, text) #inputDialogdan aldıgımız text yani öğrenci bilgisini 0. indexten sonra eklemiş olalım
            self.ui.listItems.insertItem(currentIndex, text)

    def sortStudents(self):
        self.ui.listItems.sortItems()

    def close(self):
        quit()


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()