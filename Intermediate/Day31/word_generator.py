import pandas
import random

ENGLISH = "English"
SPANISH = "Spanish"

class WordGenerator:
    def __init__(self):
        data = pandas.read_csv("Intermediate/Day31/data/1k-Most-frequent-ES-words.csv")
        dict = data.to_dict()
        self.spanish_dict = dict[SPANISH]
        self.english_dict = dict[ENGLISH]

    
    def nextWord(self):
        word_id = random.choice(range(1,len(self.spanish_dict)))
        #result = [{SPANISH: self.spanish_dict[word_id]}, {ENGLISH: self.english_dict[word_id]}]

        result = {
            SPANISH: self.spanish_dict[word_id], 
            ENGLISH: self.english_dict[word_id]
            }
        return result
