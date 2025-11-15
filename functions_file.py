# Hangman Project - Cole, Zachary, and Jace - Started Oct 27, 2025

# Needs: Word bank, Selector, Letter input calculator, Functions, (GUI?), File I/O for saving, Proper Error Handling, Distributed Workload

import random
import matplotlib.pyplot as plt

# --- GAME CONSTANTS ---
STATS_FILE = "stats.txt" # File to store wins and losses history (e.g., WWLWL)
# FIX: The file path must include the subfolder name where the file is located.
DICTIONARY_FILE = "Python_Hangman/Hangman_Dictionary.txt" 
MAX_INCORRECT_GUESSES = 6 # Maximum number of incorrect guesses allowed

# --- GAME VISUALS ---

def draw_hangman(incorrect_guesses):
    """Shows a simplified text-based hangman state."""
    # Stages are shown from 0 misses (index 6) up to 6 misses (index 0)
    stages = [  
        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """, # 6 misses (Game Over)
        """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """, # 5 misses
        """
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        """, # 4 misses
        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """, # 3 misses
        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """, # 2 misses
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """, # 1 miss
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """  # 0 misses (Gallows only)
    ]
    
    stage_index = MAX_INCORRECT_GUESSES - incorrect_guesses
    print(stages[stage_index])
    
# --- GAME INPUT ---
def get_user_guess(guessed_letters):
    """Prompts the user for a letter and validates the input (SIMPLIFIED)."""
    while True:
        user_input = input("Guess a letter: ").strip().upper()
        
        # Simplified: check only if it's exactly one character
        if len(user_input) != 1:
            print("Error: Please enter exactly one character (like 'A').")
        elif user_input in guessed_letters:
            print(f"You already guessed '{user_input}'. Try a new letter.")
        else:
            return user_input

# --- STATS HANDLING (SIMPLIFIED AND CLEANED) ---
def load_and_update_stats(result=None):
    """
    Loads all previous game results ('W' or 'L') and appends the new result 
    to the stats file for easy plotting of history.
    Returns: (stats_count, history_list) 
    """
    history = []
    
    # 1. Load existing history (read the file)
    try:
        # Open the file for reading ('r')
        with open(STATS_FILE, 'r') as stats_file: 
            content = stats_file.read().strip()
            # This makes a list like ['W', 'L', 'W', 'W']
            history = [r for r in content if r in ('W', 'L')] 
            
    except FileNotFoundError:
        # File doesn't exist yet, history remains empty.
        pass
        
    # 2. Update and append to file if a new result is given
    if result in ('W', 'L'):
        try:
            # Open the file for appending ('a') to add the new result to the end
            with open(STATS_FILE, 'a') as stats_file:
                stats_file.write(result) 
                history.append(result) 
                
        except Exception as e:
            print(f"Error writing new stats file: {e}")
        
    stats = {"WINS": history.count('W'), "LOSSES": history.count('L')}
    return stats, history # Return counts and the history list

# --- CORE GAME LOGIC ---
def start_game(chosen_word):
    """
    Handles the main game loop, including guesses, tracking, and win/loss conditions.
    """
    # Renamed internal variable for consistency
    
    # Variables for the game state
    display = ['_' for _ in chosen_word]
    guessed_letters = set() # Set is used to prevent duplicate guesses
    incorrect_guesses = 0

    print("\n" + "=" * 40)
    print("THE GAME IS STARTING!")

    # --- MAIN GAME LOOP ---
    while incorrect_guesses < MAX_INCORRECT_GUESSES and "_" in display:

        print("\n" + "-"*40)
        draw_hangman(incorrect_guesses)
        # ' '.join(display) is the simple way to show the word with spaces (e.g., "_ A _")
        print(f"Word: {' '.join(display)}") 
        print(f"Guessed Letters: {', '.join(sorted(list(guessed_letters)))}")

        # Get and validate the user's guess
        guess = get_user_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in chosen_word:
            print("Correct guess! Good job!")
            # Update the display word
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess
        else:
            print("Incorrect guess. The letter is not in the word.")
            incorrect_guesses += 1

    # --- GAME OVER CONDITIONS ---
    print("\n" + "#"*40)
    print(f"The word was: {chosen_word}")
    
    if "_" not in display:
        print("CONGRATULATIONS! You won!")
        load_and_update_stats('W') # Update stats file with 'W'
        return True
    else:
        draw_hangman(incorrect_guesses) # Show the final, dead hangman
        print("GAME OVER! You ran out of guesses.")
        load_and_update_stats('L') # Update stats file with 'L'
        return False
    print("#"*40)


# --- UTILITY FUNCTIONS ---

def add_words_to_dictionary():
    """Handles adding new words to the Hangman dictionary file (SIMPLIFIED)."""
    print("\n--- ADD WORDS TO DICTIONARY ---")
    print("Enter new words, one at a time. Enter 'DONE' when finished.")

    try:
        # Using 'a' mode creates the file if it doesn't exist and appends new lines
        with open(DICTIONARY_FILE, 'a') as file: # Path updated to DICTIONARY_FILE constant
            while True:
                new_word = input("Enter new word (or DONE): ").strip().lower()

                if new_word == "done":
                    break

                # Simplified validation: check only for length > 1
                if len(new_word) > 1:
                    # Write in lowercase to keep dictionary consistent
                    file.write(new_word + "\n") 
                    print(f"'{new_word.upper()}' added.")
                else:
                    # Simplified error message
                    print("Invalid input. Please enter a word with at least 2 characters.")
        print("\nDictionary update complete.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


# def show_stats: Cole Boehlert
#def show_stats():
#    """Loads, displays, and plots game statistics (W/L ratio) progression."""
#    # Load dictionary words to get total count
#    try:
#        with open(DICTIONARY_FILE, "r") as file: # Path updated to DICTIONARY_FILE constant
#            # Filter out empty lines and convert to uppercase
#            word_list = [word.strip() for word in file if word.strip()]
#    except FileNotFoundError:
#        word_list = []
#        
#    # Get stats counts and the full history list
#    stats, history = load_and_update_stats() 
#    total_games = stats['WINS'] + stats['LOSSES']
#    
#    print("\n--- GAME STATS ---")
#    print(f"Total words currently in dictionary: {len(word_list)}")
#    print(f"Games Won: {stats['WINS']}")
#    print(f"Games Lost: {stats['LOSSES']}")
#    
#    if total_games > 0:
#        win_rate = (stats['WINS'] / total_games) * 100
#        print(f"Win Rate: {win_rate:.2f}%")
#        
#        # --- Simplified Plotting for Progression ---
#        # Create numerical lists for plotting progression
#        wins_y = []
#        losses_y = []
#        current_wins = 0
#        current_losses = 0
#        
#        # Calculate cumulative wins and losses after each game
#        for result in history:
#            if result == 'W':
#                current_wins += 1
#            elif result == 'L':
#                current_losses += 1
#           wins_y.append(current_wins)
#            losses_y.append(current_losses)
#
#        game_numbers = list(range(1, total_games + 1))
#        
#        plt.title("Hangman Game Progression (Cumulative)")
#        plt.xlabel("Game Number")
#        plt.ylabel("Cumulative Wins/Losses")
3        
#        # Plotting total wins vs losses over time
#        plt.plot(game_numbers, wins_y, label='Wins', color='green', marker='o')
#        plt.plot(game_numbers, losses_y, label='Losses', color='red', marker='x')
#        plt.legend()
#        plt.grid(True)
#        plt.show()
#
#    else:
#        print("No games played yet. Get guessing!")