# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyqtfile\test2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(485, 376)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 100, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 170, 71, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 210, 71, 21))
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(170, 90, 211, 31))
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(170, 130, 211, 31))
        self.textBrowser_2.setReadOnly(False)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(170, 170, 211, 31))
        self.textBrowser_3.setReadOnly(False)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_4.setGeometry(QtCore.QRect(170, 210, 211, 31))
        self.textBrowser_4.setReadOnly(False)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(200, 40, 91, 41))
        self.label_5.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 9pt \"微软雅黑\";")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 280, 321, 41))
        self.pushButton.setStyleSheet("font: 14pt \"微软雅黑\";\n"
"background-color: rgb(0, 85, 255);")
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(80, 250, 111, 16))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "欢迎注册"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\"> 账  号</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">密  码</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">确认密码</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">电子邮件</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\"> 注 册</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", " 注      册"))
        self.checkBox.setText(_translate("Form", "同意用户协议"))


