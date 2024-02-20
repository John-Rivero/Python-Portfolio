
from PyQt6 import QtCore, QtGui, QtWidgets
from logic import *
import logic
import sys

#from logic import display_nba_stats

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(552, 683)
        MainWindow.setMinimumSize(QtCore.QSize(552, 683))
        MainWindow.setMaximumSize(QtCore.QSize(552, 683))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(parent=self.widget)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 150))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 150))
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 3, 0, 1, 1)
        self.NBA_Logo = QtWidgets.QLabel(parent=self.widget)
        self.NBA_Logo.setMinimumSize(QtCore.QSize(0, 400))
        self.NBA_Logo.setMaximumSize(QtCore.QSize(16777215, 400))
        self.NBA_Logo.setText("")
        self.NBA_Logo.setScaledContents(True)
        self.NBA_Logo.setObjectName("NBA_Logo")
        self.gridLayout_2.addWidget(self.NBA_Logo, 2, 0, 1, 1)
        self.NBA_Team_Stats_Title = QtWidgets.QLabel(parent=self.widget)
        self.NBA_Team_Stats_Title.setMinimumSize(QtCore.QSize(0, 110))
        self.NBA_Team_Stats_Title.setMaximumSize(QtCore.QSize(16777215, 110))
        self.NBA_Team_Stats_Title.setText("")
        self.NBA_Team_Stats_Title.setPixmap(QtGui.QPixmap("image/NBA Team Logo Title.png"))
        self.NBA_Team_Stats_Title.setScaledContents(True)
        self.NBA_Team_Stats_Title.setObjectName("NBA_Team_Stats_Title")
        self.gridLayout_2.addWidget(self.NBA_Team_Stats_Title, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setPlaceholderText('Select a team...')
        team_list_name = [team[1] for team in teams_list]
        self.comboBox.addItems(team_list_name)
        self.comboBox.currentIndexChanged.connect(lambda: logic.display_nba_stats(self))
        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2023 NBA Stats"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
