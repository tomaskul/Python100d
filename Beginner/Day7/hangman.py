import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

blank_char = "_"
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in chosen_word:
    display.append(blank_char)

print(display)

end_of_game = False
while not end_of_game:
    guess = input("Type a letter in the random word:\t")[0].lower()

    is_correct_guess = False
    for position in range(0, len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
            is_correct_guess = True
        position += 1

    if not is_correct_guess:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if blank_char not in display:
        end_of_game = True
        print("You've win!")
    
    print(stages[lives])