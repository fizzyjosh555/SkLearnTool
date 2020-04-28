# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LRDialogedit.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(161, 220)
        self.lrRunButton = QtWidgets.QPushButton(Dialog)
        self.lrRunButton.setGeometry(QtCore.QRect(10, 170, 141, 31))
        self.lrRunButton.setObjectName("lrRunButton")
        self.svrKernelInput = QtWidgets.QLineEdit(Dialog)
        self.svrKernelInput.setGeometry(QtCore.QRect(80, 20, 71, 20))
        self.svrKernelInput.setText("")
        self.svrKernelInput.setMaxLength(5)
        self.svrKernelInput.setObjectName("svrKernelInput")
        self.svrKernelLabel = QtWidgets.QLabel(Dialog)
        self.svrKernelLabel.setGeometry(QtCore.QRect(40, 20, 71, 20))
        self.svrKernelLabel.setObjectName("svrKernelLabel")
        self.svrDegreeLabel = QtWidgets.QLabel(Dialog)
        self.svrDegreeLabel.setGeometry(QtCore.QRect(35, 50, 50, 20))
        self.svrDegreeLabel.setObjectName("svrDegreeLabel")
        self.svrDegreeInput = QtWidgets.QLineEdit(Dialog)
        self.svrDegreeInput.setGeometry(QtCore.QRect(80, 50, 71, 20))
        self.svrDegreeInput.setMaxLength(5)
        self.svrDegreeInput.setObjectName("svrDegreeInput")
        self.svrGammaLabel = QtWidgets.QLabel(Dialog)
        self.svrGammaLabel.setGeometry(QtCore.QRect(35, 80, 50, 20))
        self.svrGammaLabel.setMinimumSize(QtCore.QSize(50, 20))
        self.svrGammaLabel.setMaximumSize(QtCore.QSize(50, 20))
        self.svrGammaLabel.setObjectName("svrGammaLabel")
        self.svrGammaInput = QtWidgets.QLineEdit(Dialog)
        self.svrGammaInput.setGeometry(QtCore.QRect(80, 80, 71, 20))
        self.svrGammaInput.setMaxLength(5)
        self.svrGammaInput.setObjectName("svrGammaInput")
        self.svrCoefInput = QtWidgets.QLineEdit(Dialog)
        self.svrCoefInput.setGeometry(QtCore.QRect(80, 110, 71, 20))
        self.svrCoefInput.setToolTip("")
        self.svrCoefInput.setStatusTip("")
        self.svrCoefInput.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.svrCoefInput.setObjectName("svrCoefInput")
        self.svrCoefLabel = QtWidgets.QLabel(Dialog)
        self.svrCoefLabel.setGeometry(QtCore.QRect(42, 110, 50, 20))
        self.svrCoefLabel.setObjectName("svrCoefLabel")
        self.svrTolInput = QtWidgets.QLineEdit(Dialog)
        self.svrTolInput.setGeometry(QtCore.QRect(80, 140, 71, 20))
        self.svrTolInput.setToolTip("")
        self.svrTolInput.setStatusTip("")
        self.svrTolInput.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.svrTolInput.setObjectName("svrTolInput")
        self.svrTolLabel = QtWidgets.QLabel(Dialog)
        self.svrTolLabel.setGeometry(QtCore.QRect(57, 140, 50, 20))
        self.svrTolLabel.setObjectName("svrTolLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SVR"))
        self.lrRunButton.setText(_translate("Dialog", "Run"))
        self.svrKernelLabel.setText(_translate("Dialog", "kernel:"))
        self.svrDegreeLabel.setText(_translate("Dialog", "degree:"))
        self.svrGammaLabel.setText(_translate("Dialog", "gamma:"))
        self.svrCoefLabel.setText(_translate("Dialog", "coef0:"))
        self.svrTolLabel.setText(_translate("Dialog", "tol:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

