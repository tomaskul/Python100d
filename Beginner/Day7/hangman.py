import random

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Type a letter in the random word:\t")[0].lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")