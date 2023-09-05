import pandas
#TODO 1. Create a dictionary in this format:


df = pandas.read_csv('nato_phonetic_alphabet.csv', header= None, index_col=0,).to_dict()
inner_dict = df[1]
desired_output = {key: value for key, value in inner_dict.items() if key != 'letter'}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


name = input("name: ").upper()
out_list = [desired_output[letter] for letter in name]
print(out_list)
