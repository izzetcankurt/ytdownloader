from PyQt5 import QtWidgets
from ytdown import Ui_MainWindow
from pytube import YouTube

class Program(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.p144.clicked.connect(self.f144)
        self.p360.clicked.connect(self.f360)
        self.p720.clicked.connect(self.f720)
        self.p1080.clicked.connect(self.f1080)

    def f144(self):
        try:
            self.yt = YouTube(str(self.urlx.text()))
            x = self.yt.streams.get_by_resolution("144p")
            x.download(filename=self.namex.text() + "_" + "144p" + ".mp4")
        except:
            print("Problem!")

    def f360(self):
        try:
            self.yt = YouTube(str(self.urlx.text()))
            x = self.yt.streams.get_by_resolution("360p")
            x.download(filename=self.namex.text() + "_" + "360p" + ".mp4")
        except:
            print("Problem!")
    def f720(self):
        try:
            self.yt = YouTube(str(self.urlx.text()))
            x = self.yt.streams.get_by_resolution("720p")
            x.download(filename=self.namex.text() + "_" + "720p" + ".mp4")
        except:
            print("Problem!")
    def f1080(self):
        try:
            self.yt = YouTube(str(self.urlx.text()))
            x = self.yt.streams.get_by_resolution("1080p")
            x.download(filename=self.namex.text() + "_" + "1080p" + ".mp4")
        except:
            print("Problem!")