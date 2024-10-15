import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap


# main window of the application
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors Game")     # GUI title
        self.setGeometry(700, 300, 500, 500)                # GUI size

        # SCORE LABEL
        self.comp_score_label = QLabel("Computer: 0", self)            # computer score label
        self.player_score_label = QLabel("Player: 0", self)            # player score label

        # score variable
        self.comp_score = 0
        self.player_score = 0

        # MIDDLE LINE BORDER
        self.middle_border_label = QLabel("                                                                                    ", self)

        # Computer hand sign
        comp_hand = ("rock", "paper", "scissors")
        self.comp_chosen_sign = random.choice(comp_hand)
        print(f"{self.comp_chosen_sign}")

        # Create QLabel for the computer sign
        self.comp_sign_label = QLabel(self)

        # Set the appropriate pixmap based on chosen_sign
        if self.comp_chosen_sign == 'rock':
            new_pixmap = QPixmap("RPS_rock.jpeg")
        elif self.comp_chosen_sign == 'paper':
            new_pixmap = QPixmap("RPS_paper.jpeg")
        elif self.comp_chosen_sign == 'scissors':
            new_pixmap = QPixmap("RPS_scissors.jpeg")

        # Resize the pixmap and set it on the QLabel
        resized_pixmap = new_pixmap.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.comp_sign_label.setPixmap(resized_pixmap)


        # Player hand sign
        self.player_sign_label = QLabel('', self)

        # Player buttons (Rock, Paper, Scissors)
        self.rock_button = QPushButton("", self)
        self.paper_button = QPushButton("", self)
        self.scissors_button = QPushButton("", self)

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

            # score label size and positioning
        self.comp_score_label.setGeometry(0, 200, 120, 30)
        self.player_score_label.setGeometry(390, 238, 110, 30)

            # score label text alignment
        self.comp_score_label.setAlignment(Qt.AlignCenter)
        self.player_score_label.setAlignment(Qt.AlignCenter)

            # score label style
        self.comp_score_label.setStyleSheet("background-color: #03befc;"
                                       "padding: 5px;"
                                       "border-radius: 5px;")
        self.player_score_label.setStyleSheet("background-color: #fc03f0;"
                                       "padding: 5px;"
                                       "border-radius: 5px;")

            # middle line size and position
        self.middle_border_label.setGeometry(0, 200, 500, 50)

            # middle line style
        self.middle_border_label.setStyleSheet("font-weight: bold;"
                                    "text-decoration: underline;")

            # middle line alignment
        self.middle_border_label.setAlignment(Qt.AlignCenter)


            # comp hand sign position
        self.comp_sign_label.setGeometry(200, 70, 100, 100)

            # comp hand sign style
        # self.comp_sign_label.setStyleSheet("background-color: #e8e6e8;")
        self.comp_sign_label.setStyleSheet("border: 1px solid black;"
                                           "border-radius: 10px")

            # comp hand sign alignment
        self.comp_sign_label.setAlignment(Qt.AlignCenter)


            # player hand sign position
        self.player_sign_label.setGeometry(200, 300, 100, 100)

            # player hand sign style
        # self.player_sign_label.setStyleSheet("background-color: #e8e6e8;")
        self.player_sign_label.setStyleSheet("border: 1px solid black;"
                                             "border-radius: 10px")

            # player hand sign alignment
        self.player_sign_label.setAlignment(Qt.AlignCenter)


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

            # buttons position
        hbox = QHBoxLayout()
        hbox.setContentsMargins(30, 420, 30, 10)  # Left, top, right, bottom margins

        hbox.addWidget(self.rock_button)
        hbox.addWidget(self.paper_button)
        hbox.addWidget(self.scissors_button)

        central_widget.setLayout(hbox)

            # Set fixed sizes for each button
        self.rock_button.setFixedSize(80, 80)
        self.paper_button.setFixedSize(80, 80)
        self.scissors_button.setFixedSize(80, 80)

            # button signals
        self.rock_button.clicked.connect(self.rock_on_click)
        self.paper_button.clicked.connect(self.paper_on_click)
        self.scissors_button.clicked.connect(self.scissors_on_click)

    # button methods
    def rock_on_click(self):
        new_pixmap = QPixmap("RPS_rock.jpeg")
        resized_pixmap = new_pixmap.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.player_sign_label.setPixmap(resized_pixmap)

        if self.comp_chosen_sign == "rock":
            print("rock")
            print("It's a tie!")
        elif "rock" and self.comp_chosen_sign == "scissors":
            print("You win!")
            self.player_score += 1
        else:
            print("You lose!")
            self.comp_score += 1

        print(f"Computer score: {self.comp_score}")
        print(f"Player score: {self.player_score}")

    def paper_on_click(self):
        new_pixmap = QPixmap("RPS_paper.jpeg")
        resized_pixmap = new_pixmap.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.player_sign_label.setPixmap(resized_pixmap)

        if self.comp_chosen_sign == "paper":
            print("paper")
            print("It's a tie!")
        elif "paper" and self.comp_chosen_sign == "rock":
            print("You win!")
            self.player_score += 1
        else:
            print("You lose!")
            self.comp_score += 1

        print(f"Computer score: {self.comp_score}")
        print(f"Player score: {self.player_score}")

    def scissors_on_click(self):
        new_pixmap = QPixmap("RPS_scissors.jpeg")
        resized_pixmap = new_pixmap.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.player_sign_label.setPixmap(resized_pixmap)

        if self.comp_chosen_sign == "scissors":
            print("scissors")
            print("It's a tie!")
        elif "scissors" and self.comp_chosen_sign == "paper":
            print("You win!")
            self.player_score += 1
        else:
            print("You lose!")
            self.comp_score += 1

        print(f"Computer score: {self.comp_score}")
        print(f"Player score: {self.player_score}")

    def batobatopik(self):
        if self.comp_sign_label == self.player_sign_label:
            print("It's a tie!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()