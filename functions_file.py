import random
import sys

# --- CONFIGURATION ---
WORD_BANK_FILE = "Hangman_Dictionary.txt"
STATS_FILE = "stats.txt" 
MAX_INCORRECT_GUESSES = 6 

# --- 1. FILE I/O AND SELECTOR FUNCTIONS ---

def load_word_bank(filename):
    """
    Loads all words from the specified file into a list.
    WARNING: Will raise FileNotFoundError if the file does not exist.
    """
    with open(filename, 'r') as file:
        words = [word.strip().upper() for word in file if word.strip()]
    
    if not words:
        return ["PYTHON", "HANGMAN", "CODE"]
        
    return words


def add_words_to_bank(filename):
    """
    Allows the user to enter words to be added to the dictionary file.
    WARNING: Will raise an IOError if the file cannot be written.
    """
    print("\n--- ADD WORDS TO DICTIONARY ---")
    print("Enter new words, one at a time. Enter 'DONE' when finished.")
    
    with open(filename, 'a') as file:
        while True:
            new_word = input("Enter new word (or DONE): ").strip().upper()
            
            if new_word == "DONE":
                break
            
            if new_word.isalpha() and len(new_word) > 1:
                file.write(new_word + "\n")
                print(f"'{new_word}' added.")
            else:
                print("⚠️ Invalid input. Please enter a word with only letters.")
    
    print("\nDictionary update complete.")
    return load_word_bank(filename)


# --- 2. STATS I/O (Error Handling Removed) ---

def load_and_update_stats(result):
    """
    Loads stats, updates them based on the game result ('W' or 'L'), and saves the file.
    WARNING: Will raise FileNotFoundError if stats.txt doesn't exist.
    """
    
    # Initialize default stats (used only if file loading is skipped or fails externally)
    stats = {"WINS": 0, "LOSSES": 0}

    # 1. Load existing stats (Reading the file)
    # This assumes stats.txt *exists* and is formatted correctly.
    with open(STATS_FILE, 'r') as f:
        for line in f:
            if ':' in line:
                key, value = line.split(':', 1)
                stats[key.strip()] = int(value.strip())
        
    # 2. Update stats based on result (if a game was just played)
    if result == 'W':
        stats["WINS"] += 1
    elif result == 'L':
        stats["LOSSES"] += 1
    elif result is None:
        # If result is None, we just loaded the stats, no update needed, return existing values
        return stats
        
    # 3. Write back to the file
    with open(STATS_FILE, 'w') as f:
        f.write(f"WINS: {stats['WINS']}\n")
        f.write(f"LOSSES: {stats['LOSSES']}\n")

    return stats

def show_stats(word_list):
    """Loads and displays the game statistics."""
    # Note: If stats.txt doesn't exist, this function will raise FileNotFoundError
    stats = load_and_update_stats(None) 
    
    print("\n--- GAME STATS ---")
    print(f"Total words currently in dictionary: {len(word_list)}")
    print(f"Games Won: {stats['WINS']}")
    print(f"Games Lost: {stats['LOSSES']}")
    total_games = stats['WINS'] + stats['LOSSES']
    if total_games > 0:
        win_rate = (stats['WINS'] / total_games) * 100
        print(f"Win Rate: {win_rate:.2f}%")
    else:
        print("No games played yet.")


# --- 3. GAME INPUT AND VISUALS ---

def get_user_guess(guessed_letters):
    """Prompts the user for a letter and validates the input."""
    while True:
        user_input = input("Guess a letter: ").strip().upper()
        
        if not user_input.isalpha() or len(user_input) != 1:
            print("⚠️ Error: Please enter **exactly one letter** (A-Z).")
        elif user_input in guessed_letters:
            print(f"You already guessed '{user_input}'. Try a new letter.")
        else:
            return user_input

def draw_hangman(incorrect_guesses):
    """Shows the hangman state based on incorrect guesses."""
    remaining = MAX_INCORRECT_GUESSES - incorrect_guesses
    print(f"[Placeholder] Hangman State: {incorrect_guesses} incorrect guesses (You have {remaining} left)")


# --- 4. MAIN GAME LOGIC (Updated to save stats) ---

def start_new_game(word_list):
    """The main gameplay loop where the user guesses letters."""
    if not word_list:
        print("Cannot start game: No words available.")
        return

    secret_word = random.choice(word_list)
    word_length = len(secret_word)
    
    display = ['_' for _ in secret_word]
    guessed_letters = set()
    incorrect_guesses = 0
    
    print(f"\n--- STARTING GAME ---")
    print(f"The secret word has {word_length} letters. Good luck!")

    # --- MAIN GAME LOOP ---
    while incorrect_guesses < MAX_INCORRECT_GUESSES and "_" in display:
        
        print("\n" + "="*35)
        draw_hangman(incorrect_guesses)
        print(f"Word: {' '.join(display)}")
        print(f"Guessed Letters: {', '.join(sorted(list(guessed_letters)))}")
        
        guess = get_user_guess(guessed_letters)
        guessed_letters.add(guess)
        
        if guess in secret_word:
            print("🎉 Correct guess!")
            for i in range(word_length):
                if secret_word[i] == guess:
                    display[i] = guess
        else:
            print("❌ Incorrect guess.")
            incorrect_guesses += 1
    
    # --- GAME OVER CONDITIONS ---
    print("\n" + "#"*35)
    if "_" not in display:
        print(f"🎉 **CONGRATULATIONS!** You guessed the word: **{secret_word}**")
        load_and_update_stats('W') 
    else:
        draw_hangman(incorrect_guesses)
        print("💀 **GAME OVER!** You ran out of guesses.")
        print(f"The word was: **{secret_word}**")
        load_and_update_stats('L')
    print("#"*35)


# --- 5. MAIN MENU LOOP ---

def main_menu():
    """Manages the user interface and routes to different functions."""
    # WARNING: This will crash if Hangman_Dictionary.txt does not exist
    current_word_bank = load_word_bank(WORD_BANK_FILE)
    
    print("✨ Welcome to Command-Line Hangman! ✨")
    
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
            sys.exit(0)
            
        else:
            print("⚠️ **Invalid option.** Please choose a number from 1 to 4.")