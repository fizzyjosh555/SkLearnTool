# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LRDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(162, 219)
        self.lrRunButton = QtWidgets.QPushButton(Dialog)
        self.lrRunButton.setGeometry(QtCore.QRect(10, 170, 141, 31))
        self.lrRunButton.setObjectName("lrRunButton")
        self.lrFitInput = QtWidgets.QLineEdit(Dialog)
        self.lrFitInput.setGeometry(QtCore.QRect(80, 20, 71, 20))
        self.lrFitInput.setText("")
        self.lrFitInput.setMaxLength(5)
        self.lrFitInput.setObjectName("lrFitInput")
        self.lrFitLabel = QtWidgets.QLabel(Dialog)
        self.lrFitLabel.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.lrFitLabel.setObjectName("lrFitLabel")
        self.lrNormLabel = QtWidgets.QLabel(Dialog)
        self.lrNormLabel.setGeometry(QtCore.QRect(24, 50, 50, 20))
        self.lrNormLabel.setObjectName("lrNormLabel")
        self.lrNormInput = QtWidgets.QLineEdit(Dialog)
        self.lrNormInput.setGeometry(QtCore.QRect(80, 50, 71, 20))
        self.lrNormInput.setMaxLength(5)
        self.lrNormInput.setObjectName("lrNormInput")
        self.lrCopyLabel = QtWidgets.QLabel(Dialog)
        self.lrCopyLabel.setGeometry(QtCore.QRect(34, 80, 50, 20))
        self.lrCopyLabel.setObjectName("lrCopyLabel")
        self.lrCopyInput = QtWidgets.QLineEdit(Dialog)
        self.lrCopyInput.setGeometry(QtCore.QRect(80, 80, 71, 20))
        self.lrCopyInput.setMaxLength(5)
        self.lrCopyInput.setObjectName("lrCopyInput")
        self.lrJobsInput = QtWidgets.QLineEdit(Dialog)
        self.lrJobsInput.setGeometry(QtCore.QRect(80, 110, 71, 20))
        self.lrJobsInput.setToolTip("")
        self.lrJobsInput.setStatusTip("")
        self.lrJobsInput.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lrJobsInput.setObjectName("lrJobsInput")
        self.lrJobsLabel = QtWidgets.QLabel(Dialog)
        self.lrJobsLabel.setGeometry(QtCore.QRect(37, 110, 50, 20))
        self.lrJobsLabel.setObjectName("lrJobsLabel")
        self.lrDaysInput = QtWidgets.QLineEdit(Dialog)
        self.lrDaysInput.setGeometry(QtCore.QRect(80, 140, 71, 20))
        self.lrDaysInput.setToolTip("")
        self.lrDaysInput.setStatusTip("")
        self.lrDaysInput.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lrDaysInput.setObjectName("lrDaysInput")
        self.lrDaysLabel = QtWidgets.QLabel(Dialog)
        self.lrDaysLabel.setGeometry(QtCore.QRect(39, 140, 50, 20))
        self.lrDaysLabel.setObjectName("lrDaysLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LR"))
        self.lrRunButton.setText(_translate("Dialog", "Run"))
        self.lrFitLabel.setText(_translate("Dialog", "fit_intercept:"))
        self.lrNormLabel.setText(_translate("Dialog", "normalize:"))
        self.lrCopyLabel.setText(_translate("Dialog", "copy_X:"))
        self.lrJobsLabel.setText(_translate("Dialog", "n_jobs:"))
        self.lrDaysLabel.setText(_translate("Dialog", "  Days:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

