# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'placed.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class placed(QtGui.QWidget):
    
    def __init__(self):

        super(placed,self).__init__()
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
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 20, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(160, 60, 221, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit2 = QtGui.QLineEdit(self)
        self.lineEdit2.setGeometry(QtCore.QRect(160, 100, 221, 27))
        self.lineEdit2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit3 = QtGui.QLineEdit(self)
        self.lineEdit3.setGeometry(QtCore.QRect(160, 140, 221, 27))
        self.lineEdit3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit4 = QtGui.QLineEdit(self)
        self.lineEdit4.setGeometry(QtCore.QRect(160, 180, 221, 27))
        self.lineEdit4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 240, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lcdNumber = QtGui.QLCDNumber(self)
        self.lcdNumber.setGeometry(QtCore.QRect(240, 240, 91, 31))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Your order is :", None))
        self.label_2.setText(_translate("Form", "Your current balance is :", None))

  
        from order2 import order
        ex = order()
        ex.buttonclicked()
       

