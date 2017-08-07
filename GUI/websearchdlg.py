# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'websearchdlg.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WebSearchDialog(object):
    def setupUi(self, WebSearchDialog):
        WebSearchDialog.setObjectName("WebSearchDialog")
        WebSearchDialog.resize(511, 459)
        self.verticalLayout = QtWidgets.QVBoxLayout(WebSearchDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(WebSearchDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.urlEdit = QtWidgets.QLineEdit(WebSearchDialog)
        self.urlEdit.setObjectName("urlEdit")
        self.horizontalLayout.addWidget(self.urlEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(WebSearchDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.startEdit = QtWidgets.QLineEdit(WebSearchDialog)
        self.startEdit.setObjectName("startEdit")
        self.horizontalLayout_2.addWidget(self.startEdit)
        self.label_3 = QtWidgets.QLabel(WebSearchDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.endEdit = QtWidgets.QLineEdit(WebSearchDialog)
        self.endEdit.setObjectName("endEdit")
        self.horizontalLayout_2.addWidget(self.endEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.resultEdit = QtWidgets.QTextEdit(WebSearchDialog)
        self.resultEdit.setReadOnly(True)
        self.resultEdit.setObjectName("resultEdit")
        self.verticalLayout.addWidget(self.resultEdit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.searchButton = QtWidgets.QPushButton(WebSearchDialog)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_3.addWidget(self.searchButton)
        self.resetButton = QtWidgets.QPushButton(WebSearchDialog)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_3.addWidget(self.resetButton)
        self.closeButton = QtWidgets.QPushButton(WebSearchDialog)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(WebSearchDialog)
        self.closeButton.clicked.connect(WebSearchDialog.close)
        QtCore.QMetaObject.connectSlotsByName(WebSearchDialog)

    def retranslateUi(self, WebSearchDialog):
        _translate = QtCore.QCoreApplication.translate
        WebSearchDialog.setWindowTitle(_translate("WebSearchDialog", "WebSearch"))
        self.label.setText(_translate("WebSearchDialog", "Url Template"))
        self.label_2.setText(_translate("WebSearchDialog", "Start"))
        self.label_3.setText(_translate("WebSearchDialog", "End"))
        self.searchButton.setText(_translate("WebSearchDialog", "Search"))
        self.resetButton.setText(_translate("WebSearchDialog", "Rest"))
        self.closeButton.setText(_translate("WebSearchDialog", "Close"))

