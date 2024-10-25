from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QGridLayout,QTextBrowser
from PyQt5 import QtGui
import sys
import rps

class TextEditDemo(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)

                self.setWindowTitle("Rock Paper Scissors")
                self.setWindowIcon(QtGui.QIcon('icon.png'))
                self.resize(500,400)
                
                self.btnRock = QPushButton("Rock")
                self.btnPaper = QPushButton("Paper")
                self.btnScissors = QPushButton("Scissors")
                self.btnExit = QPushButton("Exit")

                self.statusText = QTextBrowser()

                layout = QGridLayout()

                # First column
                layout.addWidget(self.btnRock, 1, 1, 1, 1)
                layout.addWidget(self.btnPaper, 2, 1, 1, 1)
                layout.addWidget(self.btnScissors, 3, 1, 1, 1)
                layout.addWidget(self.btnExit, 4, 1, 1, 1)
                # Second column
                layout.addWidget(self.statusText, 1, 2, 4, 1)

                self.setLayout(layout)

                self.btnRock.clicked.connect(self.btnRock_Clicked)
                self.btnPaper.clicked.connect(self.btnPaper_Clicked)
                self.btnScissors.clicked.connect(self.btnScissors_Clicked)
                self.btnExit.clicked.connect(self.btnExit_Clicked)

        def btnRock_Clicked(self):
                self.statusText.setPlainText(rps.RPSGame.startGame(1))

        def btnPaper_Clicked(self):
                self.statusText.setPlainText(rps.RPSGame.startGame(2))

        def btnScissors_Clicked(self):
                self.statusText.setPlainText(rps.RPSGame.startGame(3))

        def btnExit_Clicked(self):
                self.statusText.setPlainText(rps.RPSGame.startGame(0))

if __name__ == '__main__':
        app = QApplication(sys.argv)
        win = TextEditDemo()
        win.show()
        sys.exit(app.exec_())