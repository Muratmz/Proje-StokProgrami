# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hakkimda.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(484, 374)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, -40, 231, 291))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../OneDrive/Hobbies/Erhan/KaliteliFoto.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 250, 311, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 300, 221, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Hakkımda"))
        self.label_2.setText(_translate("Dialog", "Erhan Namlı © 2021 - Tüm Hakları Saklıdır"))
        self.label_3.setText(_translate("Dialog", "Websitem : erhan-namli.github.io"))

