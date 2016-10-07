import sys
from PyQt4 import QtGui, uic, QtCore

class MyWindow(QtGui.QMainWindow) :
	def __init__(self):
		super(MyWindow, self).__init__()
		self.ui = uic.loadUi('servidor.ui', self)
		self.actualiza_tabla()
		self.timer  = QtCore.QTimer(self)
		self.timer.setInterval(1000)          
		self.timer.timeout.connect(self.actualiza_tabla)
		self.timer.start()
		self.show()

	@QtCore.pyqtSlot()
	def actualiza_tabla(self) :
		columnas = int(self.ui.spin_columnas.text())
		filas = int(self.ui.spin_filas.text())
		if filas == self.ui.table_widget_board.rowCount() and columnas == self.ui.table_widget_board.columnCount() :
			return
		self.ui.table_widget_board.setRowCount(filas)
		self.ui.table_widget_board.setColumnCount(columnas)
		self.ui.table_widget_board.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
		self.ui.table_widget_board.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

if __name__ == '__main__' :
	app = QtGui.QApplication(sys.argv)
	window = MyWindow()
	sys.exit(app.exec_())