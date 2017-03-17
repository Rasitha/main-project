

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
var=" "
class Ui_Form(QtGui.QWidget):
    def __init__(self):
       QtGui.QWidget.__init__(self)
       self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(468, 296)
        self.p1 = QtGui.QPushButton(Form)
        self.p1.setGeometry(QtCore.QRect(90, 70, 41, 31))
        self.p1.setObjectName(_fromUtf8("p1"))
        self.p2 = QtGui.QPushButton(Form)
        self.p2.setGeometry(QtCore.QRect(180, 70, 41, 31))
        self.p2.setObjectName(_fromUtf8("p2"))
        self.p3 = QtGui.QPushButton(Form)
        self.p3.setGeometry(QtCore.QRect(270, 70, 41, 31))
        self.p3.setObjectName(_fromUtf8("p3"))
        self.p4 = QtGui.QPushButton(Form)
        self.p4.setGeometry(QtCore.QRect(90, 120, 41, 31))
        self.p4.setObjectName(_fromUtf8("p4"))
        self.p5 = QtGui.QPushButton(Form)
        self.p5.setGeometry(QtCore.QRect(180, 120, 41, 31))
        self.p5.setObjectName(_fromUtf8("p5"))
        self.p6 = QtGui.QPushButton(Form)
        self.p6.setGeometry(QtCore.QRect(270, 120, 41, 31))
        self.p6.setObjectName(_fromUtf8("p6"))
        self.p7 = QtGui.QPushButton(Form)
        self.p7.setGeometry(QtCore.QRect(90, 170, 41, 31))
        self.p7.setObjectName(_fromUtf8("p7"))
        self.p8 = QtGui.QPushButton(Form)
        self.p8.setGeometry(QtCore.QRect(180, 170, 41, 31))
        self.p8.setObjectName(_fromUtf8("p8"))
        self.p9 = QtGui.QPushButton(Form)
        self.p9.setGeometry(QtCore.QRect(270, 170, 41, 31))
        self.p9.setObjectName(_fromUtf8("p9"))
        self.p10 = QtGui.QPushButton(Form)
        self.p10.setGeometry(QtCore.QRect(180, 220, 41, 31))
        self.p10.setObjectName(_fromUtf8("p10"))
        self.l = QtGui.QLabel(Form)
        self.l.setGeometry(QtCore.QRect(10, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l.setFont(font)
        self.l.setObjectName(_fromUtf8("l"))
        self.cm1 = QtGui.QCommandLinkButton(Form)
        self.cm1.setGeometry(QtCore.QRect(250, 220, 101, 31))
        self.cm1.setObjectName(_fromUtf8("cm1"))
        self.cm2 = QtGui.QCommandLinkButton(Form)
        self.cm2.setGeometry(QtCore.QRect(60, 220, 81, 31))
        self.cm2.setObjectName(_fromUtf8("cm2"))
	self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(210, 20, 211, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.p1.setText(_translate("Form", "1", None))
        self.p2.setText(_translate("Form", "2", None))
        self.p3.setText(_translate("Form", "3", None))
        self.p4.setText(_translate("Form", "4", None))
        self.p5.setText(_translate("Form", "5", None))
        self.p6.setText(_translate("Form", "6", None))
        self.p7.setText(_translate("Form", "7", None))
        self.p8.setText(_translate("Form", "8", None))
        self.p9.setText(_translate("Form", "9", None))
        self.p10.setText(_translate("Form", "0", None))
        self.l.setText(_translate("Form", "Enter Your Passcode", None))
        self.cm1.setText(_translate("Form", "Confirm", None))
        self.cm2.setText(_translate("Form", "Clear", None))
        
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
        c = self.lineEdit.text()
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())

