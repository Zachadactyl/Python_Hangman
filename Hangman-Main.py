#Hangman Project - Cole, Zachary, and Jace - Started Oct 27, 2025

#Needs: Word bank, Selector, Letter input calculator, Functions, (GUI?), File I/O for saving, Proper Error Handling, Distributed Workload

import turtle
import random

file = open("Hangman_Dictionary.txt", "r")

def main_menu():
    """Manages the user interface and routes to different functions."""
    current_word_bank = load_word_bank(WORD_BANK_FILE)
    
    print("Welcome to Command-Line Hangman!")
    
    while True:
        print("\n" + "="*30)
        print("MAIN MENU:")
        print("1. Start New Game")
        print("2. Add Words to Dictionary")
        print("3. Show Stats")
        print("4. Quit")
        print("="*30)
        
        choice = input("Enter option number (1-4): ").strip()
        
        if choice == '1':
            start_new_game(current_word_bank)
            
        elif choice == '2':
            current_word_bank = add_words_to_bank(WORD_BANK_FILE)
            
        elif choice == '3':
            show_stats(current_word_bank)
            
        elif choice == '4':
            print("\nThanks for playing! Goodbye.")
            
        else:
            print("Invalid option. Please choose a number from 1 to 4.")

words = [word.strip().upper() for word in file]
chosen_word = random.choice(words)
print("The secret wored has been chosen!")
print("_ " * len(chosen_word))

file.close()
if __name__ == "__main__":
    # Call the main entry point of the application
    main_menu()
