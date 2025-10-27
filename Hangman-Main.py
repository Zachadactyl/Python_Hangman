#Hangman Project - Cole, Zachary, and Jace - Started Oct 27, 2025

#Needs: Word bank, Selector, Letter input calculator, Functions, (GUI?), File I/O for saving, Proper Error Handling, Distributed Workload

import turtle
import random


WillPlay = input("Welcome to hangman! Press |s| to start or |q| to quit.")

if WillPlay.lower() != "q":
    print("testbox")
    WillPlay = input("Welcome to hangman! Press |s| to start.")
else:
    WillPlay.lower() == "q"


