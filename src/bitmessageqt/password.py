# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_passwordDialog(object):
    def setupUi(self, passwordDialog):
        passwordDialog.setObjectName(_fromUtf8("passwordDialog"))
        passwordDialog.resize(291, 120)
        self.gridLayout = QtGui.QGridLayout(passwordDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(passwordDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 4, 2)
        self.passwordInput = QtGui.QLineEdit(passwordDialog)
        self.passwordInput.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.passwordInput.setMaxLength(100)
        self.passwordInput.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordInput.setObjectName(_fromUtf8("passwordInput"))
        self.gridLayout.addWidget(self.passwordInput, 5, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(passwordDialog)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Abort|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 1, 1, 1)

        self.retranslateUi(passwordDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), passwordDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), passwordDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(passwordDialog)

    def retranslateUi(self, passwordDialog):
        passwordDialog.setWindowTitle(_translate("passwordDialog", "Bitmessage", None))
        self.label.setText(_translate("passwordDialog", "Enter your passphrase : ", None))

