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
        self.back_2 = QtWidgets.QPushButton(self.centralwidget)
        self.back_2.setGeometry(QtCore.QRect(300, 20, 241, 81))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        self.back_2.setFont(font)
        self.back_2.setStyleSheet("background-color: rgb(82, 255, 255);")
        self.back_2.setObjectName("back_2")
        self.back_main = QtWidgets.QPushButton(self.centralwidget)
        self.back_main.setGeometry(QtCore.QRect(0, 0, 271, 121))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(50)
        self.back_main.setFont(font)
        self.back_main.setStyleSheet("background-color: rgb(25, 120, 200);")
        self.back_main.setObjectName("back_main")
        self.save = QtWidgets.QToolButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(630, 20, 241, 81))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        self.save.setFont(font)
        self.save.setStyleSheet("background-color: rgb(82, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        self.save.setObjectName("save")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(70, 140, 901, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(35)
        self.title.setFont(font)
        self.title.setText(list(back.Anime().view_all())[0])
        self.title.setObjectName(list(back.Anime().view_all())[0])
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 220, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(35)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ep = QtWidgets.QLineEdit(self.centralwidget)
        self.ep.setGeometry(QtCore.QRect(100, 290, 241, 71))
        self.ep.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ep.setObjectName("ep")
        self.addd = QtWidgets.QPushButton(self.centralwidget)
        self.addd.setGeometry(QtCore.QRect(80, 400, 151, 131))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(50)
        self.addd.setFont(font)
        self.addd.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.addd.setObjectName("add")
        self.subb = QtWidgets.QPushButton(self.centralwidget)
        self.subb.setGeometry(QtCore.QRect(280, 400, 151, 131))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(50)
        self.subb.setFont(font)
        self.subb.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.subb.setObjectName("sub")
        self.remove = QtWidgets.QPushButton(self.centralwidget)
        self.remove.setGeometry(QtCore.QRect(560, 400, 411, 121))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(45)
        self.remove.setFont(font)
        self.remove.setStyleSheet("alternate-background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 0, 0);")
        self.remove.setObjectName("remove")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back_2.setText(_translate("MainWindow", "Back"))
        self.back_main.setText(_translate("MainWindow", "AniTrack"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.label_2.setText(_translate("MainWindow", "# of Ep"))
        self.addd.setText(_translate("MainWindow", "+"))
        self.subb.setText(_translate("MainWindow", "-"))
        self.remove.setText(_translate("MainWindow", "Remove Anime"))
        self.ep.setText(_translate("MainWindow", "1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
