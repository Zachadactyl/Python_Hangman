# Hangman Project - Cole, Zachary, and Jace - Started Oct 27, 2025

# Needs: Word bank, Selector, Letter input calculator, Functions, (GUI?), File I/O for saving, Proper Error Handling, Distributed Workload

import random
import matplotlib.pyplot as plt
from functions_file import start_game, DICTIONARY_FILE, show_stats, add_words_to_dictionary, load_and_update_stats, MAX_INCORRECT_GUESSES, STATS_FILE
def main_menu():
    """The main entry point for the Hangman game application."""
    print("Welcome to Command-Line Hangman! Choose an option to continue... \n")
    while True:
        print("\n" + "="*30)
        print("MAIN MENU:")
        print("1. Start New Game")
        print("2. Add Words to Dictionary")
        print("3. Show Stats")
        print("4. Quit")
        print("="*30)
        
        menu_input = input("Enter option number (1-4): ").strip()

        if menu_input == "1":
            try:
                # Use 'with open' for safe file handling
                # FIX APPLIED HERE: The path is updated using the constant.
                with open(DICTIONARY_FILE, "r") as file: 
                    # Filter out empty lines and convert to uppercase
                    words = [word.strip().upper() for word in file if word.strip()] 
                
                if not words:
                    print("\nError: The dictionary is empty. Please add words using Option 2.")
                    continue
                
                chosen_word = random.choice(words)
                start_game(chosen_word)
                
            except FileNotFoundError:
                # Modified message to explain the path issue.
                print(f"\nError: Dictionary file ({DICTIONARY_FILE}) not found. Make sure the file is in the '{DICTIONARY_FILE.split('/')[0]}' folder and try option 2 to add words.")
            except Exception as e:
                 print(f"An unexpected error occurred: {e}")
                
        elif menu_input == "2":
            add_words_to_dictionary()
            
        elif menu_input == "3":
            show_stats()
            
        elif menu_input == "4":
            print("\nThanks for playing! Goodbye.")
            break
            
        else:
            print("Invalid option. Please choose a number from 1 to 4.")

# Entry point
if __name__ == "__main__":
    # Call the main entry point of the application
    main_menu()