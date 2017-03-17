from PyQt4 import QtCore, QtGui
from placed import placed
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
r1 = " "
r2 = " "
r3 = " "
r4 = " "
class order(QtGui.QWidget):
    global r1
    def __init__(self):
        super(order,self).__init__()
        self.resize(468, 278)
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
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 281, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        
        self.commandLinkButton = QtGui.QCommandLinkButton(self)
        self.commandLinkButton.setGeometry(QtCore.QRect(310, 240, 141, 31))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.commandLinkButton2 = QtGui.QCommandLinkButton(self)
        self.commandLinkButton2.setGeometry(QtCore.QRect(20, 240, 111, 31))
        self.commandLinkButton2.setObjectName(_fromUtf8("commandLinkButton2"))
        self.commandLinkButton2.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lcdNumber = QtGui.QLCDNumber(self)
        self.lcdNumber.setGeometry(QtCore.QRect(180, 240, 71, 31))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.c1 = QtGui.QComboBox(self)
        self.c1.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.c1.setGeometry(QtCore.QRect(124, 70, 221, 27))
        self.c1.setObjectName(_fromUtf8("c1"))
        self.c1.addItem(_fromUtf8(""))
        self.c1.addItem(_fromUtf8(""))
        self.c1.addItem(_fromUtf8(""))
        self.c1.addItem(_fromUtf8(""))
        self.c1.addItem(_fromUtf8(""))
        self.c2 = QtGui.QComboBox(self)
        self.c2.setGeometry(QtCore.QRect(124, 110, 221, 27))
        self.c2.setObjectName(_fromUtf8("c2"))
        self.c2.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.c2.addItem(_fromUtf8(""))
        self.c2.addItem(_fromUtf8(""))
        self.c2.addItem(_fromUtf8(""))
        self.c2.addItem(_fromUtf8(""))
        self.c2.addItem(_fromUtf8(""))
        self.c3 = QtGui.QComboBox(self)
        self.c3.setGeometry(QtCore.QRect(124, 150, 221, 27))
        self.c3.setObjectName(_fromUtf8("c3"))
        self.c3.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.c3.addItem(_fromUtf8(""))
        self.c3.addItem(_fromUtf8(""))
        self.c3.addItem(_fromUtf8(""))
        self.c4 = QtGui.QComboBox(self)
        self.c4.setGeometry(QtCore.QRect(124, 190, 221, 27))
        self.c4.setObjectName(_fromUtf8("c4"))
        self.c4.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.c4.addItem(_fromUtf8(""))
        self.c4.addItem(_fromUtf8(""))
        self.c4.addItem(_fromUtf8(""))
        self.c4.addItem(_fromUtf8(""))
        self.c4.addItem(_fromUtf8(""))
        self.l3 = QtGui.QLabel(self)
        self.l3.setGeometry(QtCore.QRect(10, 70, 121, 31))
        self.l3.setObjectName(_fromUtf8("l3"))
        self.l3.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.l4 = QtGui.QLabel(self)
        self.l4.setGeometry(QtCore.QRect(10, 110, 121, 31))
        self.l4.setObjectName(_fromUtf8("l4"))
        self.l4.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.l5 = QtGui.QLabel(self)
        self.l5.setGeometry(QtCore.QRect(10, 150, 121, 31))
        self.l5.setObjectName(_fromUtf8("l5"))
        self.l5.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.l6 = QtGui.QLabel(self)
        self.l6.setGeometry(QtCore.QRect(10, 190, 121, 31))
        self.l6.setObjectName(_fromUtf8("l6"))
        self.l6.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.s1 = QtGui.QSpinBox(self)
        self.s1.setGeometry(QtCore.QRect(390, 70, 61, 27))
        self.s1.setObjectName(_fromUtf8("s1"))
        self.s1.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.s2 = QtGui.QSpinBox(self)
        self.s2.setGeometry(QtCore.QRect(390, 110, 61, 27))
        self.s2.setObjectName(_fromUtf8("s2"))
        self.s2.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.s3 = QtGui.QSpinBox(self)
        self.s3.setGeometry(QtCore.QRect(390, 150, 61, 27))
        self.s3.setObjectName(_fromUtf8("s3"))
        self.s3.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.s4 = QtGui.QSpinBox(self)
        self.s4.setGeometry(QtCore.QRect(390, 190, 61, 27))
        self.s4.setObjectName(_fromUtf8("s4"))
        self.s4.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.l2 = QtGui.QLabel(self)
        self.l2.setGeometry(QtCore.QRect(390, 40, 68, 17))
        self.l2.setObjectName(_fromUtf8("l2"))
        self.l2.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        
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
        self.commandLinkButton.clicked.connect(self.call2)
    def buttonclicked(self):
        global r1
        global r2
        global r3
        global r4
        r1=self.c1.currentText()
        r2=self.c2.currentText()
        r3=self.c3.currentText()
        r4=self.c4.currentText()
        n1=self.s1.value()
        n2=self.s2.value()
        n3=self.s3.value()
        n4=self.s4.value()
        print r1,n1,r2,n2,r3,n3,r4,n4 

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

   
    def call2(self):
	self.close()
	self.win2=placed()
	self.close()
	self.win2.show()




