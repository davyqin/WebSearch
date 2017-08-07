from PyQt5 import QtWidgets
from Controller.WebSearchController import WebSearchController


def main():
	app = QtWidgets.QApplication(sys.argv)
	controller = WebSearchController()
	controller.activate()
	sys.exit(app.exec_())

if __name__ == "__main__":
	import sys
	main()
