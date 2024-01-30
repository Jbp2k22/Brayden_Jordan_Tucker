import random

def print_rules():
    print("Yahtzee Rules:")
    print("1. The game consists of 13 rounds.")
    print("2. In each round, you can roll the dice up to 3 times.")
    print("3. After each roll, you can choose which dice to keep.")
    print("4. After the third roll, you must choose a category to score in.")
    print("5. The score is calculated based on the chosen category.")
    print("6. The player with the highest total score at the end wins.")

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def print_dice(dice):
    print("Dice:", ", ".join(map(str, dice)))

def choose_dice_to_keep():
    keep_dice = input("Enter the indices of dice to keep (e.g., 1 3 5), or 'none' to reroll all: ")
    if keep_dice.lower() == 'none':
        return []
    else:
        return [int(index) - 1 for index in keep_dice.split()]

def yahtzee():
    print("Welcome to Yahtzee!")
    print_rules()

    total_score = 0
    for round_num in range(1, 14):
        print("\nRound", round_num)
        dice = roll_dice(5)

        for roll_num in range(1, 4):
            print("\nRoll", roll_num)
            print_dice(dice)

            if roll_num < 3:
                keep_dice_indices = choose_dice_to_keep()
                dice = [dice[i] for i in range(5) if i in keep_dice_indices] + roll_dice(len(keep_dice_indices))
            else:
                print("Final roll")
        
        print_dice(dice)

        # Dummy scoring for demonstration purposes (replace with actual scoring logic)
        score = sum(dice)
        print("Score for this round:", score)
        total_score += score

    print("\nGame Over!")
    print("Total Score:", total_score)

if __name__ == "__main__":
    yahtzee()

