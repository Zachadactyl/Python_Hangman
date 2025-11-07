#Hangman Project - Cole, Zachary, and Jace - Started Oct 27, 2025

#Needs: Word bank, Selector, Letter input calculator, Functions, (GUI?), File I/O for saving, Proper Error Handling, Distributed Workload

import turtle
import random

from word import Hangman_Dictionary.txt
chosen_word = random.choice(Hangman.Dictionary.txt)
print("The secret wored has been chosen!")
print("_ " * len(chosen_word))


file = open("Hangman_Dictionary.txt", "r")

WillPlay = input("Welcome to hangman! Press |s| to start or |q| to quit. ")

while WillPlay.lower() != "q":
    line = file.readline()
    print(line)
    WillPlay = input("Welcome to hangman! Press |s| to start or |q| to quit. ")



