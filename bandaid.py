while True:
        guess = str(input("Guess a letter!"))
        if guess.isalpha() != True or len(guess) != 1: print("Invalid letter. Please, enter a single alphabetical character.")
        else: break