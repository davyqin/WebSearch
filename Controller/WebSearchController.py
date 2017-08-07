from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from GUI.WebSearchDialog import WebSearchDialog
from Util.UrlGenerator import UrlGenerator
from Util.UrlEngine import UrlEngine
from Util.TextCapturer import TextCapturer

class WebSearchController(QObject):
	def __init__(self, parent=None):
		super(WebSearchController, self).__init__(parent)
		self.__dialog = WebSearchDialog()
		self.__dialog.searchSignal.connect(self.doSearch)

	def activate(self):
		self.__dialog.show()

	@pyqtSlot(str, int, int)
	def doSearch(self, urlTemplate, start, end):
		urlGen = UrlGenerator(urlTemplate, start, end)
		# urlEngine = UrlEngine({'http': 'http://139.24.205.163:8080/'})
		urlEngine = UrlEngine()
		textCapture = TextCapturer("gbk", "name=\"title\" ><a title=", "href=")

		for url in urlGen.genURL():
			self.__dialog.appendResult("-" * 30 + url + "-" * 30)
			for result in textCapture.captureText(urlEngine.work(url)):
				self.__dialog.appendResult(result)
			# self.__dialog.appendResult(textCapture.captureText(urlEngine.work(url)))

		self.__dialog.appendResult("Done!")