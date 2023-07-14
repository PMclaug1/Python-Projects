
import pandas


#1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}
print((nato_dict))

#2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_input = input("Please enter a word. ").upper()
    try:
        output = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Please choise a valid letter from the alphabet.")
        generate_phonetic()
    else:
        print(output)

generate_phonetic()




