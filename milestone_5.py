import random

word_list = ["mango", "grape", "coconut", "strawberry", "tomato"]
"""Word_list is a list of possible words that could be used for the game."""

class Hangman():
    """Class that represents the classic hangman game."""

    def __init__(self, word_list, num_lives=5):
        self.word_list=word_list
        self.word=random.choice(word_list)
        self.word_guessed=["_"]*len(self.word)
        self.num_letters=len(set(self.word)) 
        self.num_lives=num_lives
        self.list_of_guesses=[]

    """Class Attributes

    word: str - The word to be guessed, picked randomly from the word_list.
    word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed.
    num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.
    num_lives: int - The number of lives the player has at the start of the game.
    word_list: list - A list of words.
    list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially"""       
    
    def check_guess(self, guess):

        """Method checks to see if the answer inputed by the player matches the selected word. 
        If the answer is in the selected word, the player is informed. If the answer is not in
        the selected word, the player is informed and his lives will be reduced by one for 
        every wrong attempt."""

        guess = guess.lower()  

        if guess in self.word: 
            print("Good guess, ", guess, "is in the word!")
            for i in range(len(self.word)):
                if guess == self.word[i]: self.word_guessed[i] = guess
            self.num_letters = self.num_letters-1

        else: 
            print("Sorry,", guess, "is not in the word. Try again.")
            self.num_lives=self.num_lives-1
            print("You have", self.num_lives, "lives left.")
        pass
    
    def ask_for_input(self):

        """Method checks to see if the player input is a single and alphabetic character and informs the user 
        to retry if it does not pass the checks."""

        while True:
            guess = str(input("Guess a letter!"))
            if guess.isalpha() != True or len(guess) != 1: print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses: print("You already tried that letter!")
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
            
            

def play_game(word_list):
    """Function initiates the game and keeps track of the player's remaining lives. This function continues to run 
    either until the number of lives is 0 and the player loses the game or until the player wins the game. Player
    will be informed of either outcomes or asked to continue inputting single letters."""
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives==0:
            print ("You lost!")
            break
        if game.num_letters>0: 
            game.ask_for_input()
            print(game.word_guessed)
            continue
        if game.num_lives!=0 and game.num_letters==0:
            print("Congratulations. You won the game!")
            break

play_game(word_list) 

"""Calling this function initiates the game."""