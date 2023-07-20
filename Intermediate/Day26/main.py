import pandas

alphabet_df = pandas.read_csv("Intermediate/Day26/nato_phonetic_alphabet.csv")
alphabet_dictionary = {row.letter:row.code for (_,row) in alphabet_df.iterrows()}

while True:
    try:
        input_text = input("Enter word to be spelt in NATO phonetic alphabet:\t").upper()
        # Alternatively to try-except, use: 'if character in alphabet_dictionary.keys()' within dictionary comprehension.
        output_text = [alphabet_dictionary[character] for character in input_text]
        print(output_text)
        break
    except KeyError:
        print("Sorry, only letters in the English alphabet please.")
