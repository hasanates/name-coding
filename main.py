import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


letter_code = {row.letter:row.code for (index, row) in data.iterrows()}

word = [x for x in input("enter a word").upper().replace(" ","")]

answer = [ letter_code[x] for x in word]

print(answer)
