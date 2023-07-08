from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import pyttsx3
import speedtest
from SpeedTestUi import Ui_SpeedTest

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

class SpeedTestThread(QThread):
    finished = pyqtSignal(int, int)
    error = pyqtSignal(str)

    def run(self):
        try:
            Speak("I am checking speed, please wait.")
            st = speedtest.Speedtest()
            download_bps = st.download()
            upload_bps = st.upload()
            download_mbps = download_bps / 1000000.0
            upload_mbps = upload_bps / 1000000.0
            Speak(f"Downloading speed is {download_mbps:.2f} megabits per second")
            Speak(f"Uploading speed is {upload_mbps:.2f} megabits per second")
            self.finished.emit(download_mbps, upload_mbps)
        except Exception as e:
            self.error.emit(str(e))

class SpeedTestWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_SpeedTest()
        self.ui.setupUi(self)

        # Set up the GIF animation
        self.gif = QMovie("C:\\Users\\Gagan\\Desktop\\BlackHole\\Complete NEO series\\DataBase\\Gui\\speedtest.gif")
        self.ui.gif.setMovie(self.gif)
        self.gif.start()

        self.thread = None

        self.ui.BtnStart.clicked.connect(self.startSpeedTest)
        self.ui.BtnStop.clicked.connect(self.stopSpeedTest)

    def startSpeedTest(self):
        if not self.thread:
            self.ui.BtnStart.setEnabled(False)
            self.ui.BtnStop.setEnabled(True)
            self.ui.StatusLbl.setText("Running speed test...")
            self.thread = SpeedTestThread()
            self.thread.finished.connect(self.showSpeedTestResults)
            self.thread.error.connect(self.showSpeedTestError)
            self.thread.start()

    def stopSpeedTest(self):
        if self.thread:
            self.ui.BtnStart.setEnabled(True)
            self.ui.BtnStop.setEnabled(False)
            self.ui.StatusLbl.setText("Speed test stopped.")
            self.thread.terminate()
            self.thread = None

    def showSpeedTestResults(self, download_mbps, upload_mbps):
        self.ui.BtnStart.setEnabled(True)
        self.ui.BtnStop.setEnabled(False)
        self.ui.StatusLbl.setText(f"Download: {download_mbps:.2f} Mbps | Upload: {upload_mbps:.2f} Mbps")
        self.thread = None

    def showSpeedTestError(self, error):
        self.ui.BtnStart.setEnabled(True)
        self.ui.BtnStop.setEnabled(False)
        self.ui.StatusLbl.setText(f"Error: {error}")
        self.thread = None

def Speak(audio):
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()

App = QApplication(sys.argv)
speedtest = SpeedTestWindow()
speedtest.show()
sys.exit(App.exec_())