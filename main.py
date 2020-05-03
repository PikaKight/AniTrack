from PyQt5 import QtCore, QtGui, QtWidgets
from back import *
import main_menu,register,menu_2, json

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.main_menu = main_menu.Ui_MainWindow()
        self.register = register.Ui_MainWindow()
        self.menu_2 = menu_2.Ui_MainWindow()
        self.startmain_menu()
    
    def startmain_menu(self):
        self.main_menu.setupUi(self)
        self.main_menu.register_2.clicked.connect(self.startregister)
        self.main_menu.login.clicked.connect(self.startmenu_2)
        self.show()
        
        
    def startregister(self):
        self.register.setupUi(self)
        self.register.pushButton.clicked.connect(self.startmain_menu)
        self.register.pushButton.clicked.connect(self.startmain_menu)
        self.show()   


    def startmenu_2(self):
        self.menu_2.setupUi(self)
        self.menu_2.anime.clicked.connect(self.startanime)
        self.menu_2.manga.clicked.connect(self.startmanga)
        self.menu_2.webtoon.clicked.connect(self.startwebtoon)
        self.show()
        

    def startanime(self):
        self.shelf.remove(self.gui.product)
        self.bin = Bin()
        self.bin.add(self.gui.product)
        self.gui_4.setupUi(self)
        self.gui_4.pushButton.clicked.connect(self.startGUIbox)
        self.show()
        
    
    def startmanga(self):
        self.gui_box_type.setupUi(self)
        self.gui_box_type.cont.clicked.connect(self.startGUIAddress)
        self.show()
    
    def startwebtoon(self):
        self.gui_address.setupUi(self)
        self.gui_address.cont.clicked.connect(self.startGUIfinal)
        self.show()
        
                   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())