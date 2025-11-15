#Hangman Project - Cole, Zachary, and Jace - Started Oct 27, 2025

#Needs: Word bank, Selector, Letter input calculator, Functions, (GUI?), File I/O for saving, Proper Error Handling, Distributed Workload

import random
import matplotlib.pyplot as plt

def main_menu():
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

        #Lines 23-48: Jace Dutey

        if menu_input == "1":
            print("Starting Game: ")
            file = open("Hangman_Dictionary.txt", "r")
            words = [word.strip().upper() for word in file] #brought line from previous Python project done by Zachary Tull, February 23, 2025
            chosen_word = random.choice(words)
            print("The secret wored has been chosen! \n")
            print("_ " * len(chosen_word))
            file.close()
            print(chosen_word)
        elif menu_input == "2":
            print("\n--- ADD WORDS TO DICTIONARY ---")
            print("Enter new words, one at a time. Enter 'DONE' when finished.")
    
            file = open(f"Hangman_Dictionary.txt", 'a') # Manually open for appending

            while True:
                new_word = input("Enter new word (or DONE): ").strip().lower()
        
                if new_word == "DONE":
                    break
        
                if len(new_word) > 1:
                    file.write(new_word + "\n")
                    print(f"'{new_word}' added.")
                else:
                    print("Invalid input. Please enter a word with only letters.")
    
            file.close() # Manually close the file
            print("\nDictionary update complete.")
        elif menu_input == "3":
            print("Showing Stats...")
            show_stats()
        elif menu_input == "4":
            print("\nThanks for playing! Goodbye.")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 4.")

#def show_stats: Cole Boehlert
def show_stats():    
    # whats in it
    categories = ['Wins', 'Losses']
    values = []
    color = ['gold', 'red']
    open(stats.txt, 'r') as f
    for i in f:
        f.readlines()
        values.append(f)

    f.close()    

    # presentation
    plt.bar(categories, values, color = color)
    plt.xlabel('Games')
    plt.ylabel('Rounds')
    plt.title('Hangman Graph')
    plt.show()

#brought in from previous Python project done by Zachary Tull, February 23, 2025
if __name__ == "__main__":
    # Call the main entry point of the application
    main_menu()



