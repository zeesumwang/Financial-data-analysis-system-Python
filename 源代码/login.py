# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 14:30:44 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyqtfile\test1.ui'f
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
import sys
class Ui_Form(object):
    
    
    
    
        
    
    
    
    def login(self):
        user=self.name.text()
        print(user) 
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(436, 344)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 200, 241, 41))
        self.pushButton.setStyleSheet("background-color: rgb(0, 85, 255);\n""font: 75 11pt \"微软雅黑\";\n""color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(150, 100, 161, 31))
        self.name.setObjectName("name")
        self.name.setText("策略过少，取消加入")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 100, 91, 31))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 150, 81, 31))
        self.label_2.setObjectName("label_2")
        
        self.pwd = QtWidgets.QLineEdit(Form)
        self.pwd.setGeometry(QtCore.QRect(150, 150, 161, 31))
        self.pwd.setObjectName("pwd")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(180, 30, 111, 61))
        self.label_3.setObjectName("label_3")
        self.goregister = QtWidgets.QCommandLinkButton(Form)
        self.goregister.setGeometry(QtCore.QRect(100, 250, 176, 41))
        self.goregister.setText("立即注册")
        self.goregister.setIconSize(QtCore.QSize(15, 15))
        self.goregister.setObjectName("goregister")
        self.goregister.raise_()
        self.goregister.clicked.connect(self.login)
        
        self.name.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pwd.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)
        
        
        
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.show()
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "欢迎登录"))
        self.pushButton.setText(_translate("Form", "登        录"))
        self.label.setText(_translate("Form", "     账 号"))
        self.label_2.setText(_translate("Form", "  密 码"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#0000ff;\">  登 录</span></p></body></html>"))

    

       
        
            







