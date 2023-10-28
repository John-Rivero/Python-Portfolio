
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1273, 923)
        MainWindow.setMinimumSize(QtCore.QSize(1273, 923))
        MainWindow.setMaximumSize(QtCore.QSize(1273, 923))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.departure = QtWidgets.QTextEdit(parent=self.widget)
        self.departure.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.departure.setFont(font)
        self.departure.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDate)
        self.departure.setObjectName("departure")
        self.gridLayout_2.addWidget(self.departure, 2, 0, 1, 1)
        
##############################################################       
        
        #location from Dropdown
        self.locationFrom = QtWidgets.QComboBox(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.locationFrom.setFont(font)
        
        self.locationFrom.setObjectName("locationFrom")
        self.gridLayout_2.addWidget(self.locationFrom, 1, 0, 1, 1)
        
##############################################################
        
        #location to Dropdown
        self.locationTo = QtWidgets.QComboBox(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.locationTo.setFont(font)
        

        
        self.locationTo.setObjectName("locationTo")
        self.gridLayout_2.addWidget(self.locationTo, 1, 1, 1, 1)
        
##############################################################
        
        self.arriving = QtWidgets.QTextEdit(parent=self.widget)
        self.arriving.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.arriving.setFont(font)
        self.arriving.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDate)
        self.arriving.setObjectName("arriving")
        self.gridLayout_2.addWidget(self.arriving, 2, 1, 1, 1)
        self.Top = QtWidgets.QWidget(parent=self.widget)
        self.Top.setMinimumSize(QtCore.QSize(0, 100))
        self.Top.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Top.setStyleSheet("\n"
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
        self.Top.setObjectName("Top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Top)
        self.horizontalLayout_2.setContentsMargins(1, 5, 1, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Identification_2 = QtWidgets.QGridLayout()
        self.Identification_2.setObjectName("Identification_2")
        self.FlightSearchTitle = QtWidgets.QLabel(parent=self.Top)
        self.FlightSearchTitle.setMinimumSize(QtCore.QSize(0, 0))
        self.FlightSearchTitle.setMaximumSize(QtCore.QSize(1000, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(30)
        font.setBold(True)
        self.FlightSearchTitle.setFont(font)
        self.FlightSearchTitle.setStyleSheet("color : #fff")
        self.FlightSearchTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.FlightSearchTitle.setWordWrap(False)
        self.FlightSearchTitle.setIndent(-4)
        self.FlightSearchTitle.setObjectName("FlightSearchTitle")
        self.Identification_2.addWidget(self.FlightSearchTitle, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.Identification_2)
        self.gridLayout_2.addWidget(self.Top, 0, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
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
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"\n"
"    background-color: rgb(58, 202, 111);\n"
"    border : #fff;\n"
"    \n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 2, 2, 1)
        self.cityImage = QtWidgets.QLabel(parent=self.widget)
        self.cityImage.setStyleSheet("QLabel\n"
"\n"
"{border : 1px solid  rgb(200, 200, 200);\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 10px;\n"
"background-color: rgb(250,250,250);\n"
"\n"
"}")
        self.cityImage.setText("")
        self.cityImage.setObjectName("cityImage")
        self.gridLayout_2.addWidget(self.cityImage, 3, 0, 1, 3)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.flightresult = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.flightresult.setMaximumSize(QtCore.QSize(16777215, 150))
        self.flightresult.setStyleSheet("QTextEdit\n"
"\n"
"{border : 1px solid  rgb(200, 200, 200);\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"border-radius: 10px;\n"
"background-color: rgb(250,250,250);\n"
"\n"
"}")
        self.flightresult.setReadOnly(True)
        self.flightresult.setObjectName("flightresult")
        self.gridLayout.addWidget(self.flightresult, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FlightSearchTitle.setText(_translate("MainWindow", "Flight Search"))
        self.pushButton.setText(_translate("MainWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
