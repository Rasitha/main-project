

import sys
from PyQt4 import QtCore, QtGui
from welcome2 import Ui_Form

#class Main(QtGui.QMainWindow):
#    def __init__(self):
#        super(Main, self).__init__()

        # build ui
     
	
  

if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    ui1 = Ui_Form()
    ui1.show()	
    sys.exit(app.exec_())
