from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from NeoUi import Ui_MainWindow
import sys
import Main

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        Main.TaskExe()

startFunctions = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.neo_ui = Ui_MainWindow()
        self.neo_ui.setupUi(self)
        self.neo_ui.pushButton.clicked.connect(self.startFunc)
        self.neo_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):
        self.movies = QtGui.QMovie("DataBase/Gui/VoiceReg/Siri_1.gif")
        self.neo_ui.gif.setMovie(self.movies)
        self.movies.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startFunctions.start()

    def showtime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString("hh:mm:ss")
        labbel = " Time :  " + label_time
        self.neo_ui.textBrowser.setText(labbel)

Gui_App = QApplication(sys.argv)
Gui_Neo = Gui_Start()
Gui_Neo.show()
exit(Gui_App.exec_())