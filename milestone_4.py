import random
import numpy
word_list = ["mango", "grape", "coconut", "strawberry", "tomato"]
class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word_list=word_list
        self.word=random.choice(word_list)
        self.word_guessed=["_"]*len(self.word)
        self.num_letters=numpy.unique(self.word)
        self.num_lives=num_lives
        self.list_of_guesses=[]
    
    def check_guess(self, guess):
        guess = guess.lower()    
        if guess in self.word: 
            print("Good guess, ", guess, "is in the word!")
            for i in len(self.word):
                if guess == self.word[i]: self.word_guessed[i] = guess
        self.num_letters = self.num_letters-1
        else: 
            print("Sorry,", guess, "is not in the word. Try again.")
            self.num_lives=self.num_lives-1
            print("You have", self.num_lives, "left.")
        pass
    
    def ask_for_input(self):
        while True:
            guess = str(input("Guess a letter!"))
            if guess.isalpha() != True or len(guess) != 1: 
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            pass
            



game = Hangman(word_list, num_lives=5)
game.ask_for_input()
