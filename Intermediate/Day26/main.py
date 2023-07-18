import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
alphabet_df = pandas.read_csv("Intermediate/Day26/nato_phonetic_alphabet.csv")
alphabet_dictionary = {row.letter:row.code for (_,row) in alphabet_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_text = input("Enter word to be spelt in NATO phonetic alphabet:\t").upper()
output_text = [alphabet_dictionary[character] for character in input_text if character in alphabet_dictionary.keys()]
print(output_text)

