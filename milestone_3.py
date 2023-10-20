def check_guess(letter):
    letter = letter.lower()    
    if letter in word: 
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






