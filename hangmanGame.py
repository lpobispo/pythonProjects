# Hangman game in Python

import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" O ",
                   "   ",
                   "   "),
               2: (" O ",
                   " | ",
                   "   "),
               3: (" O ",
                   "/| ",
                   "   "),
               4: (" O ",
                   "/|\\",
                   "   "),
               5: (" O ",
                   "/|\\",
                   "/  "),
               6: (" O ",
                   "/|\\",
                   "/'\\")}

print(words)