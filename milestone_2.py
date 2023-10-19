import random

word_list = ["mango", "grape", "coconut", "strawberry", "tomato"]
print(word_list)

word=random.choice(word_list)

print("Guess a letter!")
guess=str(input())

if len(guess)==1 & guess.isalpha()==1:
    print("Good guess!")
else: print("Oops! That is not a valid input.")
