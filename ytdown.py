# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\izzet\OneDrive\Masaüstü\ytdown.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 303)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.baslik = QtWidgets.QLabel(self.centralwidget)
        self.baslik.setGeometry(QtCore.QRect(40, 10, 711, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.baslik.setFont(font)
        self.baslik.setAlignment(QtCore.Qt.AlignCenter)
        self.baslik.setObjectName("baslik")
        self.urlx = QtWidgets.QLineEdit(self.centralwidget)
        self.urlx.setGeometry(QtCore.QRect(130, 79, 621, 31))
        self.urlx.setObjectName("urlx")
        self.url = QtWidgets.QLabel(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(40, 80, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.url.setFont(font)
        self.url.setObjectName("url")
        self.p1080 = QtWidgets.QPushButton(self.centralwidget)
        self.p1080.setGeometry(QtCore.QRect(570, 200, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p1080.setFont(font)
        self.p1080.setObjectName("p1080")
        self.p720 = QtWidgets.QPushButton(self.centralwidget)
        self.p720.setGeometry(QtCore.QRect(450, 200, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p720.setFont(font)
        self.p720.setObjectName("p720")
        self.p360 = QtWidgets.QPushButton(self.centralwidget)
        self.p360.setGeometry(QtCore.QRect(330, 200, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p360.setFont(font)
        self.p360.setObjectName("p360")
        self.p144 = QtWidgets.QPushButton(self.centralwidget)
        self.p144.setGeometry(QtCore.QRect(210, 200, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p144.setFont(font)
        self.p144.setObjectName("p144")
        self.namex = QtWidgets.QLineEdit(self.centralwidget)
        self.namex.setGeometry(QtCore.QRect(210, 139, 541, 31))
        self.namex.setObjectName("namex")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(40, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.name.setFont(font)
        self.name.setObjectName("name")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.baslik.setText(_translate("MainWindow", "YouTube Video Downloader"))
        self.url.setText(_translate("MainWindow", "Url :"))
        self.p1080.setText(_translate("MainWindow", "1080p"))
        self.p720.setText(_translate("MainWindow", "720p"))
        self.p360.setText(_translate("MainWindow", "360p"))
        self.p144.setText(_translate("MainWindow", "144p"))
        self.name.setText(_translate("MainWindow", "Video Name :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
