
import pandas


#1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}
print((nato_dict))

#2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please enter a word. ").upper()
output = [nato_dict[letter] for letter in user_input]
print(output)




