#-*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from observer.observer import Observer

class hangmanView(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignLeft)
        font = self.font()
        font.setFamily('Courier New')
        self.setFont(font)
        self.setText("hangmanView")

    def update(observable):
        self.setText(observable.hangmanList[6-observable.numTries])

class currentWordView(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignCenter)
        font = self.font()
        font.setPointSize(font.pointSize() + 8)
        self.setFont(font)
        self.setText("currentWordView")

    def update(observable):
        self.setText(observable.currentStatus)

class guessedCharsView(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignLeft)
        self.setMaxLength(52)
        self.setText("guessedCharsView")

    def update(observable):
        self.setText(observable.guessedChars)

class messageView(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignLeft)
        self.setMaxLength(52)
        self.setText("messageView")

    def update(observable):
        self.setText("미구현")

class Layout(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


        # Hangman display window
        self.hangmanWindow = hangmanView()

        # Layout
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # Status Layout creation
        statusLayout = QGridLayout()

        # Display widget for current status
        self.currentWord = currentWordView()
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        # Display widget for already used characters
        self.guessedChars = guessedCharsView()
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        # Display widget for message output
        self.message = messageView()
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        # Input widget for user selected characters
        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        statusLayout.addWidget(self.charInput, 3, 0)

        # Button for submitting a character
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        statusLayout.addWidget(self.guessButton, 3, 1)

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        statusLayout.addWidget(self.newGameButton, 4, 0)

        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Hangman Game')

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = Layout()
    game.show()
    sys.exit(app.exec_())