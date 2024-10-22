import sys
import random
from time import sleep

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QWidget,
                             QVBoxLayout, QHBoxLayout, QBoxLayout, QGridLayout, QMessageBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap


# main window of the application
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors Game")     # GUI title
        self.setGeometry(700, 300, 500, 500)                # GUI size

        # SCORE LABEL
        self.comp_label = QLabel("Computer", self)
        self.player_label = QLabel("You", self)
        self.comp_score_label = QLabel("0", self)            # computer score label
        self.player_score_label = QLabel("0", self)            # player score label

        # score variable
        self.comp_score = 0
        self.player_score = 0

        # MIDDLE LINE BORDER
        self.middle_border_label = QLabel("                                                                                    ", self)

        # play hand sign
        self.player_chosen_sign = ''

        # Computer hand sign
        comp_hand = ("rock", "paper", "scissors")
        self.comp_chosen_sign = random.choice(comp_hand)

        # Create QLabel for the computer sign
        self.comp_sign_label = QLabel(self)

        # Player hand sign
        self.player_sign_label = QLabel('', self)

        # Player buttons (Rock, Paper, Scissors)
        self.rock_button = QPushButton("", self)
        self.paper_button = QPushButton("", self)
        self.scissors_button = QPushButton("", self)

        # Go! button
        self.go_btn = QPushButton("Go!", self)

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

            # score label size and positioning
        self.comp_label.setGeometry(5, 200, 100, 30)
        self.player_label.setGeometry(395, 238, 100, 30)
        self.comp_score_label.setGeometry(5, 106, 100, 100)
        self.player_score_label.setGeometry(395, 262, 100, 100)

            # score label text alignment
        self.comp_label.setAlignment(Qt.AlignCenter)
        self.player_label.setAlignment(Qt.AlignCenter)
        self.comp_score_label.setAlignment(Qt.AlignCenter)
        self.player_score_label.setAlignment(Qt.AlignCenter)

            # score label style
        self.comp_label.setStyleSheet("background-color: #03befc;"
                                        "padding: 5px;"
                                        "border-radius: 5px;"
                                        "font-size: 20px;"
                                        "font-family: calibri;"
                                        )
        self.player_label.setStyleSheet("background-color: #fc03f0;"
                                        "padding: 5px;"
                                        "border-radius: 5px;"
                                        "font-size: 20px;"
                                        "font-family: calibri;"
                                        )

        self.comp_score_label.setStyleSheet("background-color: #03befc;"
                                        "padding: 5px;"
                                        "border-radius: 5px;"
                                        "font-size: 90px;"
                                        "font-family: calibri;")
        self.player_score_label.setStyleSheet("background-color: #fc03f0;"
                                        "padding: 5px;"
                                        "border-radius: 5px;"
                                        "font-size: 90px;"
                                        "font-family: calibri;")

            # middle line size and position
        self.middle_border_label.setGeometry(0, 200, 500, 50)

            # middle line style
        self.middle_border_label.setStyleSheet("font-weight: bold;"
                                    "text-decoration: underline;")

            # middle line alignment
        self.middle_border_label.setAlignment(Qt.AlignCenter)

            # comp hand sign position
        self.comp_sign_label.setGeometry(150, 10, 200, 200)

            # comp hand sign alignment
        self.comp_sign_label.setAlignment(Qt.AlignCenter)

            # comp hand sign style
        # self.comp_sign_label.setStyleSheet("background-color: #e8e6e8;")
        # self.comp_sign_label.setStyleSheet("border: 1px solid black;"
        #                                    "border-radius: 10px")

            # player hand sign position
        self.player_sign_label.setGeometry(150, 240, 200, 200)

            # player hand sign alignment
        self.player_sign_label.setAlignment(Qt.AlignCenter)

            # player hand sign style
        # self.player_sign_label.setStyleSheet("background-color: #e8e6e8;")
        # self.player_sign_label.setStyleSheet("border: 1px solid black;"
        #                                      "border-radius: 10px")

            # rock button icon
        self.rock_button.setIcon(QIcon("RPS_rock.jpeg"))
        self.rock_button.setIconSize(self.rock_button.sizeHint())
        self.rock_button.setIconSize(QSize(60, 60))

            # paper button icon
        self.paper_button.setIcon(QIcon("RPS_paper.jpeg"))
        self.paper_button.setIconSize(self.paper_button.sizeHint())
        self.paper_button.setIconSize(QSize(60, 60))

            # scissors button icon
        self.scissors_button.setIcon(QIcon("RPS_scissors.jpeg"))
        self.scissors_button.setIconSize(self.scissors_button.sizeHint())
        self.scissors_button.setIconSize(QSize(60, 60))

            # player button layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.rock_button)
        hbox.addWidget(self.paper_button)
        hbox.addWidget(self.scissors_button)
        hbox.setContentsMargins(30, 420, 30, 10)  # Left, top, right, bottom margins

            # go button layout
        go_btn_layout = QVBoxLayout()
        go_btn_layout.addWidget(self.go_btn)

        # Add both layouts to a main vertical layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(hbox)  # Existing layout for the Rock, Paper, Scissors buttons
        main_layout.addLayout(go_btn_layout)  # New layout for the Go button
        main_layout.setAlignment(Qt.AlignCenter)

        central_widget.setLayout(main_layout)

        # Set fixed sizes for each button
        self.rock_button.setFixedSize(80, 80)
        self.paper_button.setFixedSize(80, 80)
        self.scissors_button.setFixedSize(80, 80)
        self.go_btn.setFixedSize(350, 40)

            # player button signals
        self.rock_button.clicked.connect(self.rock_on_click)
        self.paper_button.clicked.connect(self.paper_on_click)
        self.scissors_button.clicked.connect(self.scissors_on_click)

            # go button size & position
        # self.go_btn.setGeometry(345, 315, 90, 70)

            # go btn style
        self.go_btn.setStyleSheet("font-size: 25px;"
                                  "font-family: calibri;"
                                  )

            # go btn signal
        self.go_btn.clicked.connect(self.go_btn_on_click)


    # button methods
    def rock_on_click(self):
        new_pixmap = QPixmap("RPS_rock.jpeg")
        resized_pixmap = new_pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.player_sign_label.setPixmap(resized_pixmap)

        self.player_chosen_sign = "rock"

    def paper_on_click(self):
        new_pixmap = QPixmap("RPS_paper.jpeg")
        resized_pixmap = new_pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.player_sign_label.setPixmap(resized_pixmap)

        self.player_chosen_sign = "paper"

    def scissors_on_click(self):
        new_pixmap = QPixmap("RPS_scissors.jpeg")
        resized_pixmap = new_pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.player_sign_label.setPixmap(resized_pixmap)

        self.player_chosen_sign = "scissors"

    def go_btn_on_click(self):

        # message box display to tell who won each round
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        # Compare the player's chosen sign with the computer's chosen sign
        if self.player_chosen_sign == self.comp_chosen_sign:
            # print("It's a tie!")
            msg.setText(f"It's a tie! Player: {self.player_score} | Computer: {self.comp_score}")     # msgbox if tie
        elif (self.player_chosen_sign == "rock" and self.comp_chosen_sign == "scissors") or \
                (self.player_chosen_sign == "scissors" and self.comp_chosen_sign == "paper") or \
                (self.player_chosen_sign == "paper" and self.comp_chosen_sign == "rock"):
            self.player_score += 1
            msg.setText(f"Player win! Player: {self.player_score} | Computer: {self.comp_score}")     # msgbox if player win
        else:
            self.comp_score += 1
            msg.setText(f"Computer win! Player: {self.player_score} | Computer: {self.comp_score}")   # msgbox if comp win

        # Update the score labels to reflect the new scores
        self.comp_score_label.setText(f"{self.comp_score}")
        self.player_score_label.setText(f"{self.player_score}")

        if self.comp_chosen_sign == 'rock':
            new_pixmap = QPixmap("RPS_rock.jpeg")
        elif self.comp_chosen_sign == 'paper':
            new_pixmap = QPixmap("RPS_paper.jpeg")
        elif self.comp_chosen_sign == 'scissors':
            new_pixmap = QPixmap("RPS_scissors.jpeg")

        # Resize the pixmap and set it on the QLabel
        resized_pixmap = new_pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.comp_sign_label.setPixmap(resized_pixmap)

        msg.setWindowTitle("RPS")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        # checks who got 5 scores
        if self.player_score == 5:
            self.game_over()
        elif self.comp_score == 5:
            self.game_over()
        else:
            sleep(1)
            self.reset_game()

    def reset_game(self):
        # Clear the player and computer hand signs
        self.player_chosen_sign = ''
        self.comp_chosen_sign = ''

        # Clear the pixmaps from the sign labels
        self.player_sign_label.clear()
        self.comp_sign_label.clear()

        # Re-select a new hand for the computer each round
        comp_hand = ("rock", "paper", "scissors")
        self.comp_chosen_sign = random.choice(comp_hand)


    def game_over(self):

        # Game over msgbox
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        if self.player_score == 5:
            msg.setText("Congratulations, player. You win!\n\nDo you want to play again?")       # msgbox if player win
        elif self.comp_score == 5:
            msg.setText("Sorry player, computer Win!\n\nDo you want to play again?")           # msgbox if comp win
        msg.setWindowTitle("Game over")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = msg.exec_()
        if retval == QMessageBox.Yes:
            # reset scores
            self.player_score = 0
            self.comp_score = 0
            self.player_score_label.setText("0")
            self.comp_score_label.setText("0")
            self.reset_game()  # Call your reset function here
        else:
            # close the main window
            MainWindow.close(self)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()