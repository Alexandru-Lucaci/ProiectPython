

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import subprocess
import numpy as np
import random


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
        self.btnRobotAI.setGeometry(QtCore.QRect(0, 250, 391, 91))
        self.btnRobotAI.setObjectName("btnRobotAI")
        self.btnRobotAISmart = QtWidgets.QPushButton(self.pageSelectGameType)
        self.btnRobotAISmart.setGeometry(QtCore.QRect(390, 250, 381, 91))

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
        self.btnRobotAISmart.setText(_translate(
            "MainView", "Robot ( smart choices)"))
        self.btnPlayerVSPlayer.setText(
            _translate("MainView", "Player VS Player"))
        self.btnRobotAI.setText(_translate(
            "MainView", "Robot ( good choices)"))
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
        self.btnRobotAISmart.clicked.connect(
            lambda: self.changeToNames(3, 2))

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
            event, self.lbl00, 0, 0)
        self.lbl01.mousePressEvent = lambda event: self.modifying(
            event, self.lbl01, 0, 1)
        self.lbl02.mousePressEvent = lambda event: self.modifying(
            event, self.lbl02, 0, 2)
        self.lbl10.mousePressEvent = lambda event: self.modifying(
            event, self.lbl10, 1, 0)
        self.lbl11.mousePressEvent = lambda event: self.modifying(
            event, self.lbl11, 1, 1)
        self.lbl12.mousePressEvent = lambda event: self.modifying(
            event, self.lbl12, 1, 2)
        self.lbl20.mousePressEvent = lambda event: self.modifying(
            event, self.lbl20, 2, 0)
        self.lbl21.mousePressEvent = lambda event: self.modifying(
            event, self.lbl21, 2, 1)
        self.lbl22.mousePressEvent = lambda event: self.modifying(
            event, self.lbl22, 2, 2)

    def changeToNames(self, type, index):
        self.typeOfGame = type
        self.stackedWidget.setCurrentIndex(index)

    def modifying(self, event, id, linie, coloana):
        # round 0 -> player 1
        # round 1 -> player 2
        print(event)
        print(id.accessibleName())
        print(f"type of game {self.typeOfGame}")
        if self.typeOfGame == 0:
            if self.round == 0:
                if self.matrixVal[linie, coloana] == -1:
                    id.setPixmap(QtGui.QPixmap(
                        "D:\\git\\GitHub\\ProiectPython\\venv\\x.png"))
                    self.matrixVal[linie, coloana] = self.round
                    self.round = (self.round+1) % 2
                    print(self.matrixVal)
            else:
                if self.matrixVal[linie, coloana] == -1:
                    id.setPixmap(QtGui.QPixmap(
                        "D:\\git\\GitHub\\ProiectPython\\venv\\0.png"))
                    self.matrixVal[linie, coloana] = self.round
                    self.round = (self.round+1) % 2
                    print(self.matrixVal)
                else:
                    return
            # check if draw
            if self.checkIfDraw() == 1 and self.checkIfWon() == 0:
                self.scorePlayer1 += 1
                self.scorePlayer2 += 1
                self.lblScore.setText(
                    f"{self.scorePlayer1} : {self.scorePlayer2}")
                self.resetGame()
            # check if someone won
            if self.checkIfWon() == 1:
                if self.round == 0:
                    self.scorePlayer2 += 1
                else:
                    self.scorePlayer1 += 1
                self.lblScore.setText(
                    f"{self.scorePlayer1} : {self.scorePlayer2}")
                self.resetGame()
        elif self.typeOfGame == 1:
            # player 2 is a robot with random moves
            if self.round == 0:
                # this is player 1
                if self.matrixVal[linie, coloana] == -1:
                    id.setPixmap(QtGui.QPixmap(
                        "D:\\git\\GitHub\\ProiectPython\\venv\\x.png"))
                    self.matrixVal[linie, coloana] = self.round
                    self.round = (self.round+1) % 2
                    print(self.matrixVal)
                else:
                    return
                if self.checkIfDraw() == 1 and self.checkIfWon() == 0:
                    self.scorePlayer1 += 1
                    self.scorePlayer2 += 1
                    self.lblScore.setText(
                        f"{self.scorePlayer1} : {self.scorePlayer2}")
                    self.resetGame()
                # check if someone won
                elif self.checkIfWon() == 1:
                    if self.round == 0:
                        self.scorePlayer2 += 1
                    else:
                        self.scorePlayer1 += 1
                    self.lblScore.setText(
                        f"{self.scorePlayer1} : {self.scorePlayer2}")
                    self.resetGame()
                else:
                    # now the robot is moving and we need to find a random place
                    # where to move
                    (linie, coloana) = self.pickRandomNumber()

                    self.whereRobotPutY(linie, coloana)
                    self.matrixVal[linie, coloana] = self.round
                    self.round = (self.round+1) % 2
                    print(self.matrixVal)
                    if self.checkIfDraw() == 1 and self.checkIfWon() == 0:
                        self.scorePlayer1 += 1
                        self.scorePlayer2 += 1
                        self.lblScore.setText(
                            f"{self.scorePlayer1} : {self.scorePlayer2}")
                        self.resetGame()
                # check if someone won
                    elif self.checkIfWon() == 1:
                        if self.round == 0:
                            self.scorePlayer2 += 1
                        else:
                            self.scorePlayer1 += 1
                        self.lblScore.setText(
                            f"{self.scorePlayer1} : {self.scorePlayer2}")
                        self.resetGame()
            # else:
            #     never in this case
            #     print("robot is starting")
            #     (linie, coloana) = self.pickRandomNumber()
            #     self.whereRobotPutY(linie, coloana)
            #     self.matrixVal[linie, coloana] = self.round
            #     self.round = (self.round+1) % 2
            #     print(self.matrixVal)
        elif self.typeOfGame == 2:
            # player 2 is a robot with half random moves
            if self.round == 0:
                # this is player 1
                if self.matrixVal[linie, coloana] == -1:
                    id.setPixmap(QtGui.QPixmap(
                        "D:\\git\\GitHub\\ProiectPython\\venv\\x.png"))
                    self.matrixVal[linie, coloana] = self.round
                    self.round = (self.round+1) % 2
                    print(self.matrixVal)
                else:
                    return
                if self.checkIfDraw() == 1 and self.checkIfWon() == 0:
                    self.scorePlayer1 += 1
                    self.scorePlayer2 += 1
                    self.lblScore.setText(
                        f"{self.scorePlayer1} : {self.scorePlayer2}")
                    self.resetGame()
                # check if someone won
                elif self.checkIfWon() == 1:
                    if self.round == 0:
                        self.scorePlayer2 += 1
                    else:
                        self.scorePlayer1 += 1
                    self.lblScore.setText(
                        f"{self.scorePlayer1} : {self.scorePlayer2}")
                    self.resetGame()
                else:
                    # check to see if is the first move for ai
                    if self.turnRandom() == 0:
                        # choose a random move
                        (linie, coloana) = self.pickRandomNumber()
                        self.whereRobotPutY(linie, coloana)
                        self.matrixVal[linie, coloana] = self.round
                        self.round = (self.round+1) % 2
                        print(self.matrixVal)
                        if self.checkIfDraw() == 1 and self.checkIfWon() == 0:
                            self.scorePlayer1 += 1
                            self.scorePlayer2 += 1
                            self.lblScore.setText(
                                f"{self.scorePlayer1} : {self.scorePlayer2}")
                            self.resetGame()
                        # check if someone won
                        elif self.checkIfWon() == 1:
                            if self.round == 0:
                                self.scorePlayer2 += 1
                            else:
                                self.scorePlayer1 += 1
                            self.lblScore.setText(
                                f"{self.scorePlayer1} : {self.scorePlayer2}")
                            self.resetGame()
                    else:
                        # check to see if the other player is winning
                        # if he is, block him
                        # if he is not, try to win
                        if self.theOtherPlayerIsWinning() != (-1, -1):
                            # block the other player
                            print("block the other player")
                            (linie, coloana) = self.theOtherPlayerIsWinning()
                            self.whereRobotPutY(linie, coloana)
                            self.matrixVal[linie, coloana] = self.round
                            self.round = (self.round+1) % 2
                            print(self.matrixVal)
                            if self.checkIfDraw() == 1 and self.checkIfWon() == 0:
                                self.scorePlayer1 += 1
                                self.scorePlayer2 += 1
                                self.lblScore.setText(
                                    f"{self.scorePlayer1} : {self.scorePlayer2}")
                                self.resetGame()
                            # check if someone won
                            elif self.checkIfWon() == 1:
                                if self.round == 0:
                                    self.scorePlayer2 += 1
                                else:
                                    self.scorePlayer1 += 1
                                self.lblScore.setText(
                                    f"{self.scorePlayer1} : {self.scorePlayer2}")
                                self.resetGame()
                        else:
                            if self.iAmWinning() != (-1, -1):
                                # i am winning
                                print("i am winning")
                                (linie, coloana) = self.iAmWinning()
                                self.whereRobotPutY(linie, coloana)
                                self.matrixVal[linie, coloana] = self.round
                                self.round = (self.round+1) % 2
                                print(self.matrixVal)
                                if self.checkIfDraw() == 1 and self.checkIfWon() == 0:
                                    self.scorePlayer1 += 1
                                    self.scorePlayer2 += 1
                                    self.lblScore.setText(
                                        f"{self.scorePlayer1} : {self.scorePlayer2}")
                                    self.resetGame()
                                # check if someone won
                                elif self.checkIfWon() == 1:

                                    if self.round == 0:
                                        self.scorePlayer2 += 1
                                    else:
                                        self.scorePlayer1 += 1
                                    self.lblScore.setText(
                                        f"{self.scorePlayer1} : {self.scorePlayer2}")
                                    self.resetGame()
                            else:
                                # this is temporary
                                # choose a random move
                                self.board = {1: self.matrixVal[0, 0], 2: self.matrixVal[0, 1], 3: self.matrixVal[0, 2], 4: self.matrixVal[1, 0],
                                              5: self.matrixVal[1, 1], 6: self.matrixVal[1, 2], 7: self.matrixVal[2, 0], 8: self.matrixVal[2, 1], 9: self.matrixVal[2, 2]}
                                self.printBoard()
                                print(self.spaceIsFree(1))
                                print(self.spaceIsFree(2))
                                self.compMove()
                                print(self.board)
                                if self.board[1] == 1 and self.matrixVal[0, 0] != 1:
                                    self.matrixVal[0, 0] = self.board[1]
                                    self.whereRobotPutY(0, 0)
                                elif self.board[2] == 1 and self.matrixVal[0, 1] != 1:
                                    self.matrixVal[0, 1] = self.board[2]
                                    self.whereRobotPutY(0, 1)
                                elif self.board[3] == 1 and self.matrixVal[0, 2] != 1:
                                    self.matrixVal[0, 2] = self.board[3]
                                    self.whereRobotPutY(0, 2)
                                elif self.board[4] == 1 and self.matrixVal[1, 0] != 1:
                                    self.matrixVal[1, 0] = self.board[4]
                                    self.whereRobotPutY(1, 0)
                                elif self.board[5] == 1 and self.matrixVal[1, 1] != 1:
                                    self.matrixVal[1, 1] = self.board[5]
                                    self.whereRobotPutY(1, 1)
                                elif self.board[6] == 1 and self.matrixVal[1, 2] != 1:
                                    self.matrixVal[1, 2] = self.board[6]
                                    self.whereRobotPutY(1, 2)
                                elif self.board[7] == 1 and self.matrixVal[2, 0] != 1:
                                    self.matrixVal[2, 0] = self.board[7]
                                    self.whereRobotPutY(2, 0)
                                elif self.board[8] == 1 and self.matrixVal[2, 1] != 1:
                                    self.matrixVal[2, 1] = self.board[8]
                                    self.whereRobotPutY(2, 1)
                                elif self.board[9] == 1 and self.matrixVal[2, 2] != 1:
                                    self.matrixVal[2, 2] = self.board[9]
                                    self.whereRobotPutY(2, 2)
                                self.round = (self.round+1) % 2

                                print(self.matrixVal)

    def spaceIsFree(self, position):
        if self.board[position] == -1:
            return True
        return False

    def compMove(self):
        self.bestScore = -1000
        self.bestMove = 0
        for key in self.board.keys():
            if self.board[key] == -1:
                self.board[key] = 1
                self.score = self.minimax(self.board, 0, False)
                self.board[key] = -1
                if self.score > self.bestScore:
                    self.bestScore = self.score
                    self.bestMove = key
        self.insertLetter(1, self.bestMove)

    def minimax(self, board, depth, isMaximizing):
        if self.checkWhichMarkWon(1):
            return 100
        elif self.checkWhichMarkWon(0):
            return -100
        elif self.checkDraw():
            return 0

        if isMaximizing:
            bestScore = -1000

            for key in board.keys():
                if board[key] == -1:
                    board[key] = 1
                    score = self.minimax(board, 0, False)
                    board[key] = -1
                    if score > bestScore:
                        bestScore = score
            return bestScore
        else:
            bestScore = 1000
            for key in board.keys():
                if board[key] == -1:
                    board[key] = 0
                    score = self.minimax(board, 0, True)
                    board[key] = -1
                    if score < bestScore:
                        bestScore = self.score
            return bestScore

    def insertLetter(self, letter, position):
        if self.spaceIsFree(position):
            self.board[position] = letter
            self.printBoard()
            if self.checkDraw() and self.checkForWin() == False:
                print("Draw")
                exit()
            if self.checkForWin():
                if letter == 0:
                    print("Player 1 won")
                    exit()
                else:
                    print("Bot won")
                    exit()
            return
        else:
            print("Space is not free")
            exit()

    def checkDraw(self):
        for i in self.board.keys():
            if self.board[i] == -1:
                return False
        return True

    def checkForWin(self):
        if self.board[1] == self.board[2] == self.board[3] and self.board[1] != -1:
            return True
        if self.board[4] == self.board[5] == self.board[6] and self.board[4] != -1:
            return True
        if self.board[7] == self.board[8] == self.board[9] and self.board[7] != -1:
            return True
        if self.board[1] == self.board[4] == self.board[7] and self.board[1] != -1:
            return True
        if self.board[2] == self.board[5] == self.board[8] and self.board[2] != -1:
            return True
        if self.board[3] == self.board[6] == self.board[9] and self.board[3] != -1:
            return True
        if self.board[1] == self.board[5] == self.board[9] and self.board[1] != -1:
            return True
        if self.board[3] == self.board[5] == self.board[7] and self.board[3] != -1:
            return True
        return False

    def checkWhichMarkWon(self, mark):
        if self.board[1] == self.board[2] == self.board[3] and self.board[1] != mark:
            return True
        if self.board[4] == self.board[5] == self.board[6] and self.board[4] != mark:
            return True
        if self.board[7] == self.board[8] == self.board[9] and self.board[7] != mark:
            return True
        if self.board[1] == self.board[4] == self.board[7] and self.board[1] != mark:
            return True
        if self.board[2] == self.board[5] == self.board[8] and self.board[2] != mark:
            return True
        if self.board[3] == self.board[6] == self.board[9] and self.board[3] != mark:
            return True
        if self.board[1] == self.board[5] == self.board[9] and self.board[1] != mark:
            return True
        if self.board[3] == self.board[5] == self.board[7] and self.board[3] != mark:
            return True
        return False

    def printBoard(self):
        print(str(self.board[1]) + '|' +
              str(self.board[2]) + '|' + str(self.board[3]))
        print('-----')
        print(str(self.board[4]) + '|' +
              str(self.board[5]) + '|' + str(self.board[6]))
        print('-----')
        print(str(self.board[7]) + '|' +
              str(self.board[8]) + '|' + str(self.board[9]))

    def iAmWinning(self):
        # if i have 2 in row or 2 in cols is wining
        # if i have 2 in diagonals is winning
        # check rows
        for i in range(3):
            if self.matrixVal[i, 0] == 1 and self.matrixVal[i, 1] == 1 and self.matrixVal[i, 2] == -1:
                return (i, 2)
            if self.matrixVal[i, 0] == 1 and self.matrixVal[i, 1] == -1 and self.matrixVal[i, 2] == 1:
                return (i, 1)
            if self.matrixVal[i, 0] == -1 and self.matrixVal[i, 1] == 1 and self.matrixVal[i, 2] == 1:
                return (i, 0)
        # check cols
        for i in range(3):
            if self.matrixVal[0, i] == 1 and self.matrixVal[1, i] == 1 and self.matrixVal[2, i] == -1:
                return (2, i)
            if self.matrixVal[0, i] == 1 and self.matrixVal[1, i] == -1 and self.matrixVal[2, i] == 1:
                return (1, i)
            if self.matrixVal[0, i] == -1 and self.matrixVal[1, i] == 1 and self.matrixVal[2, i] == 1:
                return (0, i)
        # check diagonals
        if self.matrixVal[0, 0] == 1 and self.matrixVal[1, 1] == 1 and self.matrixVal[2, 2] == -1:
            return (2, 2)
        if self.matrixVal[0, 0] == 1 and self.matrixVal[1, 1] == -1 and self.matrixVal[2, 2] == 1:
            return (1, 1)
        if self.matrixVal[0, 0] == -1 and self.matrixVal[1, 1] == 1 and self.matrixVal[2, 2] == 1:
            return (0, 0)
        if self.matrixVal[0, 2] == 1 and self.matrixVal[1, 1] == 1 and self.matrixVal[2, 0] == -1:
            return (2, 0)
        if self.matrixVal[0, 2] == 1 and self.matrixVal[1, 1] == -1 and self.matrixVal[2, 0] == 1:
            return (1, 1)
        if self.matrixVal[0, 2] == -1 and self.matrixVal[1, 1] == 1 and self.matrixVal[2, 0] == 1:
            return (0, 2)
        return (-1, -1)

    def theOtherPlayerIsWinning(self):
        # if he has 2 in row or 2 in cols is wining
        # if he has 2 in diagonals is winning
        # check rows
        for i in range(3):
            if self.matrixVal[i, 0] == 0 and self.matrixVal[i, 1] == 0 and self.matrixVal[i, 2] == -1:
                return (i, 2)
            if self.matrixVal[i, 0] == 0 and self.matrixVal[i, 1] == -1 and self.matrixVal[i, 2] == 0:
                return (i, 1)
            if self.matrixVal[i, 0] == -1 and self.matrixVal[i, 1] == 0 and self.matrixVal[i, 2] == 0:
                return (i, 0)
        # check cols
        for i in range(3):
            if self.matrixVal[0, i] == 0 and self.matrixVal[1, i] == 0 and self.matrixVal[2, i] == -1:
                return (2, i)
            if self.matrixVal[0, i] == 0 and self.matrixVal[1, i] == -1 and self.matrixVal[2, i] == 0:
                return (1, i)
            if self.matrixVal[0, i] == -1 and self.matrixVal[1, i] == 0 and self.matrixVal[2, i] == 0:
                return (0, i)
        # check diagonals
        if self.matrixVal[0, 0] == 0 and self.matrixVal[1, 1] == 0 and self.matrixVal[2, 2] == -1:
            return (2, 2)
        if self.matrixVal[0, 0] == 0 and self.matrixVal[1, 1] == -1 and self.matrixVal[2, 2] == 0:
            return (1, 1)
        if self.matrixVal[0, 0] == -1 and self.matrixVal[1, 1] == 0 and self.matrixVal[2, 2] == 0:
            return (0, 0)
        if self.matrixVal[0, 2] == 0 and self.matrixVal[1, 1] == 0 and self.matrixVal[2, 0] == -1:
            return (2, 0)
        if self.matrixVal[0, 2] == 0 and self.matrixVal[1, 1] == -1 and self.matrixVal[2, 0] == 0:
            return (1, 1)
        if self.matrixVal[0, 2] == -1 and self.matrixVal[1, 1] == 0 and self.matrixVal[2, 0] == 0:
            return (0, 2)
        return (-1, -1)

    def turnRandom(self):
        numbersOf0InMatrix = 0
        for i in range(3):
            for j in range(3):
                if self.matrixVal[i, j] == 0:
                    numbersOf0InMatrix += 1
        return (numbersOf0InMatrix % 2)

    def pickRandomNumber(self):

        while True:
            linie = random.randint(0, 2)
            coloana = random.randint(0, 2)
            if self.matrixVal[linie, coloana] == -1:
                break
        return (linie, coloana)

    def whereRobotPutY(self, linie, coloana):
        for i in range(3):
            for j in range(3):
                if i == linie and j == coloana:
                    if i == 0 and j == 0:
                        self.lbl00.setPixmap(QtGui.QPixmap(
                            "D:\\git\\GitHub\\ProiectPython\\venv\\0.png"))
                    elif i == 0 and j == 1:
                        self.lbl01.setPixmap(QtGui.QPixmap(
                            "D:\\git\\GitHub\\ProiectPython\\venv\\0.png"))
                    elif i == 0 and j == 2:
                        self.lbl02.setPixmap(QtGui.QPixmap(
                            "D:\\git\\GitHub\\ProiectPython\\venv\\0.png"))
                    elif i == 1 and j == 0:
                        self.lbl10.setPixmap(QtGui.QPixmap(
                            "D:\\git\\GitHub\\ProiectPython\\venv\\0.png"))
                    elif i == 1 and j == 1:
                        self.lbl11.setPixmap(QtGui.QPixmap(
                            "D:\\git\\GitHub\\ProiectPython\\venv\\0.png"))
                    elif i == 1 and j == 2:
                        self.lbl12.setPixmap(QtGui.QPixmap(
                            "D:\\git\\GitHub\\ProiectPython\\venv\\0.png"))
                    elif i == 2 and j == 0:
                        self.lbl20.setPixmap(QtGui.QPixmap(
                            "D:\\git\\GitHub\\ProiectPython\\venv\\0.png"))
                    elif i == 2 and j == 1:
                        self.lbl21.setPixmap(QtGui.QPixmap(
                            "D:\\git\\GitHub\\ProiectPython\\venv\\0.png"))
                    elif i == 2 and j == 2:
                        self.lbl22.setPixmap(QtGui.QPixmap(
                            "D:\\git\\GitHub\\ProiectPython\\venv\\0.png"))

    def checkIfDraw(self):
        for i in range(3):
            for j in range(3):
                if self.matrixVal[i, j] == -1:
                    return 0
        return 1

    def checkIfWon(self):
        # check if someone won
        for i in range(3):
            if self.matrixVal[i, 0] == self.matrixVal[i, 1] and self.matrixVal[i, 1] == self.matrixVal[i, 2] and self.matrixVal[i, 0] != -1:
                return 1
        for i in range(3):
            if self.matrixVal[0, i] == self.matrixVal[1, i] and self.matrixVal[1, i] == self.matrixVal[2, i] and self.matrixVal[0, i] != -1:
                return 1
        if self.matrixVal[0, 0] == self.matrixVal[1, 1] and self.matrixVal[1, 1] == self.matrixVal[2, 2] and self.matrixVal[0, 0] != -1:
            return 1
        if self.matrixVal[0, 2] == self.matrixVal[1, 1] and self.matrixVal[1, 1] == self.matrixVal[2, 0] and self.matrixVal[0, 2] != -1:
            return 1
        return 0

    def resetGame(self):
        self.matrixVal = np.full((3, 3), -1)
        self.lbl00.setPixmap(QtGui.QPixmap(""))
        self.lbl01.setPixmap(QtGui.QPixmap(""))
        self.lbl02.setPixmap(QtGui.QPixmap(""))
        self.lbl10.setPixmap(QtGui.QPixmap(""))
        self.lbl11.setPixmap(QtGui.QPixmap(""))
        self.lbl12.setPixmap(QtGui.QPixmap(""))
        self.lbl20.setPixmap(QtGui.QPixmap(""))
        self.lbl21.setPixmap(QtGui.QPixmap(""))
        self.lbl22.setPixmap(QtGui.QPixmap(""))
        # self.round = 0
        if self.typeOfGame == 1:
            print("i'm here 1")
            if self.round == 1:

                print("robot is starting")
                (linie, coloana) = self.pickRandomNumber()
                self.whereRobotPutY(linie, coloana)
                self.matrixVal[linie, coloana] = self.round
                self.round = (self.round+1) % 2
                print(self.matrixVal)
                if self.checkIfDraw() == 1 and self.checkIfWon() == 0:
                    self.scorePlayer1 += 1
                    self.scorePlayer2 += 1
                    self.lblScore.setText(
                        f"{self.scorePlayer1} : {self.scorePlayer2}")
                    self.resetGame()
                # check if someone won
                elif self.checkIfWon() == 1:
                    if self.round == 0:
                        self.scorePlayer2 += 1
                    else:
                        self.scorePlayer1 += 1
                    self.lblScore.setText(
                        f"{self.scorePlayer1} : {self.scorePlayer2}")
                    self.resetGame()
        else:
            print("i'm here 2")
            if self.round == 1:

                print("robot is starting")
                (linie, coloana) = (0, 0)
                self.whereRobotPutY(linie, coloana)
                self.matrixVal[linie, coloana] = self.round
                self.round = (self.round+1) % 2
                print(self.matrixVal)
                if self.checkIfDraw() == 1 and self.checkIfWon() == 0:
                    self.scorePlayer1 += 1
                    self.scorePlayer2 += 1
                    self.lblScore.setText(
                        f"{self.scorePlayer1} : {self.scorePlayer2}")
                    self.resetGame()
                # check if someone won
                elif self.checkIfWon() == 1:
                    if self.round == 0:
                        self.scorePlayer2 += 1
                    else:
                        self.scorePlayer1 += 1
                    self.lblScore.setText(
                        f"{self.scorePlayer1} : {self.scorePlayer2}")
                    self.resetGame()

    def setTypeOfGame(self, typeOfGame):
        self.typeOfGame = typeOfGame
        self.stackedWidget.setCurrentIndex(3)
        if typeOfGame != 0:
            self.name2 = "ROBOT"
        self.naming = str(self.name1) + " VS " + str(self.name2)

        self.lblNaming.setText(self.naming)
        print(self.naming)
        self.scorePlayer1 = 0
        self.scorePlayer2 = 0
        self.lblScore.setText(f"{self.scorePlayer1} : {self.scorePlayer2}")
        self.round = 0
        self.matrixVal = np.full((3, 3), -1)
        print(self.matrixVal)
        # x an 0 game (tic tac toe)
        print(self.typeOfGame)

        for i in range(3):
            for j in range(3):
                if (self.matrixVal[i][j] == -1):
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
        self.scorePlayer2 = 0
        self.scorePlayer1 = 0


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainView = QtWidgets.QMainWindow()
    ui = Ui_MainView()
    ui.setupUi(MainView)
    MainView.show()
    sys.exit(app.exec_())
