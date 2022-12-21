

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import subprocess
import numpy as np


class Ui_MainView(object):
    def setupUi(self, MainView):
        MainView.setObjectName("MainView")
        MainView.resize(799, 600)
        self.centralwidget = QtWidgets.QWidget(MainView)
        self.centralwidget.setObjectName("centralwidget")
        self.defaultFrame = QtWidgets.QFrame(self.centralwidget)
        self.defaultFrame.setGeometry(QtCore.QRect(10, 20, 800, 600))
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.defaultFrame.setFont(font)
        self.defaultFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.defaultFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.defaultFrame.setObjectName("defaultFrame")
        self.lblNumeProiect = QtWidgets.QLabel(self.defaultFrame)
        self.lblNumeProiect.setGeometry(QtCore.QRect(0, 0, 321, 61))
        self.lblNumeProiect.setObjectName("lblNumeProiect")
        self.lblNumeSiPrenume = QtWidgets.QLabel(self.defaultFrame)
        self.lblNumeSiPrenume.setGeometry(QtCore.QRect(450, 0, 321, 61))
        self.lblNumeSiPrenume.setObjectName("lblNumeSiPrenume")
        self.frameForPages = QtWidgets.QFrame(self.defaultFrame)
        self.frameForPages.setGeometry(QtCore.QRect(-10, 50, 791, 471))
        self.frameForPages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameForPages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameForPages.setObjectName("frameForPages")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frameForPages)
        self.stackedWidget.setGeometry(QtCore.QRect(12, 12, 771, 461))
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageStartUp = QtWidgets.QWidget()
        self.pageStartUp.setObjectName("pageStartUp")
        self.btnStart = QtWidgets.QPushButton(self.pageStartUp)
        self.btnStart.setGeometry(QtCore.QRect(0, 70, 771, 91))
        self.btnStart.setObjectName("btnStart")
        self.btnCerinta = QtWidgets.QPushButton(self.pageStartUp)
        self.btnCerinta.setGeometry(QtCore.QRect(0, 180, 771, 91))
        self.btnCerinta.setObjectName("btnCerinta")
        self.btnExitStartUp = QtWidgets.QPushButton(self.pageStartUp)
        self.btnExitStartUp.setGeometry(QtCore.QRect(0, 290, 771, 91))
        self.btnExitStartUp.setObjectName("btnExitStartUp")
        self.stackedWidget.addWidget(self.pageStartUp)
        self.pageSetPlayerNames = QtWidgets.QWidget()
        self.pageSetPlayerNames.setObjectName("pageSetPlayerNames")
        self.btnSetFirstName = QtWidgets.QPushButton(self.pageSetPlayerNames)
        self.btnSetFirstName.setGeometry(QtCore.QRect(290, 90, 171, 31))
        self.btnSetFirstName.setObjectName("btnSetFirstName")
        self.lblPlayerSection = QtWidgets.QLabel(self.pageSetPlayerNames)
        self.lblPlayerSection.setGeometry(QtCore.QRect(10, 40, 161, 51))
        self.lblPlayerSection.setObjectName("lblPlayerSection")
        self.lblPlayer2Section = QtWidgets.QLabel(self.pageSetPlayerNames)
        self.lblPlayer2Section.setGeometry(QtCore.QRect(10, 170, 161, 51))
        self.lblPlayer2Section.setObjectName("lblPlayer2Section")
        self.lblIsFirstSet = QtWidgets.QLabel(self.pageSetPlayerNames)
        self.lblIsFirstSet.setGeometry(QtCore.QRect(10, 10, 501, 31))
        self.lblIsFirstSet.setObjectName("lblIsFirstSet")
        self.lineEdit = QtWidgets.QLineEdit(self.pageSetPlayerNames)
        self.lineEdit.setGeometry(QtCore.QRect(0, 90, 271, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lblIsSecondSet = QtWidgets.QLabel(self.pageSetPlayerNames)
        self.lblIsSecondSet.setGeometry(QtCore.QRect(0, 140, 501, 31))
        self.lblIsSecondSet.setObjectName("lblIsSecondSet")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.pageSetPlayerNames)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 220, 271, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.btnSetSecondName = QtWidgets.QPushButton(self.pageSetPlayerNames)
        self.btnSetSecondName.setGeometry(QtCore.QRect(290, 220, 171, 31))
        self.btnSetSecondName.setObjectName("btnSetSecondName")
        self.btnStartGame = QtWidgets.QPushButton(self.pageSetPlayerNames)
        self.btnStartGame.setGeometry(QtCore.QRect(0, 290, 771, 91))
        self.btnStartGame.setObjectName("btnStartGame")
        self.btnBackNamePick = QtWidgets.QPushButton(self.pageSetPlayerNames)
        self.btnBackNamePick.setGeometry(QtCore.QRect(390, 380, 381, 71))
        self.btnBackNamePick.setObjectName("btnBackNamePick")
        self.btnExitNamePick = QtWidgets.QPushButton(self.pageSetPlayerNames)
        self.btnExitNamePick.setGeometry(QtCore.QRect(0, 380, 381, 71))
        self.btnExitNamePick.setObjectName("btnExitNamePick")
        self.stackedWidget.addWidget(self.pageSetPlayerNames)
        self.pageSelectNameRobot = QtWidgets.QWidget()
        self.pageSelectNameRobot.setObjectName("pageSelectNameRobot")
        self.btnStartGame_2 = QtWidgets.QPushButton(self.pageSelectNameRobot)
        self.btnStartGame_2.setGeometry(QtCore.QRect(0, 290, 771, 91))
        self.btnStartGame_2.setObjectName("btnStartGame_2")
        self.lblPlayerSection_2 = QtWidgets.QLabel(self.pageSelectNameRobot)
        self.lblPlayerSection_2.setGeometry(QtCore.QRect(10, 40, 161, 51))
        self.lblPlayerSection_2.setObjectName("lblPlayerSection_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.pageSelectNameRobot)
        self.lineEdit_4.setGeometry(QtCore.QRect(0, 90, 271, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.btnSetFirstName_2 = QtWidgets.QPushButton(
            self.pageSelectNameRobot)
        self.btnSetFirstName_2.setGeometry(QtCore.QRect(290, 90, 171, 31))
        self.btnSetFirstName_2.setObjectName("btnSetFirstName_2")
        self.lblIsFirstSet_2 = QtWidgets.QLabel(self.pageSelectNameRobot)
        self.lblIsFirstSet_2.setGeometry(QtCore.QRect(10, 10, 501, 31))
        self.lblIsFirstSet_2.setObjectName("lblIsFirstSet_2")
        self.lblPlayer2Section_3 = QtWidgets.QLabel(self.pageSelectNameRobot)
        self.lblPlayer2Section_3.setGeometry(QtCore.QRect(10, 180, 161, 51))
        self.lblPlayer2Section_3.setObjectName("lblPlayer2Section_3")
        self.lblIsSecondSet_3 = QtWidgets.QLabel(self.pageSelectNameRobot)
        self.lblIsSecondSet_3.setGeometry(QtCore.QRect(0, 160, 501, 31))
        self.lblIsSecondSet_3.setObjectName("lblIsSecondSet_3")
        self.lblPlayer2Section_4 = QtWidgets.QLabel(self.pageSelectNameRobot)
        self.lblPlayer2Section_4.setGeometry(QtCore.QRect(10, 220, 281, 51))
        self.lblPlayer2Section_4.setObjectName("lblPlayer2Section_4")
        self.btnBackNamePick_2 = QtWidgets.QPushButton(
            self.pageSelectNameRobot)
        self.btnBackNamePick_2.setGeometry(QtCore.QRect(390, 380, 381, 71))
        self.btnBackNamePick_2.setObjectName("btnBackNamePick_2")
        self.btnExitNamePick_2 = QtWidgets.QPushButton(
            self.pageSelectNameRobot)
        self.btnExitNamePick_2.setGeometry(QtCore.QRect(0, 380, 381, 71))
        self.btnExitNamePick_2.setObjectName("btnExitNamePick_2")
        self.stackedWidget.addWidget(self.pageSelectNameRobot)
        self.pageGame = QtWidgets.QWidget()
        self.pageGame.setObjectName("pageGame")
        self.btnBackNamePick_3 = QtWidgets.QPushButton(self.pageGame)
        self.btnBackNamePick_3.setGeometry(QtCore.QRect(390, 380, 381, 71))
        self.btnBackNamePick_3.setObjectName("btnBackNamePick_3")
        self.btnExitNamePick_3 = QtWidgets.QPushButton(self.pageGame)
        self.btnExitNamePick_3.setGeometry(QtCore.QRect(0, 380, 381, 71))
        self.btnExitNamePick_3.setObjectName("btnExitNamePick_3")
        self.lblNaming = QtWidgets.QLabel(self.pageGame)
        self.lblNaming.setGeometry(QtCore.QRect(250, 10, 271, 31))
        self.lblNaming.setObjectName("lblNaming")
        self.lblScore = QtWidgets.QLabel(self.pageGame)
        self.lblScore.setGeometry(QtCore.QRect(330, 40, 71, 31))
        self.lblScore.setObjectName("lblScore")
        self.lblTable = QtWidgets.QLabel(self.pageGame)
        self.lblTable.setGeometry(QtCore.QRect(110, 70, 481, 311))
        self.lblTable.setText("")
        self.lblTable.setPixmap(QtGui.QPixmap(
            "D:\\git\\GitHub\\ProiectPython\\venv\\table.png"))
        self.lblTable.setScaledContents(True)
        self.lblTable.setObjectName("lblTable")
        self.lbl00 = QtWidgets.QLabel(self.pageGame)
        self.lbl00.setGeometry(QtCore.QRect(180, 100, 81, 71))

        self.lbl00.setText("")
        self.lbl00.setPixmap(QtGui.QPixmap(
            "D:\\git\\GitHub\\ProiectPython\\venv\\x.png"))
        self.lbl00.setScaledContents(True)
        self.lbl00.setObjectName("lbl00")
        self.lbl01 = QtWidgets.QLabel(self.pageGame)
        self.lbl01.setGeometry(QtCore.QRect(300, 100, 81, 71))
        self.lbl01.setText("")
        self.lbl01.setPixmap(QtGui.QPixmap(
            "D:\\git\\GitHub\\ProiectPython\\venv\\x.png"))
        self.lbl01.setScaledContents(True)
        self.lbl01.setObjectName("lbl01")
        self.lbl02 = QtWidgets.QLabel(self.pageGame)
        self.lbl02.setGeometry(QtCore.QRect(450, 100, 81, 71))
        self.lbl02.setText("")
        self.lbl02.setPixmap(QtGui.QPixmap(
            "D:\\git\\GitHub\\ProiectPython\\venv\\x.png"))
        self.lbl02.setScaledContents(True)
        self.lbl02.setObjectName("lbl02")
        self.lbl10 = QtWidgets.QLabel(self.pageGame)
        self.lbl10.setGeometry(QtCore.QRect(170, 190, 101, 71))
        self.lbl10.setText("")
        self.lbl10.setPixmap(QtGui.QPixmap(
            "D:\\git\\GitHub\\ProiectPython\\venv\\x.png"))
        self.lbl10.setScaledContents(True)
        self.lbl10.setObjectName("lbl10")
        self.lbl11 = QtWidgets.QLabel(self.pageGame)
        self.lbl11.setGeometry(QtCore.QRect(300, 190, 101, 71))
        self.lbl11.setText("")
        self.lbl11.setPixmap(QtGui.QPixmap(
            "D:\\git\\GitHub\\ProiectPython\\venv\\x.png"))
        self.lbl11.setScaledContents(True)
        self.lbl11.setObjectName("lbl11")
        self.lbl12 = QtWidgets.QLabel(self.pageGame)
        self.lbl12.setGeometry(QtCore.QRect(440, 190, 101, 71))
        self.lbl12.setText("")
        self.lbl12.setPixmap(QtGui.QPixmap(
            "D:\\git\\GitHub\\ProiectPython\\venv\\x.png"))
        self.lbl12.setScaledContents(True)
        self.lbl12.setObjectName("lbl12")
        self.lbl20 = QtWidgets.QLabel(self.pageGame)
        self.lbl20.setGeometry(QtCore.QRect(170, 280, 101, 71))
        self.lbl20.setText("")
        self.lbl20.setPixmap(QtGui.QPixmap(
            "D:\\git\\GitHub\\ProiectPython\\venv\\x.png"))
        self.lbl20.setScaledContents(True)
        self.lbl20.setObjectName("lbl20")
        self.lbl21 = QtWidgets.QLabel(self.pageGame)
        self.lbl21.setGeometry(QtCore.QRect(300, 280, 101, 71))
        self.lbl21.setText("")
        self.lbl21.setPixmap(QtGui.QPixmap(
            "D:\\git\\GitHub\\ProiectPython\\venv\\x.png"))
        self.lbl21.setScaledContents(True)
        self.lbl21.setObjectName("lbl21")
        self.lbl22 = QtWidgets.QLabel(self.pageGame)
        self.lbl22.setGeometry(QtCore.QRect(450, 280, 101, 71))
        self.lbl22.setText("")
        self.lbl22.setPixmap(QtGui.QPixmap(
            "D:\\git\\GitHub\\ProiectPython\\venv\\x.png"))
        self.lbl22.setScaledContents(True)
        self.lbl22.setObjectName("lbl22")
        self.stackedWidget.addWidget(self.pageGame)
        self.pageSelectGameType = QtWidgets.QWidget()
        self.pageSelectGameType.setObjectName("pageSelectGameType")
        self.btnRobotRandom = QtWidgets.QPushButton(self.pageSelectGameType)
        self.btnRobotRandom.setGeometry(QtCore.QRect(0, 140, 771, 91))
        self.btnRobotRandom.setObjectName("btnRobotRandom")
        self.btnPlayerVSPlayer = QtWidgets.QPushButton(self.pageSelectGameType)
        self.btnPlayerVSPlayer.setGeometry(QtCore.QRect(0, 30, 771, 91))
        self.btnPlayerVSPlayer.setObjectName("btnPlayerVSPlayer")
        self.btnRobotAI = QtWidgets.QPushButton(self.pageSelectGameType)
        self.btnRobotAI.setGeometry(QtCore.QRect(0, 250, 771, 91))
        self.btnRobotAI.setObjectName("btnRobotAI")
        self.btnExit = QtWidgets.QPushButton(self.pageSelectGameType)
        self.btnExit.setGeometry(QtCore.QRect(0, 360, 381, 91))
        self.btnExit.setObjectName("btnExit")
        self.btnBack = QtWidgets.QPushButton(self.pageSelectGameType)
        self.btnBack.setGeometry(QtCore.QRect(390, 360, 381, 91))
        self.btnBack.setObjectName("btnBack")
        self.stackedWidget.addWidget(self.pageSelectGameType)
        MainView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 26))
        self.menubar.setObjectName("menubar")
        self.menuConfig = QtWidgets.QMenu(self.menubar)
        self.menuConfig.setObjectName("menuConfig")
        MainView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainView)
        self.statusbar.setObjectName("statusbar")
        MainView.setStatusBar(self.statusbar)
        self.actionSize_Color_Fonts = QtWidgets.QAction(MainView)
        self.actionSize_Color_Fonts.setObjectName("actionSize_Color_Fonts")
        self.menuConfig.addAction(self.actionSize_Color_Fonts)
        self.menubar.addAction(self.menuConfig.menuAction())

        self.retranslateUi(MainView)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainView)

    def retranslateUi(self, MainView):
        _translate = QtCore.QCoreApplication.translate
        MainView.setWindowTitle(_translate("MainView", "X și 0"))
        self.lblNumeProiect.setText(_translate("MainView", "Proiect X și 0 "))
        self.lblNumeSiPrenume.setText(_translate(
            "MainView", "Lucaci Alexandru-Constantin"))
        self.btnStart.setText(_translate("MainView", "Start"))
        self.btnCerinta.setText(_translate("MainView", "Cerința"))
        self.btnExitStartUp.setText(_translate("MainView", "Exit"))
        self.btnSetFirstName.setText(_translate("MainView", "Set Name"))
        self.lblPlayerSection.setText(_translate("MainView", "Player 1"))
        self.lblPlayer2Section.setText(_translate("MainView", "Player 2"))
        self.lblIsFirstSet.setText(_translate(
            "MainView", " Name for the first player hasn\'t been set "))
        self.lblIsSecondSet.setText(_translate(
            "MainView", " Name for the second player hasn\'t been set "))
        self.btnSetSecondName.setText(_translate("MainView", "Set Name"))
        self.btnStartGame.setText(_translate("MainView", "Start"))
        self.btnBackNamePick.setText(_translate("MainView", "Back"))
        self.btnExitNamePick.setText(_translate("MainView", "Exit"))
        self.btnStartGame_2.setText(_translate("MainView", "Start"))
        self.lblPlayerSection_2.setText(_translate("MainView", "Player 1"))
        self.btnSetFirstName_2.setText(_translate("MainView", "Set Name"))
        self.lblIsFirstSet_2.setText(_translate(
            "MainView", " Name for the first player hasn\'t been set "))
        self.lblPlayer2Section_3.setText(_translate("MainView", "Player 2"))
        self.lblIsSecondSet_3.setText(_translate(
            "MainView", "The name fro the second player is set to ROBOT"))
        self.lblPlayer2Section_4.setText(_translate("MainView", "ROBOT"))
        self.btnBackNamePick_2.setText(_translate("MainView", "Back"))
        self.btnExitNamePick_2.setText(_translate("MainView", "Exit"))
        self.btnBackNamePick_3.setText(_translate("MainView", "Back"))
        self.btnExitNamePick_3.setText(_translate("MainView", "Exit"))
        self.lblNaming.setText(_translate("MainView", "Player 1 VS Player2"))
        self.lblScore.setText(_translate("MainView", "0:0"))
        self.btnRobotRandom.setText(_translate(
            "MainView", "Robot ( random choices)"))
        self.btnPlayerVSPlayer.setText(
            _translate("MainView", "Player VS Player"))
        self.btnRobotAI.setText(_translate(
            "MainView", "Robot ( best choices)"))
        self.btnExit.setText(_translate("MainView", "Exit"))
        self.btnBack.setText(_translate("MainView", "Back"))
        self.menuConfig.setTitle(_translate("MainView", "Config"))
        self.actionSize_Color_Fonts.setText(
            _translate("MainView", "Size,Color,Fonts"))

        # MainPage Buttons
        self.typeOfGame = -1
        self.btnStart.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(4))
        # self.btnCerinta.clicked.connect()
        self.btnExitStartUp.clicked.connect(lambda: exit())
        # PageSelectGameType Buttons
        self.btnBack.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0))
        self.btnExit.clicked.connect(lambda: exit())
        self.btnPlayerVSPlayer.clicked.connect(
            lambda: self.changeToNames(0, 1))
        self.btnRobotRandom.clicked.connect(
            lambda: self.changeToNames(1, 2))
        self.btnRobotAI.clicked.connect(
            lambda: self.changeToNames(2, 2))

        # PageSetPlayerNames Buttons
        self.btnBackNamePick.clicked.connect(
            self.backBtnRessetName)
        self.btnExitNamePick.clicked.connect(lambda: exit())
        self.name1 = 'Player1'
        self.name2 = 'Player2'

        self.btnSetFirstName.clicked.connect(
            lambda: self.setName(self.lineEdit.text(), 1))
        self.btnSetSecondName.clicked.connect(
            lambda: self.setName(self.lineEdit_3.text(), 2))
        # todo
        # start btn
        # self.typeOfGame = -1
        self.btnStartGame.clicked.connect(
            lambda: self.setTypeOfGame(self.typeOfGame))
        # pageSelectNameRobot Buttons
        self.btnBackNamePick_2.clicked.connect(
            self.backBtnRessetName)
        self.btnExitNamePick_2.clicked.connect(lambda: exit())
        self.btnSetFirstName_2.clicked.connect(
            lambda: self.setName(self.lineEdit_4.text(), 3))
        self.btnStartGame_2.clicked.connect(
            lambda: self.setTypeOfGame(self.typeOfGame))
        # pageGame Buttons

        self.btnBackNamePick_3.clicked.connect(
            lambda: self.backBtnRessetName())
        self.btnExitNamePick_3.clicked.connect(lambda: exit())
        self.lbl00.mousePressEvent = lambda event: self.modifying(
            event, self.lbl00)

    def changeToNames(self, type, index):
        self.typeOfGame = type
        self.stackedWidget.setCurrentIndex(index)

    def modifying(self, event, id):
        print(event)
        print(id.accessibleName())
        if self.round == 0:

            id.setPixmap(QtGui.QPixmap(
                "D:\\git\\GitHub\\ProiectPython\\venv\\x.png"))
            self.round = (self.round+1) % 2
        else:
            id.setPixmap(QtGui.QPixmap(
                "D:\\git\\GitHub\\ProiectPython\\venv\\0.png"))
            self.round = (self.round+1) % 2

    def setTypeOfGame(self, typeOfGame):
        self.typeOfGame = typeOfGame
        self.stackedWidget.setCurrentIndex(3)
        self.naming = str(self.name1) + " VS " + str(self.name2)
        self.lblNaming.setText(self.naming)
        print(self.naming)
        self.scorePlayer1 = 0
        self.scorePlayer2 = 0
        self.round = 0
        self.matrixVal = np.zeros((3, 3))
        print(self.matrixVal)
        # x an 0 game (tic tac toe)
        print(self.typeOfGame)

        for i in range(3):
            for j in range(3):
                if (self.matrixVal[i][j] == 0):
                    if i == 0:
                        if j == 0:
                            self.lbl00.setPixmap(QtGui.QPixmap(
                                "D:\\git\\GitHub\\ProiectPython\\venv\\nimic.png"))
                        elif j == 1:
                            self.lbl01.setPixmap(QtGui.QPixmap(
                                "D:\\git\\GitHub\\ProiectPython\\venv\\nimic.png"))
                        elif j == 2:
                            self.lbl02.setPixmap(QtGui.QPixmap(
                                "D:\\git\\GitHub\\ProiectPython\\venv\\nimic.png"))
                    elif i == 1:
                        if j == 0:
                            self.lbl10.setPixmap(QtGui.QPixmap(
                                "D:\\git\\GitHub\\ProiectPython\\venv\\nimic.png"))
                        elif j == 1:
                            self.lbl11.setPixmap(QtGui.QPixmap(
                                "D:\\git\\GitHub\\ProiectPython\\venv\\nimic.png"))
                        elif j == 2:
                            self.lbl12.setPixmap(QtGui.QPixmap(
                                "D:\\git\\GitHub\\ProiectPython\\venv\\nimic.png"))
                    elif i == 2:
                        if j == 0:
                            self.lbl20.setPixmap(QtGui.QPixmap(
                                "D:\\git\\GitHub\\ProiectPython\\venv\\nimic.png"))
                        elif j == 1:
                            self.lbl21.setPixmap(QtGui.QPixmap(
                                "D:\\git\\GitHub\\ProiectPython\\venv\\nimic.png"))
                        elif j == 2:
                            self.lbl22.setPixmap(QtGui.QPixmap(
                                "D:\\git\\GitHub\\ProiectPython\\venv\\nimic.png"))

    def setName(self, name, playerNumber):
        if name != '':
            if playerNumber == 1:
                self.lblIsFirstSet.setText(
                    "Name for the first player is set to " + name)
                self.name1 = name
                print(self.name1)

            elif playerNumber == 2:
                self.lblIsSecondSet.setText(
                    "Name for the second player is set to " + name)
                self.name2 = name
                print(self.name2)
            elif playerNumber == 3:
                self.lblIsFirstSet_2.setText(
                    "Name for the first player is set to " + name)
                self.name1 = name
                self.name2 = "ROBOT"
                print(self.name2)

    def backBtnRessetName(self):
        self.stackedWidget.setCurrentIndex(4)
        self.name1 = 'Player1'
        self.name2 = 'Player2'
        self.lblIsFirstSet.setText(
            " Name for the first player hasn't been set ")
        self.lblIsSecondSet.setText(
            " Name for the second player hasn't been set ")
        self.lblIsFirstSet_2.setText(
            " Name for the first player hasn't been set ")
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit.setText('')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainView = QtWidgets.QMainWindow()
    ui = Ui_MainView()
    ui.setupUi(MainView)
    MainView.show()
    sys.exit(app.exec_())