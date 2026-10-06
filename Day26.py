import os
import pandas as pd


def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')


clear_terminal()
print('==================================================')
print('        NATO PHONETIC ALPHABET GENERATOR          ')
print('==================================================')

# 1. Load CSV data using Pandas
data = pd.read_csv('nato_phonetic_alphabet.csv')

# 2. Dictionary Comprehension: Convert DataFrame to {letter: code} format
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# 3. Main Loop
while True:
  word = input("\nEnter a word (or type 'exit' to quit): ").upper()

  if word == 'EXIT':
    print('Goodbye!')
    break

  try:
    # 4. List Comprehension: Map input letters to NATO code words
    output_list = [phonetic_dict[letter] for letter in word]
    print(f'NATO Phonetic Code: {output_list}')
  except KeyError:
    print('Sorry, only letters in the alphabet please.')