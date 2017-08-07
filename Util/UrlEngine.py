import urllib.request

class UrlEngine:
	def __init__(self, proxy = {}):
		self.setProxy(proxy)

	def setProxy(self, proxy):
		if type(proxy) is not dict:
			raise Exception("Proxy configuration is not correct.")
		self.__proxy = proxy

	def work(self, url):
		opener = urllib.request.FancyURLopener(self.__proxy)
		tempfile = opener.open(url)
		urlContents = tempfile.readlines()
		tempfile.close()
		return urlContents