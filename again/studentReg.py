# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentReg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
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

class Ui_stdntreg(QtGui.QWidget):
    def __init__(self):
       QtGui.QWidget.__init__(self)
       self.setupUi(self)
    def setupUi(self, stdntreg):
        stdntreg.setObjectName(_fromUtf8("stdntreg"))
        stdntreg.resize(468, 296)
        self.label = QtGui.QLabel(stdntreg)
        self.label.setGeometry(QtCore.QRect(90, 20, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(stdntreg)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 68, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(stdntreg)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 68, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(stdntreg)
        self.label_4.setGeometry(QtCore.QRect(60, 170, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(stdntreg)
        self.label_5.setGeometry(QtCore.QRect(60, 210, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit = QtGui.QLineEdit(stdntreg)
        self.lineEdit.setGeometry(QtCore.QRect(250, 90, 191, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(stdntreg)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 130, 191, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(stdntreg)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 170, 191, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(stdntreg)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 210, 191, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))

        self.retranslateUi(stdntreg)
        QtCore.QMetaObject.connectSlotsByName(stdntreg)

    def retranslateUi(self, stdntreg):
        stdntreg.setWindowTitle(_translate("stdntreg", "Form", None))
        self.label.setText(_translate("stdntreg", "STUDENT REGISTRATION", None))
        self.label_2.setText(_translate("stdntreg", "NAME:", None))
        self.label_3.setText(_translate("stdntreg", "BATCH:", None))
        self.label_4.setText(_translate("stdntreg", "ADMISSION NO:", None))
        self.label_5.setText(_translate("stdntreg", "FINGERPRINT:", None))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_stdntreg()
    ex.show()
    sys.exit(app.exec_())

