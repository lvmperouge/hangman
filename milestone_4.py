import random
word_list = ["mango", "grape", "coconut", "strawberry", "tomato"]
class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word=random.choice(word_list)
        self.word_guessed=["_"]*len(self.word)
        self.num_letters=0
        self.num_lives=num_lives
        self.word_list=word_list
        self.list_of_guesses=[]
    
    def check_guess(guess):
        guess = guess.lower()    
        if guess in word: 
            print("Good guess, ", guess, "is in the word!")
        else: 
            print("Sorry,", guess, "is not in the word. Try again.")
    
    def ask_for_input():
        while True:
            guess = str(input("Guess a letter!"))
            if guess.isalpha() == True and len(guess) == 1:
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
