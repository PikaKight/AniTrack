from PyQt5 import QtCore, QtGui, QtWidgets
import back, main_menu,register,menu_2, anime, manga, webtoon, adda, addm, addw, edita, editm, editw, json

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # self.main_menu = main_menu.Ui_MainWindow()
        # self.register = register.Ui_MainWindow()
        self.menu_2 = menu_2.Ui_MainWindow()
        self.anime = anime.Ui_MainWindow()
        self.manga = manga.Ui_MainWindow()
        self.webtoon = webtoon.Ui_MainWindow()
        self.adda = adda.Ui_MainWindow()
        self.addm = addm.Ui_MainWindow()
        self.addw = addw.Ui_MainWindow()
        self.edita = edita.Ui_MainWindow()
        self.editm = editm.Ui_MainWindow()
        self.editw = editw.Ui_MainWindow()
        # self.startmain_menu()
        self.startmenu_2()

    # def startmain_menu(self):
    #     self.main_menu.setupUi(self)
    #     self.main_menu.register_2.clicked.connect(self.startregister)
    #     self.main_menu.login.clicked.connect(self.startmenu_2)
    #     self.show()
        
        
    # def startregister(self):
    #     self.register.setupUi(self)
    #     self.register.pushButton.clicked.connect(self.startmain_menu)
    #     self.register.pushButton.clicked.connect(self.startmain_menu)
    #     self.show()   


    def startmenu_2(self):
        self.menu_2.setupUi(self)
        if len(list(back.Anime().view_all())) == 0: 
            self.menu_2.anime.clicked.connect(self.addanime)
        else:
            self.menu_2.anime.clicked.connect(self.startanime)
        if len(list(back.Manga().view_all())) == 0: 
            self.menu_2.manga.clicked.connect(self.addmanga)
        else:
            self.menu_2.manga.clicked.connect(self.startmanga)
        if len(list(back.Webtoon().view_all())) == 0: 
            self.menu_2.webtoon.clicked.connect(self.addwebtoon)
        else:
            self.menu_2.webtoon.clicked.connect(self.startwebtoon)
        
        self.show()
        

    def startanime(self):
        self.anime.setupUi(self)
        self.anime.addanime.clicked.connect(self.addanime)
        self.anime.anime.clicked.connect(self.animeedit)
        self.anime.back.clicked.connect(self.startmenu_2)
        self.show()
    
    
    def addanime(self):
        self.adda.setupUi(self)
        self.adda.save.clicked.connect(self.save_a)
        self.adda.back_2.clicked.connect(self.startanime)
        self.adda.back_main.clicked.connect(self.startmenu_2)
        self.show()    
    

    def animeedit(self):
        self.edita.setupUi(self)
        self.edita.back_main.clicked.connect(self.startmenu_2)
        self.edita.back_2.clicked.connect(self.startanime)
        self.edita.addd.clicked.connect(self.add_epa())
        self.edita.subb.clicked.connect(self.sub_eba())
        self.edita.remove.clicked.connect(back.Anime().remove(list(back.Anime().view_all())[0]))
        self.edita.save.clicked.connect(self.save_a)
        self.show()  
       

    def add_epa(self):
        if len(self.edita.ep.text()) != '': 
            back.Anime().add_ep(list(back.Anime().view_all())[0], float(self.edita.ep.text()))
            self.animeedit()
        else: 
            self.animeedit()


    def sub_epa(self):
        if len(self.edita.ep.text()) != '': 
            back.Anime().sub_eb(list(back.Anime().view_all())[0], float(self.edita.ep.text()))
            self.animeedit()
        else: 
            self.animeedit()
            

    def save_a(self):
        back.Anime().add(self.adda.title.text(), float(self.adda.ep.text()), self.adda.version.text())
        back.Anime().save()
        self.startanime()


    def startmanga(self):
        self.anime.setupUi(self)
        self.anime.addanime.clicked.connect(self.addmanga)
        self.anime.anime.clicked.connect(self.mangaedit)
        self.anime.back.clicked.connect(self.startmenu_2)
        self.show()
    
    
    def addmanga(self):
        self.addm.setupUi(self)
        self.addm.save.clicked.connect(self.save_m)
        self.addm.back_2.clicked.connect(self.startmanga)
        self.addm.back_main.clicked.connect(self.startmenu_2)
        self.show()
    

    def mangaedit(self):
        self.editm.setupUi(self)
        self.editm.back_main.clicked.connect(self.startmenu_2)
        self.editm.back_2.clicked.connect(self.startmanga)
        self.editm.add.clicked.connect(self.add_epm())
        self.editm.sub.clicked.connect(self.sub_ebm())
        self.editm.remove.clicked.connect(back.Manga().remove(list(back.Manga().view_all())[0]))
        self.editm.save.clicked.connect(self.save_m)
        self.show()  


    def add_epm(self):
        if len(self.editm.ep.text()) != '':
            back.Manga().add_ep(list(back.Anime().view_all())[0],float(self.editm.ep.text()))
            self.mangaedit()
        else: 
            self.mangaedit()
            


    def sub_epm(self):
        if len(self.editm.ep.text()) != '': 
            back.Manga().sub_eb(list(back.Anime().view_all())[0],float(self.editm.ep.text()))
            mangaedit
        else: 
            self.mangaedit()


    def save_m(self):
        back.Manga().add(self.addm.title.text(), float(self.addm.ep.text()))
        back.Manga().save()
        self.startanime()


    def startwebtoon(self):
        self.anime.setupUi(self)
        self.anime.addanime.clicked.connect(self.addwebtoon)
        self.anime.anime.clicked.connect(self.webtoonedit)
        self.anime.back.clicked.connect(self.startmenu_2)
        self.show()

    
    def addwebtoon(self):
        self.addw.setupUi(self)
        self.addw.save.clicked.connect(self.save_w)
        self.addw.back_2.clicked.connect(self.startwebtoon)
        self.addw.back_main.clicked.connect(self.startmenu_2)
        self.show()


    def webtoonedit(self):
        self.editw.setupUi(self)
        self.editw.back_main.clicked.connect(self.startmenu_2)
        self.editw.back_2.clicked.connect(self.startwebtoon)
        self.editw.addd.clicked.connect(self.add_epw())
        self.editw.subb.clicked.connect(self.sub_ebw())
        self.editw.remove.clicked.connect(back.Webtoon().remove(list(back.Webtoon().view_all())[0]))
        self.editw.save.clicked.connect(self.save_w)
        self.show()  


    def add_epw(self):
        if len(self.editw.ep.text()) != '': 
            back.Webtoon().add_ep(list(back.Anime().view_all())[0],float(self.editw.ep.text()))
            self.webtoonedit()
        else: self.webtoonedit()


    def sub_epw(self):
        if len(self.editw.ep.text()) != '': 
            back.Webtoon().sub_eb(list(back.Anime().view_all())[0], float(self.editw.ep.text()))
            self.webtoonedit()
        else: self.webtoonedit()  


    def save_w(self):
        back.Webtoon().add(self.addw.title.text(), float(self.addw.ep.text()))
        back.Webtoon().save()
        self.startanime()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())