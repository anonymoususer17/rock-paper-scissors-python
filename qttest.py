from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QGridLayout,QTextBrowser,QLabel
from PyQt5 import QtGui
import sys

from PyQt5.uic.Compiler.qtproxies import QtCore

import rps

class ResponseObj:
    def __init__(self):
        self.playerMessage = ""
        self.wins = 0
        self.losses = 0
        self.ties = 0

class TextEditDemo(QWidget):

        responseObj = ResponseObj()

        def __init__(self,parent=None):
                super().__init__(parent)

                self.setWindowTitle("Rock Paper Scissors")
                self.setWindowIcon(QtGui.QIcon('icon.png'))
                self.resize(500,400)
                
                self.btnRock = QPushButton("Rock")
                self.btnPaper = QPushButton("Paper")
                self.btnScissors = QPushButton("Scissors")
                self.btnExit = QPushButton("Exit")
                self.msgBox = QLabel()
                self.statusText = QTextBrowser()

                layout = QGridLayout()

                # First column
                layout.addWidget(self.msgBox, 1, 1, 1, 2)
                layout.addWidget(self.btnRock, 2, 1, 1, 1)
                layout.addWidget(self.btnPaper, 3, 1, 1, 1)
                layout.addWidget(self.btnScissors, 4, 1, 1, 1)
                layout.addWidget(self.btnExit, 5, 1, 1, 1)
                # Second column
                layout.addWidget(self.statusText, 2, 2, 3, 1)

                self.setLayout(layout)

                self.btnRock.clicked.connect(self.btnRock_Clicked)
                self.btnPaper.clicked.connect(self.btnPaper_Clicked)
                self.btnScissors.clicked.connect(self.btnScissors_Clicked)
                self.btnExit.clicked.connect(self.btnExit_Clicked)


        def btnRock_Clicked(self):
                responseObj = rps.RPSGame.startGame(1, self.responseObj)
                self.statusText.setPlainText(responseObj.playerMessage)
                self.msgBox.setText(f"Wins: {responseObj.wins}\tLosses: {responseObj.losses}\tTies: {responseObj.ties}")

        def btnPaper_Clicked(self):
                responseObj = rps.RPSGame.startGame(2, self.responseObj)
                self.statusText.setPlainText(responseObj.playerMessage)
                self.msgBox.setText(f"Wins: {responseObj.wins}\tLosses: {responseObj.losses}\tTies: {responseObj.ties}")

        def btnScissors_Clicked(self):
                responseObj = rps.RPSGame.startGame(3, self.responseObj)
                self.statusText.setPlainText(responseObj.playerMessage)
                self.msgBox.setText(f"Wins: {responseObj.wins}\tLosses: {responseObj.losses}\tTies: {responseObj.ties}")

        def btnExit_Clicked(self):
                responseObj = rps.RPSGame.startGame(4, self.responseObj)
                self.statusText.setPlainText(responseObj.playerMessage)
                self.msgBox.setText(f"Wins: {responseObj.wins}\tLosses: {responseObj.losses}\tTies: {responseObj.ties}")

if __name__ == '__main__':
        app = QApplication(sys.argv)
        win = TextEditDemo()
        win.show()
        sys.exit(app.exec_())