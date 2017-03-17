# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administratorLogin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import time
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


var = " "
class Ui_Form(QtGui.QWidget):
    def __init__(self):
       QtGui.QWidget.__init__(self)
       self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(468, 296)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 10, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.p2 = QtGui.QPushButton(Form)
        self.p2.setGeometry(QtCore.QRect(200, 90, 41, 31))
        self.p2.setObjectName(_fromUtf8("p2"))
        self.p3 = QtGui.QPushButton(Form)
        self.p3.setGeometry(QtCore.QRect(290, 90, 41, 31))
        self.p3.setObjectName(_fromUtf8("p3"))
        self.cm1 = QtGui.QCommandLinkButton(Form)
        self.cm1.setGeometry(QtCore.QRect(270, 240, 101, 31))
        self.cm1.setObjectName(_fromUtf8("cm1"))
        self.p1 = QtGui.QPushButton(Form)
        self.p1.setGeometry(QtCore.QRect(110, 90, 41, 31))
        self.p1.setObjectName(_fromUtf8("p1"))
        self.p5 = QtGui.QPushButton(Form)
        self.p5.setGeometry(QtCore.QRect(200, 140, 41, 31))
        self.p5.setObjectName(_fromUtf8("p5"))
        self.cm2 = QtGui.QCommandLinkButton(Form)
        self.cm2.setGeometry(QtCore.QRect(80, 240, 81, 31))
        self.cm2.setObjectName(_fromUtf8("cm2"))
        self.p4 = QtGui.QPushButton(Form)
        self.p4.setGeometry(QtCore.QRect(110, 140, 41, 31))
        self.p4.setObjectName(_fromUtf8("p4"))
        self.p8 = QtGui.QPushButton(Form)
        self.p8.setGeometry(QtCore.QRect(200, 190, 41, 31))
        self.p8.setObjectName(_fromUtf8("p8"))
        self.p9 = QtGui.QPushButton(Form)
        self.p9.setGeometry(QtCore.QRect(290, 190, 41, 31))
        self.p9.setObjectName(_fromUtf8("p9"))
        self.p10 = QtGui.QPushButton(Form)
        self.p10.setGeometry(QtCore.QRect(200, 240, 41, 31))
        self.p10.setObjectName(_fromUtf8("p10"))
        self.p7 = QtGui.QPushButton(Form)
        self.p7.setGeometry(QtCore.QRect(110, 190, 41, 31))
        self.p7.setObjectName(_fromUtf8("p7"))
        self.p6 = QtGui.QPushButton(Form)
        self.p6.setGeometry(QtCore.QRect(290, 140, 41, 31))
        self.p6.setObjectName(_fromUtf8("p6"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(300, 30, 161, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "ENTER ADMISSION NUMBER:", None))
        self.p2.setText(_translate("Form", "2", None))
        self.p3.setText(_translate("Form", "3", None))
        self.cm1.setText(_translate("Form", "Confirm", None))
        self.p1.setText(_translate("Form", "1", None))
        self.p5.setText(_translate("Form", "5", None))
        self.cm2.setText(_translate("Form", "Clear", None))
        self.p4.setText(_translate("Form", "4", None))
        self.p8.setText(_translate("Form", "8", None))
        self.p9.setText(_translate("Form", "9", None))
        self.p10.setText(_translate("Form", "0", None))
        self.p7.setText(_translate("Form", "7", None))
        self.p6.setText(_translate("Form", "6", None))



        self.p1.clicked.connect(self.p1func)
        self.p2.clicked.connect(self.p2func)
        self.p3.clicked.connect(self.p3func)
        self.p4.clicked.connect(self.p4func)
        self.p5.clicked.connect(self.p5func)
        self.p6.clicked.connect(self.p6func)
        self.p7.clicked.connect(self.p7func)
        self.p8.clicked.connect(self.p8func)
        self.p9.clicked.connect(self.p9func)
        self.p10.clicked.connect(self.p10func)
        self.cm2.clicked.connect(self.clear)
        
    def clear(self):
	global var
	var=""	
	self.lineEdit.setText(var)        
    def p1func(self):
 	global var
	var=var+"1"
        self.lineEdit.setText(var)
    def p2func(self):
	global var
	var=var+"2"
        self.lineEdit.setText(var)
    def p3func(self):
	global var
	var=var+"3"
        self.lineEdit.setText(var)
    def p4func(self):
	global var
	var=var+"4"
        self.lineEdit.setText(var)
    def p5func(self):
	global var
	var=var+"5"
        self.lineEdit.setText(var)
    def p6func(self):
	global var
	var=var+"6"
        self.lineEdit.setText(var)
    def p7func(self):
	global var
	var=var+"7"
        self.lineEdit.setText(var)
    def p8func(self):
	global var
	var=var+"8"
        self.lineEdit.setText(var)
    def p9func(self):
	global var
	var=var+"9"
        self.lineEdit.setText(var)
    def p10func(self):
	global var
	var=var+"0"
        self.lineEdit.setText(var)

class Ui_Form2(QtGui.QWidget):
    def __init__(self):
       QtGui.QWidget.__init__(self)
       self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(468, 296)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(260, 220, 191, 16))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(250, 190, 201, 21))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.p4 = QtGui.QPushButton(Form)
        self.p4.setGeometry(QtCore.QRect(130, 160, 41, 31))
        self.p4.setObjectName(_fromUtf8("p4"))
        self.p5 = QtGui.QPushButton(Form)
        self.p5.setGeometry(QtCore.QRect(220, 160, 41, 31))
        self.p5.setObjectName(_fromUtf8("p5"))
        self.p6 = QtGui.QPushButton(Form)
        self.p6.setGeometry(QtCore.QRect(310, 160, 41, 31))
        self.p6.setObjectName(_fromUtf8("p6"))
        self.p9 = QtGui.QPushButton(Form)
        self.p9.setGeometry(QtCore.QRect(310, 210, 41, 31))
        self.p9.setObjectName(_fromUtf8("p9"))
        self.cm1 = QtGui.QCommandLinkButton(Form)
        self.cm1.setGeometry(QtCore.QRect(290, 260, 101, 31))
        self.cm1.setObjectName(_fromUtf8("cm1"))
        self.p7 = QtGui.QPushButton(Form)
        self.p7.setGeometry(QtCore.QRect(130, 210, 41, 31))
        self.p7.setObjectName(_fromUtf8("p7"))
        self.p3 = QtGui.QPushButton(Form)
        self.p3.setGeometry(QtCore.QRect(310, 110, 41, 31))
        self.p3.setObjectName(_fromUtf8("p3"))
        self.p8 = QtGui.QPushButton(Form)
        self.p8.setGeometry(QtCore.QRect(220, 210, 41, 31))
        self.p8.setObjectName(_fromUtf8("p8"))
        self.p1 = QtGui.QPushButton(Form)
        self.p1.setGeometry(QtCore.QRect(130, 110, 41, 31))
        self.p1.setObjectName(_fromUtf8("p1"))
        self.p2 = QtGui.QPushButton(Form)
        self.p2.setGeometry(QtCore.QRect(220, 110, 41, 31))
        self.p2.setObjectName(_fromUtf8("p2"))
        self.cm2 = QtGui.QCommandLinkButton(Form)
        self.cm2.setGeometry(QtCore.QRect(100, 260, 81, 31))
        self.cm2.setObjectName(_fromUtf8("cm2"))
        self.p10 = QtGui.QPushButton(Form)
        self.p10.setGeometry(QtCore.QRect(220, 260, 41, 31))
        self.p10.setObjectName(_fromUtf8("p10"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 70, 191, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_4.setText(_translate("Form", "Password:", None))
        self.label_2.setText(_translate("Form", "FOOD COURT", None))
        self.label.setText(_translate("Form", "College of Engineering,Chengannur", None))
        self.p4.setText(_translate("Form", "4", None))
        self.p5.setText(_translate("Form", "5", None))
        self.p6.setText(_translate("Form", "6", None))
        self.p9.setText(_translate("Form", "9", None))
        self.cm1.setText(_translate("Form", "Confirm", None))
        self.p7.setText(_translate("Form", "7", None))
        self.p3.setText(_translate("Form", "3", None))
        self.p8.setText(_translate("Form", "8", None))
        self.p1.setText(_translate("Form", "1", None))
        self.p2.setText(_translate("Form", "2", None))
        self.cm2.setText(_translate("Form", "Clear", None))
        self.p10.setText(_translate("Form", "0", None))


        self.p1.clicked.connect(self.p1func)
        self.p2.clicked.connect(self.p2func)
        self.p3.clicked.connect(self.p3func)
        self.p4.clicked.connect(self.p4func)
        self.p5.clicked.connect(self.p5func)
        self.p6.clicked.connect(self.p6func)
        self.p7.clicked.connect(self.p7func)
        self.p8.clicked.connect(self.p8func)
        self.p9.clicked.connect(self.p9func)
        self.p10.clicked.connect(self.p10func)
        self.cm2.clicked.connect(self.clear)
        

    def clear(self):
	global var
	var=""	
	self.lineEdit.setText(var)        
    def p1func(self):
 	global var
	var=var+"1"
        self.lineEdit.setText(var)
    def p2func(self):
	global var
	var=var+"2"
        self.lineEdit.setText(var)
    def p3func(self):
	global var
	var=var+"3"
        self.lineEdit.setText(var)
    def p4func(self):
	global var
	var=var+"4"
        self.lineEdit.setText(var)
    def p5func(self):
	global var
	var=var+"5"
        self.lineEdit.setText(var)
    def p6func(self):
	global var
	var=var+"6"
        self.lineEdit.setText(var)
    def p7func(self):
	global var
	var=var+"7"
        self.lineEdit.setText(var)
    def p8func(self):
	global var
	var=var+"8"
        self.lineEdit.setText(var)
    def p9func(self):
	global var
	var=var+"9"
        self.lineEdit.setText(var)
    def p10func(self):
	global var
	var=var+"0"
        self.lineEdit.setText(var)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    
    ex2 = Ui_Form2()
    ex2.show()
    sys.exit(app.exec_())

