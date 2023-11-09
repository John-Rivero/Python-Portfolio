# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flightsearch.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1273, 923)
        MainWindow.setMinimumSize(QSize(1273, 923))
        MainWindow.setMaximumSize(QSize(1273, 923))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.departure = QTextEdit(self.widget)
        self.departure.setObjectName(u"departure")
        self.departure.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.departure.setFont(font)
        self.departure.setInputMethodHints(Qt.ImhDate)

        self.gridLayout_2.addWidget(self.departure, 2, 0, 1, 1)

        self.locationFrom = QComboBox(self.widget)
        self.locationFrom.setObjectName(u"locationFrom")
        self.locationFrom.setFont(font)

        self.gridLayout_2.addWidget(self.locationFrom, 1, 0, 1, 1)

        self.locationTo = QComboBox(self.widget)
        self.locationTo.setObjectName(u"locationTo")
        self.locationTo.setFont(font)

        self.gridLayout_2.addWidget(self.locationTo, 1, 1, 1, 1)

        self.arriving = QTextEdit(self.widget)
        self.arriving.setObjectName(u"arriving")
        self.arriving.setMaximumSize(QSize(16777215, 30))
        self.arriving.setFont(font)
        self.arriving.setInputMethodHints(Qt.ImhDate)

        self.gridLayout_2.addWidget(self.arriving, 2, 1, 1, 1)

        self.Top = QWidget(self.widget)
        self.Top.setObjectName(u"Top")
        self.Top.setMinimumSize(QSize(0, 100))
        self.Top.setMaximumSize(QSize(16777215, 100))
        self.Top.setStyleSheet(u"\n"
"QWidget\n"
"\n"
"{\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background-color: rgb(79, 161, 255);\n"
"border-radius: 10px;\n"
"color : #fff\n"
"\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.Top)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 5, 1, 5)
        self.Identification_2 = QGridLayout()
        self.Identification_2.setObjectName(u"Identification_2")
        self.FlightSearchTitle = QLabel(self.Top)
        self.FlightSearchTitle.setObjectName(u"FlightSearchTitle")
        self.FlightSearchTitle.setMinimumSize(QSize(0, 0))
        self.FlightSearchTitle.setMaximumSize(QSize(1000, 100))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(30)
        font1.setBold(True)
        self.FlightSearchTitle.setFont(font1)
        self.FlightSearchTitle.setStyleSheet(u"color : #fff")
        self.FlightSearchTitle.setAlignment(Qt.AlignCenter)
        self.FlightSearchTitle.setWordWrap(False)
        self.FlightSearchTitle.setIndent(-4)

        self.Identification_2.addWidget(self.FlightSearchTitle, 0, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.Identification_2)


        self.gridLayout_2.addWidget(self.Top, 0, 0, 1, 3)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 60))
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"color : #fff;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 10px;\n"
"background-color: rgb(33, 126, 70);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"\n"
"	background-color: rgb(58, 202, 111);\n"
"	border : #fff;\n"
"	\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.pushButton, 1, 2, 2, 1)

        self.cityImage = QLabel(self.widget)
        self.cityImage.setObjectName(u"cityImage")
        self.cityImage.setStyleSheet(u"QLabel\n"
"\n"
"{border : 1px solid  rgb(200, 200, 200);\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 10px;\n"
"background-color: rgb(250,250,250);\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.cityImage, 3, 0, 1, 3)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.flightresult = QTextEdit(self.centralwidget)
        self.flightresult.setObjectName(u"flightresult")
        self.flightresult.setMaximumSize(QSize(16777215, 150))
        self.flightresult.setStyleSheet(u"QTextEdit\n"
"\n"
"{border : 1px solid  rgb(200, 200, 200);\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 10px;\n"
"background-color: rgb(250,250,250);\n"
"\n"
"}")
        self.flightresult.setReadOnly(True)

        self.gridLayout.addWidget(self.flightresult, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.FlightSearchTitle.setText(QCoreApplication.translate("MainWindow", u"Flight Search", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.cityImage.setText("")
    # retranslateUi

