import random

blank_char = "_"

def has_user_won(display):
    for item in display:
        if item == blank_char:
            return False
    return True

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in chosen_word:
    display.append(blank_char)

print(display)

while not has_user_won(display):
    guess = input("Type a letter in the random word:\t")[0].lower()

    for position in range(0, len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
        position += 1

    print(display)

print("You've won!")





