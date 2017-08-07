from GUI.websearchdlg import Ui_WebSearchDialog
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal

class WebSearchDialog(QDialog):
	searchSignal = pyqtSignal(str, int, int)

	def __init__(self, parent=None):
		super(WebSearchDialog, self).__init__(parent)
		self.__ui = Ui_WebSearchDialog()
		self.__ui.setupUi(self)
		self.__ui.resetButton.clicked.connect(self.resetDialog)
		self.__ui.searchButton.clicked.connect(self.doSearch)
		self.resize(800,800)

		self.__ui.urlEdit.setText("http://category.dangdang.com/pg*-cp01.54.06.00.00.00.html")
		self.__ui.startEdit.setText("1")
		self.__ui.endEdit.setText("2")

	@pyqtSlot()
	def resetDialog(self):
		self.__ui.urlEdit.clear()
		self.__ui.startEdit.clear()
		self.__ui.endEdit.clear()
		self.__ui.resultEdit.clear()

	@pyqtSlot()
	def doSearch(self):
		self.__ui.resultEdit.clear()

		if "*" not in self.__ui.urlEdit.text():
			msgBox = QMessageBox(QMessageBox.Warning, "Warning", "Url Template is not correct format.", QMessageBox.Ok)
			msgBox.exec()
			return

		if self.__ui.startEdit.text().isdigit() == False or self.__ui.endEdit.text().isdigit() == False:
			msgBox = QMessageBox(QMessageBox.Warning, "Warning", "Start or End is not int type.", QMessageBox.Ok)
			msgBox.exec()
			return

		self.searchSignal.emit(self.__ui.urlEdit.text(),
			                     eval(self.__ui.startEdit.text()),
			                     eval(self.__ui.endEdit.text()))

	def appendResult(self, result):
		if len(result) < 1:
			return
		self.__ui.resultEdit.append(result)
		self.__ui.resultEdit.append("\n")
		# self.__ui.resultEdit.update()

	def showResult(self, result):
		self.__ui.resultEdit.clear()
		for line in result:
			self.__ui.resultEdit.append(line)
