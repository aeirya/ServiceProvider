# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/madscientist/untitled1/form.ui'
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
        self.pushButton = QtWidgets.QPushButton(main)
        self.pushButton.setGeometry(QtCore.QRect(640, 540, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(main)
        self.label.setGeometry(QtCore.QRect(210, 40, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(main)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 180, 161, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(main)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 240, 161, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.f)
        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def f(self):
        print("HI")

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "main"))
        self.pushButton.setText(_translate("main", "خروج"))
        self.label.setText(_translate("main", "سیستم مدیریت شرکت خدمات􏰀"))
        self.pushButton_2.setText(_translate("main", "گزارش مالی"))
        self.pushButton_3.setText(_translate("main", "لیست کاربران"))

    