import random
import hangman_art
import hangman_words

blank_char = "_"
chosen_word = random.choice(hangman_words.word_list)
lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in chosen_word:
    display.append(blank_char)

print(hangman_art.logo)
print(display)

end_of_game = False
guess_history = []
while not end_of_game:
    guess = input("Type a letter in the random word:\t")[0].lower()

    if guess in guess_history:
        print(f"You've already guessed '{guess}', try again.")
        continue
    else:
        guess_history.append(guess)

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
    
    print(hangman_art.stages[lives])