from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1026, 597)
        MainWindow.setStyleSheet("background-color: rgb(208, 255, 254);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(-5, 0, 1031, 171))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(50)
        self.Title.setFont(font)
        self.Title.setStyleSheet("background-color: rgb(25, 120, 200);")
        self.Title.setObjectName("Title")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(650, 250, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(30)
        self.login.setFont(font)
        self.login.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.login.setObjectName("login")
        self.register_2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_2.setGeometry(QtCore.QRect(650, 400, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(30)
        self.register_2.setFont(font)
        self.register_2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.register_2.setObjectName("register_2")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(90, 270, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.email.setText("")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(90, 420, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 220, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 370, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; color:#000000;\">AniTrack</span></p></body></html>"))
        self.login.setText(_translate("MainWindow", "Log In"))
        self.register_2.setText(_translate("MainWindow", "Register"))
        self.label.setText(_translate("MainWindow", "Email"))
        self.label_2.setText(_translate("MainWindow", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
