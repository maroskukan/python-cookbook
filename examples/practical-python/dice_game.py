import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def get_name(id):
    player_name = input(f"Enter player {id}'s name: ")
    return player_name

def main():
    p1 = get_name(1)
    p2 = get_name(2)

    r1 = roll_dice()
    r2 = roll_dice()

    print(f'{p1} rolled {r1}.')
    print(f'{p2} rolled {r2}.')

    if r1 > r2:
        print(f'{p1} wins!')
    elif r2 > r1:
        print(f'{p2} wins!')
    else:
        print('Tie')

main()