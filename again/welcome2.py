# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcom.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from passcode2 import passcode
from administratorLogin2 import AdministratorLogin
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

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.resize(468, 296)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(46, 255, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(70, 120, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(38)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(330, 200, 121, 91))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../images/unnamed[1].png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(60, 200, 151, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 200, 151, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 81, 81))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("../../images/logo.jpg")))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_3.setText(_translate("Form", "Welcomes You", None))
        self.label_4.setText(_translate("Form", "FOOD COURT", None))
        self.label_5.setText(_translate("Form", "College of Engineering Chengannur", None))
        self.pushButton.setText(_translate("Form", "Administrator", None))
        self.pushButton_2.setText(_translate("Form", "User", None))
        self.pushButton_2.clicked.connect(self.call2)
        self.pushButton.clicked.connect(self.call1)


    def call2(self):
	self.close()
	self.win2=passcode()
	self.close()
	self.win2.show()



    def call1(self):
	self.close()
	self.win2=AdministratorLogin()
	self.close()
	self.win2.show()


