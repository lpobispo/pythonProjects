import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtCore import Qt

# main window of the application
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors Game")     # GUI title
        self.setGeometry(700, 300, 500, 500)                # GUI size
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # SCORE LABEL
        comp_score_label = QLabel("Computer: 0", self)            # computer score label
        player_score_label = QLabel("Player: 0", self)            # player score label

            # size and positioning
        comp_score_label.setGeometry(0, 0, 120, 50)
        player_score_label.setGeometry(390, 450, 110, 50)

            # text alignment
        comp_score_label.setAlignment(Qt.AlignCenter)
        player_score_label.setAlignment(Qt.AlignCenter)

            # style
        comp_score_label.setStyleSheet("background-color: #03befc;"
                                       "padding: 5px;"
                                       "border-radius: 5px;")
        player_score_label.setStyleSheet("background-color: #fc03f0;"
                                       "padding: 5px;"
                                       "border-radius: 5px;")

        # LINE BORDER
        middle_border_label = QLabel("                                                                                    ", self)

            # size and position
        middle_border_label.setGeometry(0, 200, 500, 50)

            # style
        middle_border_label.setStyleSheet("font-weight: bold;"
                                    "text-decoration: underline;")

            # alignment
        middle_border_label.setAlignment(Qt.AlignCenter)


        # SIGN (Computer)
        comp_sign_label = QLabel("XXXXXXXXX\nXXXXXXXXX\nXXXXXXXXX", self)

            # position
        comp_sign_label.setGeometry(200, 70, 100, 100)

            # style
        comp_sign_label.setStyleSheet("background-color: #e8e6e8;")

            # alignment
        comp_sign_label.setAlignment(Qt.AlignCenter)


        # SIGN (Player)
        player_sign_label = QLabel("XXXXXXXXX\nXXXXXXXXX\nXXXXXXXXX", self)

            # position
        player_sign_label.setGeometry(200, 300, 100, 100)

            # style
        player_sign_label.setStyleSheet("background-color: #e8e6e8;")

            # alignment
        player_sign_label.setAlignment(Qt.AlignCenter)

        # BUTTONS (Rock, Paper, Scissors)
        rock_button = QPushButton("ROCK", self)
        paper_button = QPushButton("PAPER", self)
        scissors_button = QPushButton("SCISSORS", self)

            # horizontally aligned
        hbox = QHBoxLayout()
        hbox.setContentsMargins(30, 350, 30, 10)  # Left, top, right, bottom margins

        hbox.addWidget(rock_button)
        hbox.addWidget(paper_button)
        hbox.addWidget(scissors_button)

        central_widget.setLayout(hbox)

            # Set fixed sizes for each button
        rock_button.setFixedSize(100, 40)
        paper_button.setFixedSize(100, 40)
        scissors_button.setFixedSize(100, 40)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()