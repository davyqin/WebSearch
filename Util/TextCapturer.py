class TextCapturer:
	def __init__(self):
		self.__coding = "utf-8"
		self.__leadText = ""
		self.__endText = ""

	def __init__(self, coding, leadText, endText):
		self.__coding = coding
		self.setLeadText(leadText)
		self.setEndText(endText)

	def setLeadText(self, leadText):
		if type(leadText) is not str:
			raise Exception("Lead Text is not str type")

		self.__leadText = leadText

	def setEndText(self, endText):
		if type(endText) is not str:
			raise Exception("End Text is not str type")

		self.__endText = endText

	def captureText(self, content):
		# result = []		
		for line in content:
			temp = str(line.decode(self.__coding, 'ignore'))
			posStart = temp.find(self.__leadText)
			if posStart > -1:
				temp = temp[posStart + len(self.__leadText) + 1:]
				endPos = temp.find(self.__endText) - 2
				yield temp[:endPos]
				# result.append(temp[:endPos])