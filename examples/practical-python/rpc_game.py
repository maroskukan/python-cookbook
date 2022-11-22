from random import choice

choices = ['scissors', 'rock', 'paper']
computer_choice = choice(choices)

while True:
    user_choice = input('Do you want - rock, paper, or scissors: ')
    if user_choice in choices:
        break
    else:
        print(f'Valid choices are {" ".join(choices)}. Try again.')

print(f"\nComputer had {computer_choice}.")
if computer_choice == user_choice:
    print('TIE')
elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
    print('WIN')
else:
    print("You lose :( computer wins :D")