import os
import pandas as pd


def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')


clear_terminal()
print('==================================================')
print('     SQUIRREL CENSUS DATA PROCESSING ENGINE       ')
print('==================================================')

# 1. Load dataset
data = pd.read_csv('2018_Central_Park_Squirrel_Census_Data.csv')

# 2. Count primary fur colors
grey_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])

print(f'Gray Squirrels:     {grey_count}')
print(f'Cinnamon Squirrels: {red_count}')
print(f'Black Squirrels:    {black_count}')

# 3. Export summary DataFrame to CSV
data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_count, red_count, black_count],
}

df = pd.DataFrame(data_dict)
df.to_csv('squirrel_count.csv', index=False)

print('--------------------------------------------------')
print("SUCCESS: Exported summary to 'squirrel_count.csv'")