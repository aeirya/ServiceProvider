# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/madscientist/untitled1/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(800, 600)
        self.quitButton = QtWidgets.QPushButton(main)
        self.quitButton.setGeometry(QtCore.QRect(640, 540, 151, 41))
        self.quitButton.setObjectName("quitButton")
        self.label = QtWidgets.QLabel(main)
        self.label.setGeometry(QtCore.QRect(210, 40, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.reportButton = QtWidgets.QPushButton(main)
        self.reportButton.setGeometry(QtCore.QRect(320, 180, 161, 61))
        self.reportButton.setObjectName("reportButton")
        self.clientsButton = QtWidgets.QPushButton(main)
        self.clientsButton.setGeometry(QtCore.QRect(320, 240, 161, 71))
        self.clientsButton.setObjectName("clientsButton")
        self.workersButton = QtWidgets.QPushButton(main)
        self.workersButton.setGeometry(QtCore.QRect(320, 310, 161, 71))
        self.workersButton.setObjectName("workersButton")

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "main"))
        self.quitButton.setText(_translate("main", "خروج"))
        self.label.setText(_translate("main", "سیستم مدیریت شرکت خدمات􏰀"))
        self.reportButton.setText(_translate("main", "گزارش مالی"))
        self.clientsButton.setText(_translate("main", "لیست کاربران"))
        self.workersButton.setText(_translate("main", "خدمات دهندگان"))
