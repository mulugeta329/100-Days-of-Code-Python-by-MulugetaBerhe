import os

PLACEHOLDER = "[name]"

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
print("==================================================")
print("     ENTERPRISE MAIL MERGE AUTOMATION ENGINE      ")
print("==================================================")

# 1. Read names from input file
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# 2. Read starting template letter
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip() # Remove newline \n characters
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        
        # 3. Write individual customized letter to output folder
        output_path = f"Output/ReadyToSend/letter_for_{stripped_name}.txt"
        with open(output_path, mode="w") as completed_letter:
            completed_letter.write(new_letter)

print("Batch generation complete. Output saved to Output/ReadyToSend/")