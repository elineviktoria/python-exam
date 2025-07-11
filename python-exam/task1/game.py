import random

class WordGuessingGame:
    """
    A class that represents and manages the Word Guessing Game
    """

    def __init__(self, word_file_path = "wordlist.txt"):
        """
        Constructor for the WordGuessingGame class
        
        """
        self.word_file_path = word_file_path
        self.word_list = []
        self.secret_word = ""
        self.displayed_letters = []
        self.guesses_made = set()
        self.num_wrong_guesses = 0
        self.max_wrong_guesses = 0

        self._load_words() # private helper method to laod words
        if self.word_list:
            self._setup_new_game()
        else:
            # if word_list is empty, secret_word will remain empty and run_game methos will handle this
            print("Error: No words loaded. Ensure 'wordlist.txt' exists and is not empty.")
        
    def _load_words(self):
        """
        Loads words from the text file by self.word_file_path, handles potential file errors
        """
        try:
            infile = open(self.word_file_path, "r")
            for line in infile:
                word = line.strip().upper()
                if word: # only add non-empty words
                    self.word_list.append(word)
            infile.close() # close file

            if not self.word_list:
                print(f"Warning: Word list from '{self.word_file_path}' is empty or contains only blank lines.")
        except IOError:
            print(f"Error: The file '{self.word_file_path}' was not found or could not be read.")
            self.word_list = [] # word_list is empty if file loading fails

    def _setup_new_game(self):
        """
        Selects a new secret word and resets the game state
        """
        if not self.word_list:
            self.secret_word = "" # ensure secret_word is empty if no words
            return
        
        # select random word using random.randint (L4)
        random_index = random.randint(0, len(self.word_list) - 1)
        self.secret_word = self.word_list[random_index]

        # initialize displayed_letters with underscores
        self.displayed_letters = ["_"] * len(self.secret_word)

        self.max_wrong_guesses = len(self.secret_word)
        self.num_wrong_guesses = 0
        self.guesses_made = set() # reset for a new game
        print(f"DEBUG: Secret word is {self.secret_word}") # for testing (comment out)


    def _display_status(self):
        """
        Displays the current game status to the player
        """
        # build the string for hidden word
        word_display_list = []
        for char in self.displayed_letters:
            word_display_list.append(char)

        # print the word wit spaces and underscore
        display_string = ""
        for char in self.displayed_letters:
            display_string += char + " "
        print(display_string.rstrip())

        # remaining guesses
        guesses_left = self.max_wrong_guesses - self.num_wrong_guesses
        guesses_text = "guess" if guesses_left == 1 else "guesses"
        print(f"You have {guesses_left} {guesses_text} left.")

        print("----------------------------")


    def _get_player_guess(self):
        """
        Gets a valid letter guess from the player
        """
        while True:
            guess = input("Guess a character: ").strip().upper()

            if len(guess) != 1:
                print("Invalid input. Please enter a single letter.")
            elif not guess.isalpha(): # NB: isalpha()???
                print("Invalid input. Please enter a letter (A-Z).")
            elif guess in self.guesses_made: # check if letter was already guessed
                print(f"You have already guessed '{guess}'. Try a different letter.")
            else:
                return guess # valid guess
            
    
    def _process_guess(self, guess):
        """
        Processes the player's guess, updates game state
        Return true if the guess was correct, false otherwise
        """
        self.guesses_made.add(guess) # add to set og made guesses

        if guess in self.secret_word: 
            # correct guess - iterate with indec to update displayed_letters
            for i in range(len(self.secret_word)):
                if self.secret_word[i] == guess:
                    self.displayed_letters[i] = guess
            return True
        else:
            # incorrect guess
            self.num_wrong_guesses += 1
            return False

    def _is_won(self):
        """
        Checks if the player has won the game
        """
        return "_" not in self.displayed_letters # list "in" operator
    
    def _is_lost(self):
        """
        Checks if the player has lost the game
        """
        return self.num_wrong_guesses >= self.max_wrong_guesses
    
    def run_game(self):
        """
        Runs the main game loop
        """
        if not self.secret_word: # check if secret word was successfully set up
            print("Game cannot start. No secret word available. Check 'wordlist.txt'.")
            return
        
        print("Welcome to the Word Guessing Game!")
        print(f"The word you need to guess has {len(self.secret_word)} characters.")

        # Main game loop
        while True:
            self._display_status() # shows status
            current_guess_prompt = "Guess a character: "
            guess = ""
            guess = self._get_player_guess()
            
            is_correct = self._process_guess(guess)

            if is_correct:
                pass
            else:
                print(f"Sorry, that letter is not in the word.")

            if self._is_won():
                final_word_display_str = ""
                for char_in_word in self.displayed_letters:
                    final_word_display_str += char_in_word + " "
                print(final_word_display_str.rstrip())

                print(f"You found the word --> \"{self.secret_word}\"")
                print("Congratulations! You won")
                break

            elif self._is_lost():
                print("\nGame over!")
                print(f"You ran out of guesses. The word was: {self.secret_word}")
                break
            

# --- Main part of script to run the game ---
if __name__ == "__main__":
    play_again = True
    while play_again:
        # create an object of the WordGuessingGame class
        game = WordGuessingGame(word_file_path="wordlist.txt")
        # call the run_game method on the object
        game.run_game()

        while True:
            user_choice = input("Do you want to play again? (yes/no): ").strip().lower()
            if user_choice == "yes" or user_choice == "y":
                break
            elif user_choice == "no" or user_choice == "n":
                play_again = False
                print("Thank you for playing!")
                break
            else:
                print("Invalid input. Please answer 'yes' or 'no'.")
