# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shorttermtrader.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(400, 250)
        mainWindow.setMinimumSize(QtCore.QSize(400, 250))
        mainWindow.setMaximumSize(QtCore.QSize(400, 250))
        mainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 10, 240, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.lrButton = QtWidgets.QPushButton(self.centralwidget)
        self.lrButton.setGeometry(QtCore.QRect(210, 100, 101, 31))
        self.lrButton.setObjectName("lrButton")
        self.svrButton = QtWidgets.QPushButton(self.centralwidget)
        self.svrButton.setGeometry(QtCore.QRect(210, 160, 101, 31))
        self.svrButton.setObjectName("svrButton")
        self.saveLR = QtWidgets.QPushButton(self.centralwidget)
        self.saveLR.setGeometry(QtCore.QRect(90, 100, 101, 31))
        self.saveLR.setObjectName("saveLR")
        self.saveSVR = QtWidgets.QPushButton(self.centralwidget)
        self.saveSVR.setGeometry(QtCore.QRect(90, 160, 101, 31))
        self.saveSVR.setObjectName("saveSVR")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen = QtWidgets.QAction(mainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClear = QtWidgets.QAction(mainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionHelp = QtWidgets.QAction(mainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionHelp)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Short-Term Trader"))
        self.textBrowser.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ba0003;\">Short-Term Trader</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ba0003;\">Joshua Yun</span></p></body></html>"))
        self.lrButton.setText(_translate("mainWindow", "Linear Regression"))
        self.svrButton.setText(_translate("mainWindow", "Support VR"))
        self.saveLR.setText(_translate("mainWindow", "Save"))
        self.saveSVR.setText(_translate("mainWindow", "Save"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.actionExit.setText(_translate("mainWindow", "Exit"))
        self.actionOpen.setText(_translate("mainWindow", "Open"))
        self.actionClear.setText(_translate("mainWindow", "Clear Data"))
        self.actionHelp.setText(_translate("mainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

