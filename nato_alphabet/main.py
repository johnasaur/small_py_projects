import pandas

dataread = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(dataread)

phrase = {row.letter: row.code for (index, row) in dataread.iterrows()}

word = input("Enter word: ").upper()
outputs = [phrase[letter] for letter in word]
print(outputs)

