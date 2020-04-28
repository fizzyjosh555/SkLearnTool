# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LRDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class SupportVRSetup(object):
    def svrSetupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(161, 400)
        Dialog.setMinimumSize(QtCore.QSize(161, 400))
        Dialog.setMaximumSize(QtCore.QSize(161, 400))

        self.svrRunButton = QtWidgets.QPushButton(Dialog)
        self.svrRunButton.setGeometry(QtCore.QRect(10, 350, 141, 31))
        self.svrRunButton.setObjectName("svrRunButton")

        self.svrKernelInput = QtWidgets.QLineEdit(Dialog)
        self.svrKernelInput.setGeometry(QtCore.QRect(80, 20, 71, 20))
        self.svrKernelInput.setMaxLength(15)
        self.svrKernelInput.setObjectName("svrKernelInput")

        self.svrKernelLabel = QtWidgets.QLabel(Dialog)
        self.svrKernelLabel.setGeometry(QtCore.QRect(40, 20, 71, 20))
        self.svrKernelLabel.setObjectName("svrKernelLabel")

        self.svrDegreeLabel = QtWidgets.QLabel(Dialog)
        self.svrDegreeLabel.setGeometry(QtCore.QRect(35, 50, 50, 20))
        self.svrDegreeLabel.setObjectName("svrDegreeLabel")

        self.svrDegreeInput = QtWidgets.QLineEdit(Dialog)
        self.svrDegreeInput.setGeometry(QtCore.QRect(80, 50, 71, 20))
        self.svrDegreeInput.setMaxLength(2)
        self.svrDegreeInput.setObjectName("svrDegreeInput")

        self.svrGammaLabel = QtWidgets.QLabel(Dialog)
        self.svrGammaLabel.setGeometry(QtCore.QRect(35, 80, 50, 20))
        self.svrGammaLabel.setObjectName("svrGammaLabel")

        self.svrGammaInput = QtWidgets.QLineEdit(Dialog)
        self.svrGammaInput.setGeometry(QtCore.QRect(80, 80, 71, 20))
        self.svrGammaInput.setMaxLength(10)
        self.svrGammaInput.setObjectName("svrGammaInput")

        self.svrCoefInput = QtWidgets.QLineEdit(Dialog)
        self.svrCoefInput.setGeometry(QtCore.QRect(80, 110, 71, 20))
        self.svrCoefInput.setMaxLength(10)
        self.svrCoefInput.setObjectName("svrCoefInput")

        self.svrCoefLabel = QtWidgets.QLabel(Dialog)
        self.svrCoefLabel.setGeometry(QtCore.QRect(42, 110, 50, 20))
        self.svrCoefLabel.setObjectName("svrCoefLabel")

        self.svrTolInput = QtWidgets.QLineEdit(Dialog)
        self.svrTolInput.setGeometry(QtCore.QRect(80, 140, 71, 20))
        self.svrTolInput.setMaxLength(10)
        self.svrTolInput.setObjectName("svrTolInput")

        self.svrTolLabel = QtWidgets.QLabel(Dialog)
        self.svrTolLabel.setGeometry(QtCore.QRect(57, 140, 50, 20))
        self.svrTolLabel.setObjectName("svrTolLabel")

        self.svrCLabel = QtWidgets.QLabel(Dialog)
        self.svrCLabel.setGeometry(QtCore.QRect(61, 170, 50, 20))
        self.svrCLabel.setObjectName("svrCLabel")

        self.svrShrinkLabel = QtWidgets.QLabel(Dialog)
        self.svrShrinkLabel.setGeometry(QtCore.QRect(26, 200, 50, 20))
        self.svrShrinkLabel.setObjectName("svrShrinkLabel")

        self.svrCacheLabel = QtWidgets.QLabel(Dialog)
        self.svrCacheLabel.setGeometry(QtCore.QRect(16, 230, 61, 20))
        self.svrCacheLabel.setObjectName("svrCacheLabel")

        self.svrVerbLabel = QtWidgets.QLabel(Dialog)
        self.svrVerbLabel.setGeometry(QtCore.QRect(29, 260, 50, 20))
        self.svrVerbLabel.setObjectName("svrVerbLabel")

        self.svrIterLabel = QtWidgets.QLabel(Dialog)
        self.svrIterLabel.setGeometry(QtCore.QRect(26, 290, 50, 20))
        self.svrIterLabel.setObjectName("svrIterLabel")

        self.svrCInput = QtWidgets.QLineEdit(Dialog)
        self.svrCInput.setGeometry(QtCore.QRect(80, 170, 71, 20))
        self.svrCInput.setMaxLength(10)
        self.svrCInput.setObjectName("svrCInput")

        self.svrShrinkInput = QtWidgets.QLineEdit(Dialog)
        self.svrShrinkInput.setGeometry(QtCore.QRect(80, 200, 71, 20))
        self.svrShrinkInput.setMaxLength(10)
        self.svrShrinkInput.setObjectName("svrShrinkInput")

        self.svrCacheInput = QtWidgets.QLineEdit(Dialog)
        self.svrCacheInput.setGeometry(QtCore.QRect(80, 230, 71, 20))
        self.svrCacheInput.setMaxLength(10)
        self.svrCacheInput.setObjectName("svrCacheInput")

        self.svrVerbInput = QtWidgets.QLineEdit(Dialog)
        self.svrVerbInput.setGeometry(QtCore.QRect(80, 260, 71, 20))
        self.svrVerbInput.setMaxLength(10)
        self.svrVerbInput.setObjectName("svrVerbInput")

        self.svrIterInput = QtWidgets.QLineEdit(Dialog)
        self.svrIterInput.setGeometry(QtCore.QRect(80, 290, 71, 20))
        self.svrIterInput.setMaxLength(10)
        self.svrIterInput.setObjectName("svrIterInput")

        self.svrDaysInput = QtWidgets.QLineEdit(Dialog)
        self.svrDaysInput.setGeometry(QtCore.QRect(80, 320, 71, 20))
        self.svrDaysInput.setMaxLength(10)
        self.svrDaysInput.setObjectName("svrDaysInput")

        self.svrDaysLabel = QtWidgets.QLabel(Dialog)
        self.svrDaysLabel.setGeometry(QtCore.QRect(44, 320, 50, 20))
        self.svrDaysLabel.setObjectName("svrDaysLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SVR"))
        self.svrRunButton.setText(_translate("Dialog", "Run"))
        self.svrKernelLabel.setText(_translate("Dialog", "kernel:"))
        self.svrDegreeLabel.setText(_translate("Dialog", "degree:"))
        self.svrGammaLabel.setText(_translate("Dialog", "gamma:"))
        self.svrCoefLabel.setText(_translate("Dialog", "coef0:"))
        self.svrTolLabel.setText(_translate("Dialog", "tol:"))
        self.svrCLabel.setText(_translate("Dialog", "C:"))
        self.svrShrinkLabel.setText(_translate("Dialog", "shrinking:"))
        self.svrCacheLabel.setText(_translate("Dialog", "cache_size:"))
        self.svrVerbLabel.setText(_translate("Dialog", "verbose:"))
        self.svrIterLabel.setText(_translate("Dialog", "max_iter:"))
        self.svrDaysLabel.setText(_translate("Dialog", "Days:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = SupportVRSetup()
    ui.svrSetupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

