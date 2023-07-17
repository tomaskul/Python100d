#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

NAME_PLACEHOLDER_TOKEN = "[name]"



invited_names = []
with open("Intermediate/Day24/Input/Names/invited_names.txt") as f:
    invited_names = f.readlines()

for name in invited_names:
    letter_lines = []
    with open("Intermediate/Day24/Input/Letters/starting_letter.txt") as f:
        letter_lines = f.readlines()
    
    plain_name = name.strip('\n')
    letter_lines[0] = letter_lines[0].replace(NAME_PLACEHOLDER_TOKEN, plain_name)

    with open(f"Intermediate/Day24/Output/ReadyToSend/letter_for_{plain_name}.txt", mode="w") as f:
        f.writelines(letter_lines)