import sys
from PyQt4 import QtGui, uic

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = uic.loadUi('cliente.ui', self)
        self.ui.table_widget_cliente.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.ui.table_widget_cliente.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.show()
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())