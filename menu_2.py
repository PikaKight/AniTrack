from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1026, 595)
        MainWindow.setStyleSheet("background-color: rgb(208, 255, 254);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(-5, 0, 1031, 141))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(50)
        self.Title.setFont(font)
        self.Title.setStyleSheet("background-color: rgb(25, 120, 200);")
        self.Title.setObjectName("Title")
        self.anime = QtWidgets.QPushButton(self.centralwidget)
        self.anime.setGeometry(QtCore.QRect(50, 210, 251, 301))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(50)
        self.anime.setFont(font)
        self.anime.setStyleSheet("background-color: rgb(98, 255, 242);")
        self.anime.setObjectName("anime")
        self.Manga = QtWidgets.QPushButton(self.centralwidget)
        self.Manga.setGeometry(QtCore.QRect(390, 210, 251, 301))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(50)
        self.Manga.setFont(font)
        self.Manga.setStyleSheet("background-color: rgb(98, 255, 242);")
        self.Manga.setObjectName("Manga")
        self.webtoon = QtWidgets.QPushButton(self.centralwidget)
        self.webtoon.setGeometry(QtCore.QRect(730, 210, 251, 301))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(45)
        self.webtoon.setFont(font)
        self.webtoon.setStyleSheet("background-color: rgb(98, 255, 242);")
        self.webtoon.setObjectName("webtoon")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#000000;\">AniTrack</span></p></body></html>"))
        self.anime.setText(_translate("MainWindow", "Anime"))
        self.Manga.setText(_translate("MainWindow", "Manga"))
        self.webtoon.setText(_translate("MainWindow", "Webtoon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
