from PyQt5 import QtCore, QtGui, QtWidgets

class LinearRegressionSetup(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(162, 190)
        self.lrRunButton = QtWidgets.QPushButton(Dialog)
        self.lrRunButton.setGeometry(QtCore.QRect(10, 140, 141, 31))
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
        self.lrJobsInput.setMaxLength(3)
        self.lrJobsInput.setObjectName("lrJobsInput")
        self.lrJobsLabel = QtWidgets.QLabel(Dialog)
        self.lrJobsLabel.setGeometry(QtCore.QRect(37, 110, 50, 20))
        self.lrJobsLabel.setObjectName("lrJobsLabel")

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


