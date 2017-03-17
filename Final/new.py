# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
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

class Ui_Form(QtGui.QWidget):
    def __init__(self):
       QtGui.QWidget.__init__(self)
       self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(468, 278)
        self.l1 = QtGui.QLabel(Form)
        self.l1.setGeometry(QtCore.QRect(0, 0, 301, 21))
        self.l1.setText(_fromUtf8(""))
        self.l1.setObjectName(_fromUtf8("l1"))
        self.p = QtGui.QPushButton(Form)
        self.p.setGeometry(QtCore.QRect(368, 240, 101, 31))
        self.p.setObjectName(_fromUtf8("p"))
        self.commandLinkButton = QtGui.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(220, 240, 141, 31))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.commandLinkButton2 = QtGui.QCommandLinkButton(Form)
        self.commandLinkButton2.setGeometry(QtCore.QRect(0, 240, 111, 31))
        self.commandLinkButton2.setObjectName(_fromUtf8("commandLinkButton2"))
        self.lcdNumber = QtGui.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(130, 240, 71, 31))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.c1 = QtGui.QComboBox(Form)
        self.c1.setGeometry(QtCore.QRect(124, 70, 221, 27))
        self.c1.setObjectName(_fromUtf8("c1"))
        self.c1.addItem(_fromUtf8(""))
        self.c1.addItem(_fromUtf8(""))
        self.c1.addItem(_fromUtf8(""))
        self.c1.addItem(_fromUtf8(""))
        self.c1.addItem(_fromUtf8(""))
        self.c2 = QtGui.QComboBox(Form)
        self.c2.setGeometry(QtCore.QRect(124, 110, 221, 27))
        self.c2.setObjectName(_fromUtf8("c2"))
        self.c2.addItem(_fromUtf8(""))
        self.c2.addItem(_fromUtf8(""))
        self.c2.addItem(_fromUtf8(""))
        self.c2.addItem(_fromUtf8(""))
        self.c2.addItem(_fromUtf8(""))
        self.c3 = QtGui.QComboBox(Form)
        self.c3.setGeometry(QtCore.QRect(124, 150, 221, 27))
        self.c3.setObjectName(_fromUtf8("c3"))
        self.c3.addItem(_fromUtf8(""))
        self.c3.addItem(_fromUtf8(""))
        self.c3.addItem(_fromUtf8(""))
        self.c4 = QtGui.QComboBox(Form)
        self.c4.setGeometry(QtCore.QRect(124, 190, 221, 27))
        self.c4.setObjectName(_fromUtf8("c4"))
        self.c4.addItem(_fromUtf8(""))
        self.c4.addItem(_fromUtf8(""))
        self.c4.addItem(_fromUtf8(""))
        self.c4.addItem(_fromUtf8(""))
        self.c4.addItem(_fromUtf8(""))
        self.l3 = QtGui.QLabel(Form)
        self.l3.setGeometry(QtCore.QRect(10, 70, 121, 31))
        self.l3.setObjectName(_fromUtf8("l3"))
        self.l4 = QtGui.QLabel(Form)
        self.l4.setGeometry(QtCore.QRect(10, 110, 121, 31))
        self.l4.setObjectName(_fromUtf8("l4"))
        self.l5 = QtGui.QLabel(Form)
        self.l5.setGeometry(QtCore.QRect(10, 150, 121, 31))
        self.l5.setObjectName(_fromUtf8("l5"))
        self.l6 = QtGui.QLabel(Form)
        self.l6.setGeometry(QtCore.QRect(10, 190, 121, 31))
        self.l6.setObjectName(_fromUtf8("l6"))
        self.s1 = QtGui.QSpinBox(Form)
        self.s1.setGeometry(QtCore.QRect(390, 70, 61, 27))
        self.s1.setObjectName(_fromUtf8("s1"))
        self.s2 = QtGui.QSpinBox(Form)
        self.s2.setGeometry(QtCore.QRect(390, 110, 61, 27))
        self.s2.setObjectName(_fromUtf8("s2"))
        self.s3 = QtGui.QSpinBox(Form)
        self.s3.setGeometry(QtCore.QRect(390, 150, 61, 27))
        self.s3.setObjectName(_fromUtf8("s3"))
        self.s4 = QtGui.QSpinBox(Form)
        self.s4.setGeometry(QtCore.QRect(390, 190, 61, 27))
        self.s4.setObjectName(_fromUtf8("s4"))
        self.l2 = QtGui.QLabel(Form)
        self.l2.setGeometry(QtCore.QRect(390, 40, 68, 17))
        self.l2.setObjectName(_fromUtf8("l2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.p.setText(_translate("Form", "Sign Out", None))
        self.commandLinkButton.setText(_translate("Form", "Confirm", None))
        self.commandLinkButton2.setText(_translate("Form", "Total", None))
        self.l3.setText(_translate("Form", "Rice Items", None))
        self.l4.setText(_translate("Form", "Curry", None))
        self.l5.setText(_translate("Form", "Beverages", None))
        self.l6.setText(_translate("Form", "Drinks", None))
        self.l2.setText(_translate("Form", "Quantity", None))
        self.c1.setItemText(0, _translate("Form", "Add Items", None))
        self.c1.setItemText(1, _translate("Form", "Meals ........35", None))
        self.c1.setItemText(2, _translate("Form", "Biriyani .....80", None))
        self.c1.setItemText(3, _translate("Form", "Idli ........5", None))
        self.c1.setItemText(4, _translate("Form", "Dosa .........5", None))
        self.c2.setItemText(0, _translate("Form", "Add Items", None))
        self.c2.setItemText(1, _translate("Form", "Chicken curry...20", None))
        self.c2.setItemText(2, _translate("Form", "Veg curry.......15", None))
        self.c2.setItemText(3, _translate("Form", "Egg masala......20", None))
        self.c3.setItemText(0, _translate("Form", "Add Items", None))
        self.c3.setItemText(1, _translate("Form", "Tea ........8", None))
        self.c3.setItemText(2, _translate("Form", "Coffee .....12", None))
        self.c4.setItemText(0, _translate("Form", "Add Items", None))
        self.c4.setItemText(1, _translate("Form", "Lime Juice ...15", None))
        self.c4.setItemText(2, _translate("Form", "Mango Juice ..15", None))
        self.c4.setItemText(3, _translate("Form", "7up ..........12", None))
        self.c4.setItemText(4, _translate("Form", "Lemon soda ...14", None))
        self.commandLinkButton.clicked.connect(self.buttonclicked)
        self.commandLinkButton2.clicked.connect(self.orderclick)
    def buttonclicked(self):
        t1=self.c1.currentText()
        t2=self.c2.currentText()
        t3=self.c3.currentText()
        t4=self.c4.currentText()
        n1=self.s1.value()
        n2=self.s2.value()
        n3=self.s3.value()
        n4=self.s4.value()
        print t1,n1 ,t2,n2,t3,n3,t4,n4 

    def orderclick(self):  
        t = 0
        t1 = 0
        t2 = 0       
        t3 = 0
        t4 = 0
        if str(self.c1.currentText()) == "Meals ........35":
            t1 = t1 + (self.s1.value())*35
        elif str(self.c1.currentText()) == "Biriyani .....80":
            t1 = t1 + (self.s1.value())*80
        elif str(self.c1.currentText()) == "Idali ........5": 
            t1 = t1 + (self.s1.value())*5
        elif str(self.c1.currentText()) == "Dosa .........5":
            t1 = t1 + (self.s1.value())*5
       
        if str(self.c2.currentText()) == "Chicken curry...20":
            t2 = t2 + (self.s2.value())*20
        elif str(self.c2.currentText()) == "Veg curry.......15":
            t2 = t2 + (self.s2.value())*15  
        elif str(self.c2.currentText()) == "Egg masala......20":
            t2 = t2 + (self.s2.value())*20

        if str(self.c3.currentText()) == "Tea ........8":
            t3 = t3 + (self.s3.value())*8
        elif str(self.c3.currentText()) == "Coffee .....12":
            t3 = t3 + (self.s3.value())*12

        if str(self.c4.currentText()) == "Lime Juice ...15":
            t4 = t4 + (self.s4.value())*15
        elif str(self.c4.currentText()) == "Mango Juice ..15":
            t4 = t4 + (self.s4.value())*15
        elif str(self.c4.currentText()) == "7up ..........12":
            t4 = t4 + (self.s4.value())*12
        elif str(self.c4.currentText()) == "Lemon soda ...14": 
            t4 = t4 + (self.s4.value())*14
        t = t1 + t2 + t3 + t4

        print t
        self.lcdNumber.display(t)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


