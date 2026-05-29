import random
print("----Rock Paper Scissors Game----")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Step 1: Store the images in a list
game_images = [rock, paper, scissors]

# Step 2: Get user choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Step 3: Validation Check (Prevents list index errors before printing)
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
else:
    # Print what the user chose
    print("\nYou chose:")
    print(game_images[user_choice])

    # Step 4: Generate and print computer choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Step 5: Game logic to determine the winner
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice == computer_choice:
        print("It's a tie!")