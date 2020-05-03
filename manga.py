from PyQt5 import QtCore, QtGui, QtWidgets
import back


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1026, 595)
        MainWindow.setStyleSheet("background-color: rgb(208, 255, 254);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list = QtWidgets.QScrollArea(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(10, 130, 991, 421))
        self.list.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.list.setFrameShape(QtWidgets.QFrame.Box)
        self.list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.list.setLineWidth(3)
        self.list.setMidLineWidth(1)
        self.list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.list.setWidgetResizable(True)
        self.list.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.list.setObjectName("list")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 956, 386))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.anime = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.anime.setGeometry(QtCore.QRect(10, 20, 911, 51))
        self.anime.setObjectName("anime")
        self.list.setWidget(self.scrollAreaWidgetContents)
        self.addmanga = QtWidgets.QPushButton(self.centralwidget)
        self.addmanga.setGeometry(QtCore.QRect(300, 20, 241, 81))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        self.addmanga.setFont(font)
        self.addmanga.setStyleSheet("background-color: rgb(82, 255, 255);")
        self.addmanga.setObjectName("addmanga")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(0, 0, 271, 121))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(50)
        self.back.setFont(font)
        self.back.setStyleSheet("background-color: rgb(25, 120, 200);")
        self.back.setObjectName("back")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        if len(back.Anime().view_all()) > 0: self.anime.setText(_translate("MainWindow", list(back.Anime().view_all())[0]))
        else: self.anime.setText(_translate("MainWindow", "None"))
        self.addmanga.setText(_translate("MainWindow", "Add manga"))
        self.back.setText(_translate("MainWindow", "AniTrack"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
