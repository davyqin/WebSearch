class UrlGenerator:
	def __init__(self):
		self.__urlTemplate = ""
		self.__start = 0
		self.__end = 1

	def __init__(self, urlTemplate, start, end):
		self.setUrlTemplate(urlTemplate)
		self.setStartEnd(start, end)

	def setUrlTemplate(self, urlTemplate):
		if "*" not in  urlTemplate:
		 	raise Exception("Url Template is not correct format")

		self.__urlTemplate = urlTemplate.replace("*","{0}")

	def setStartEnd(self, start, end):
		if type(start) is not int:
			raise Exception("start is not int type")

		if type(end) is not int:
		 	raise Exception("end is not int type")

		if end <= start:
			raise Exception("End is less than start")

		self.__start = start
		self.__end = end

	def genURL(self):
		for num in range(self.__start, self.__end):
			result = self.__urlTemplate.format(num)
			yield result