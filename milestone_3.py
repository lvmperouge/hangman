while True:
    guess = str(input("Guess a letter!"))
    if guess.isalpha != True:
        print("Invalid letter. Please, enter a single alphabetical character.")
        continue
    elif len(guess)!=1:
            print("Invalid letter. Please, enter a single alphabetical character.")
            continue
    else: breakpython milestone_3.py