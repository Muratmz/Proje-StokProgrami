# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Anasayfa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        MainWindow.setStyleSheet("/*\n"
"Ubuntu Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 09/10/2019 (dd/mm/yyyy), 12:31.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Ubuntu.qss\n"
"*/\n"
"QMainWindow {\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QCheckBox {\n"
"    padding:2px;\n"
"}\n"
"QCheckBox:hover {\n"
"    border:1px solid rgb(255,150,60);\n"
"    border-radius:4px;\n"
"    padding: 1px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border:1px solid rgb(246, 134, 86);\n"
"    border-radius:4px;\n"
"      background-color:rgb(246, 134, 86)\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border-width:1px solid rgb(246, 134, 86);\n"
"    border-radius:4px;\n"
"      background-color:rgb(255,255,255);\n"
"}\n"
"QColorDialog {\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QComboBox {\n"
"    color:rgb(81,72,65);\n"
"    background: #ffffff;\n"
"}\n"
"QComboBox:editable {\n"
"    selection-color:rgb(81,72,65);\n"
"    selection-background-color: #ffffff;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    selection-color: #ffffff;\n"
"    selection-background-color: rgb(246, 134, 86);\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color:  #1e1d23;    \n"
"}\n"
"QDateTimeEdit, QDateEdit, QDoubleSpinBox, QFontComboBox {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QDialog {\n"
"    background-color:#f0f0f0;\n"
"}\n"
"\n"
"QLabel,QLineEdit {\n"
"    color:rgb(17,17,17);\n"
"}\n"
"QLineEdit {\n"
"    background-color:rgb(255,255,255);\n"
"    selection-background-color:rgb(236,116,64);\n"
"}\n"
"QMenuBar {\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QMenuBar::item {\n"
"    padding-top:4px;\n"
"    padding-left:4px;\n"
"    padding-right:4px;\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QMenuBar::item:selected {\n"
"    color:rgb(255,255,255);\n"
"    padding-top:2px;\n"
"    padding-left:2px;\n"
"    padding-right:2px;\n"
"    border-top-width:2px;\n"
"    border-left-width:2px;\n"
"    border-right-width:2px;\n"
"    border-top-right-radius:4px;\n"
"    border-top-left-radius:4px;\n"
"    border-style:solid;\n"
"    background-color:rgb(65,64,59);\n"
"    border-top-color: rgb(47,47,44);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));\n"
"}\n"
"QMenu {\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QMenu::item {\n"
"    color:rgb(223,219,210);\n"
"    padding:4px 10px 4px 20px;\n"
"}\n"
"QMenu::item:selected {\n"
"    color:rgb(255,255,255);\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));\n"
"    border-style:solid;\n"
"    border-width:3px;\n"
"    padding:4px 7px 4px 17px;\n"
"    border-bottom-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));\n"
"    border-top-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-right-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-left-color:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"    border-width: 1px solid transparent;\n"
"    color:rgb(17,17,17);\n"
"    selection-background-color:rgb(236,116,64);\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"    border: 1px inset rgb(150,150,150); \n"
"    border-radius: 10px;\n"
"    background-color:rgb(221,221,219);\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));\n"
"    border:1px solid;\n"
"    border-radius:8px;\n"
"    border-bottom-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));\n"
"    border-top-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-right-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-left-color:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"}\n"
"QPushButton{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-bottom-color: rgb(150,150,150);\n"
"    border-right-color: rgb(165,165,165);\n"
"    border-left-color: rgb(165,165,165);\n"
"    border-top-color: rgb(180,180,180);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:default{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-width: 1px;\n"
"    border-top-color: rgba(255,150,60,200);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"    border-bottom-color: rgba(200,70,20,200);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"    color:rgb(174,167,159);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(200, 200, 200, 255), stop:1 rgba(230, 230, 230, 255));\n"
"}\n"
"QRadioButton {\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgba(246, 134, 86, 255);\n"
"    color: #a9b7c6;\n"
"    background-color:rgba(246, 134, 86, 255);\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(246, 134, 86);\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QScrollArea {\n"
"    color: white;\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QSlider::groove {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal, QSlider::add-page:vertical {\n"
"     background: white;\n"
"}\n"
"QSlider::sub-page:horizontal, QSlider::sub-page:vertical {\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QStatusBar, QSpinBox {\n"
"    color:rgb(81,72,65);\n"
"}\n"
"QSpinBox {\n"
"    background-color: #ffffff;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 20px;\n"
"    border: 1px transparent;\n"
"    margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border: 1px solid rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(253,253,253);\n"
"    border: 1px solid rgb(255,150,60);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"      border: 1px solid rgb(255,150,60);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-left-radius: 7px;\n"
"      border-top-right-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"      border: 1px solid rgb(255,150,60);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"      border: 1px transparent grey;\n"
"      border-top-left-radius: 3px;\n"
"      border-bottom-left-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"    border: 1px transparent grey;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"     background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
"} \n"
"QScrollBar:vertical {\n"
"    max-width: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid;\n"
"    border-color: rgb(207,207,207);\n"
"    border-bottom-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(255,150,60);\n"
"      border-bottom-right-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"      border: 1px solid grey;\n"
"      border-bottom-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"      border: 1px solid rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"      border: 1px solid rgb(255,150,60);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-left-radius: 7px;\n"
"      border-top-right-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"     height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border: 1px solid rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(253,253,253);\n"
"    border: 1px solid rgb(255,150,60);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"    border: 1px transparent grey;\n"
"      border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"      border: 1px transparent grey;\n"
"      border-bottom-left-radius: 3px;\n"
"      border-bottom-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"      background: none;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:rgb(247,246,246);\n"
"}\n"
"QTabWidget::pane {\n"
"    border-color: rgb(180,180,180);\n"
"    background-color:rgb(247,246,246);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"      border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    padding-left:4px;\n"
"    padding-right:4px;\n"
"    padding-bottom:2px;\n"
"    padding-top:2px;\n"
"    color:rgb(81,72,65);\n"
"      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(221,218,217,255), stop:1 rgba(240,239,238,255));\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"      border-top-right-radius:4px;\n"
"    border-top-left-radius:4px;\n"
"    border-top-color: rgb(180,180,180);\n"
"    border-left-color: rgb(180,180,180);\n"
"    border-right-color: rgb(180,180,180);\n"
"    border-bottom-color: transparent;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      background-color:rgb(247,246,246);\n"
"      margin-left: 0px;\n"
"      margin-right: 1px;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 1px;\n"
"    margin-right: 1px;\n"
"}\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color:transparent;\n"
"    color:rgb(17,17,17);\n"
"    selection-background-color:rgb(236,116,64);\n"
"}\n"
"QTimeEdit, QToolBox, QToolBox::tab, QToolBox::tab:selected {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, -1, 851, 421))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.cmbStokdurumu = QtWidgets.QComboBox(self.groupBox)
        self.cmbStokdurumu.setObjectName("cmbStokdurumu")
        self.cmbStokdurumu.addItem("")
        self.cmbStokdurumu.addItem("")
        self.cmbStokdurumu.addItem("")
        self.horizontalLayout_10.addWidget(self.cmbStokdurumu)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lneMaliyet = QtWidgets.QLineEdit(self.groupBox)
        self.lneMaliyet.setPlaceholderText("")
        self.lneMaliyet.setObjectName("lneMaliyet")
        self.horizontalLayout.addWidget(self.lneMaliyet)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lneIscilik = QtWidgets.QLineEdit(self.groupBox)
        self.lneIscilik.setObjectName("lneIscilik")
        self.horizontalLayout_2.addWidget(self.lneIscilik)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.lneSatisFiyati = QtWidgets.QLineEdit(self.groupBox)
        self.lneSatisFiyati.setObjectName("lneSatisFiyati")
        self.horizontalLayout_3.addWidget(self.lneSatisFiyati)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.lneAliciAdi = QtWidgets.QLineEdit(self.groupBox)
        self.lneAliciAdi.setObjectName("lneAliciAdi")
        self.horizontalLayout_4.addWidget(self.lneAliciAdi)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.lneKarat = QtWidgets.QLineEdit(self.groupBox)
        self.lneKarat.setObjectName("lneKarat")
        self.horizontalLayout_5.addWidget(self.lneKarat)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.lneurunId = QtWidgets.QLineEdit(self.groupBox)
        self.lneurunId.setObjectName("lneurunId")
        self.horizontalLayout_6.addWidget(self.lneurunId)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.lneAliciIletisim = QtWidgets.QLineEdit(self.groupBox)
        self.lneAliciIletisim.setObjectName("lneAliciIletisim")
        self.horizontalLayout_7.addWidget(self.lneAliciIletisim)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.spbStokSayisi = QtWidgets.QSpinBox(self.groupBox)
        self.spbStokSayisi.setObjectName("spbStokSayisi")
        self.horizontalLayout_8.addWidget(self.spbStokSayisi)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.cwidSatisTarihi = QtWidgets.QCalendarWidget(self.groupBox)
        self.cwidSatisTarihi.setObjectName("cwidSatisTarihi")
        self.verticalLayout_2.addWidget(self.cwidSatisTarihi)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 430, 1091, 391))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(500, 0, 421, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_12.setFont(font)
        self.label_12.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 820, 161, 31))
        self.label_13.setObjectName("label_13")
        self.lblUrunsayisi = QtWidgets.QLabel(self.centralwidget)
        self.lblUrunsayisi.setGeometry(QtCore.QRect(160, 830, 55, 16))
        self.lblUrunsayisi.setText("")
        self.lblUrunsayisi.setObjectName("lblUrunsayisi")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(900, 50, 221, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnKayitEkle = QtWidgets.QPushButton(self.layoutWidget)
        self.btnKayitEkle.setObjectName("btnKayitEkle")
        self.verticalLayout_4.addWidget(self.btnKayitEkle)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.btnGuncelle = QtWidgets.QPushButton(self.layoutWidget)
        self.btnGuncelle.setObjectName("btnGuncelle")
        self.verticalLayout_4.addWidget(self.btnGuncelle)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.btnSil = QtWidgets.QPushButton(self.layoutWidget)
        self.btnSil.setObjectName("btnSil")
        self.verticalLayout_4.addWidget(self.btnSil)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.btnAra = QtWidgets.QPushButton(self.layoutWidget)
        self.btnAra.setObjectName("btnAra")
        self.verticalLayout_4.addWidget(self.btnAra)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        self.btnListele = QtWidgets.QPushButton(self.layoutWidget)
        self.btnListele.setObjectName("btnListele")
        self.verticalLayout_4.addWidget(self.btnListele)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.btnResimEkle = QtWidgets.QPushButton(self.layoutWidget)
        self.btnResimEkle.setObjectName("btnResimEkle")
        self.verticalLayout_4.addWidget(self.btnResimEkle)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem14)
        self.btnResmiGoster = QtWidgets.QPushButton(self.layoutWidget)
        self.btnResmiGoster.setObjectName("btnResmiGoster")
        self.verticalLayout_4.addWidget(self.btnResmiGoster)
        self.btnCikis = QtWidgets.QPushButton(self.centralwidget)
        self.btnCikis.setGeometry(QtCore.QRect(1088, -5, 111, 31))
        self.btnCikis.setObjectName("btnCikis")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 25))
        self.menubar.setObjectName("menubar")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.hakkimda = QtWidgets.QAction(MainWindow)
        self.hakkimda.setObjectName("hakkimda")
        self.menuYard_m.addAction(self.hakkimda)
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Ürün Bilgileri"))
        self.label_11.setText(_translate("MainWindow", "Stok Durumu : "))
        self.cmbStokdurumu.setItemText(0, _translate("MainWindow", "Envanterde Var"))
        self.cmbStokdurumu.setItemText(1, _translate("MainWindow", "----------"))
        self.cmbStokdurumu.setItemText(2, _translate("MainWindow", "Satıldı"))
        self.label.setText(_translate("MainWindow", "Maliyet"))
        self.label_2.setText(_translate("MainWindow", "İşçilik"))
        self.label_3.setText(_translate("MainWindow", "Satış Fiyatı"))
        self.label_5.setText(_translate("MainWindow", "Alıcı İsmi :"))
        self.label_6.setText(_translate("MainWindow", "Gram, Karat (D1, D2 vb.) :"))
        self.lneKarat.setPlaceholderText(_translate("MainWindow", "Gram, Karat"))
        self.label_7.setText(_translate("MainWindow", "Ürün Id :"))
        self.label_8.setText(_translate("MainWindow", "Alıcı İletişim :"))
        self.label_9.setText(_translate("MainWindow", "Stok Sayısı : "))
        self.label_4.setText(_translate("MainWindow", "Satış Tarihi :"))
        self.tableWidget.setSortingEnabled(True)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "ASDASLIHDASIOHDASOIHDASIPHDPASIDHJPASOJDSA"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_12.setText(_translate("MainWindow", "MIHLAYICI OZAN"))
        self.label_13.setText(_translate("MainWindow", "Envanterdeki Ürün Sayısı : "))
        self.btnKayitEkle.setText(_translate("MainWindow", "Kayıt Ekle"))
        self.btnGuncelle.setText(_translate("MainWindow", "Kayıt Güncelle"))
        self.btnSil.setText(_translate("MainWindow", "Kayıt Sil"))
        self.btnAra.setText(_translate("MainWindow", "Kayıt Ara"))
        self.btnListele.setText(_translate("MainWindow", "Kayıt Listele"))
        self.btnResimEkle.setText(_translate("MainWindow", "Resim Ekle"))
        self.btnResmiGoster.setText(_translate("MainWindow", "Resmi Göster"))
        self.btnCikis.setText(_translate("MainWindow", "Çıkış"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.hakkimda.setText(_translate("MainWindow", "Hakkımızda"))

