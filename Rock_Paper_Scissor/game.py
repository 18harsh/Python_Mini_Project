# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox
from random import randint


computerscore = 0
playerscore = 0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("game.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.computerlabel = QtWidgets.QLabel(self.centralwidget)
        self.computerlabel.setGeometry(QtCore.QRect(40, 70, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.computerlabel.setFont(font)
        self.computerlabel.setObjectName("computerlabel")
        self.yourlabel = QtWidgets.QLabel(self.centralwidget)
        self.yourlabel.setGeometry(QtCore.QRect(380, 70, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.yourlabel.setFont(font)
        self.yourlabel.setObjectName("yourlabel")
        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setGeometry(QtCore.QRect(140, 0, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.namelabel.setFont(font)
        self.namelabel.setObjectName("namelabel")
        self.compimglabel = QtWidgets.QLabel(self.centralwidget)
        self.compimglabel.setGeometry(QtCore.QRect(60, 120, 151, 121))
        self.compimglabel.setText("")
        self.compimglabel.setPixmap(QtGui.QPixmap("rock.png"))
        self.compimglabel.setObjectName("compimglabel")
        self.yourimglabel = QtWidgets.QLabel(self.centralwidget)
        self.yourimglabel.setGeometry(QtCore.QRect(370, 120, 151, 121))
        self.yourimglabel.setText("")
        self.yourimglabel.setPixmap(QtGui.QPixmap("rock.png"))
        self.yourimglabel.setObjectName("yourimglabel")
        self.vslabel = QtWidgets.QLabel(self.centralwidget)
        self.vslabel.setGeometry(QtCore.QRect(260, 160, 47, 41))
        self.vslabel.setText("")
        self.vslabel.setPixmap(QtGui.QPixmap("game.png"))
        self.vslabel.setObjectName("vslabel")
        self.startpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startpushButton.setGeometry(QtCore.QRect(170, 300, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.startpushButton.setFont(font)
        self.startpushButton.setStyleSheet("background-color: green\n"
"")
        self.startpushButton.setObjectName("startpushButton")
        self.stoppushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stoppushButton.setGeometry(QtCore.QRect(330, 300, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.stoppushButton.setFont(font)
        self.stoppushButton.setStyleSheet("background-color: red\n"
"\n"
"")
        self.stoppushButton.setObjectName("stoppushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.timer = QTimer(MainWindow)
        self.timer.setInterval(50)
        self.startpushButton.clicked.connect(self.start)
        self.timer.timeout.connect(self.playGame)
        self.stoppushButton.clicked.connect(self.stop)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock-Paper_Scissor"))
        self.computerlabel.setText(_translate("MainWindow", "Computer Score:"))
        self.yourlabel.setText(_translate("MainWindow", "Your Score:"))
        self.namelabel.setText(_translate("MainWindow", "Rock-Paper-Scissor"))
        self.startpushButton.setText(_translate("MainWindow", "Start"))
        self.stoppushButton.setText(_translate("MainWindow", "Stop"))
        

    def start(self):
        self.timer.start()

    def playGame(self):
        self.rndComputer = randint(1,3)
        self.rndplayer = randint(1,3)
        if self.rndComputer == 1:
            self.compimglabel.setPixmap(QtGui.QPixmap("rock.png"))  
        elif self.rndComputer == 2:
            self.compimglabel.setPixmap(QtGui.QPixmap("paper.png"))
        else:
            self.compimglabel.setPixmap(QtGui.QPixmap("scissors.png"))         

          
        if self.rndplayer == 1:
            self.yourimglabel.setPixmap(QtGui.QPixmap("rock.png"))  
        elif self.rndplayer == 2:
            self.yourimglabel.setPixmap(QtGui.QPixmap("paper.png"))
        else:
            self.yourimglabel.setPixmap(QtGui.QPixmap("scissors.png"))         
  

    def stop(self):
        msg = QMessageBox()
        msg.setWindowTitle("RESULT")
        msg.setText("Information")
        msg.setIcon(QMessageBox.Information)

        global computerscore
        global playerscore
        self.timer.stop() 
        if self.rndComputer == self.rndplayer:
            msg.setInformativeText("Draw Game")
        elif self.rndComputer == 1 :
            if self.rndplayer == 3:
                computerscore+=1
                msg.setInformativeText("Computer Won")
            else:
                playerscore+=1
                msg.setInformativeText("You Won")    
        elif self.rndComputer == 2:
            if self.rndplayer == 1:
                computerscore+=1
                msg.setInformativeText("Computer Won")
            else:
                playerscore+=1
                msg.setInformativeText("You Won")   
        elif self.rndComputer == 3 :
            if self.rndplayer == 2:
                computerscore+=1
                msg.setInformativeText("Computer Won")
            else:
                playerscore+=1
                msg.setInformativeText("You Won")                       

        self.computerlabel.setText("Computer Score: "+str(computerscore))        
        self.yourlabel.setText("Your Score: "+str(playerscore))
        self.computerlabel.adjustSize()
        self.yourlabel.adjustSize()
        x = msg.exec_()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

