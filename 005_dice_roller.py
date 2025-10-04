import random

print("================== dice roller ==================")

def dice_roll():

    valid_no_of_rolls = (1,2,3,4,5,6)

    list_of_rolls = []
    
    while True:
        try:
            no_of_rolls = int(input("How many dice do you want to roll (1-6): "))
            if no_of_rolls in valid_no_of_rolls:
                break
            else:
                print("Invalid! input, Pls enter a valid input (1-6)")

        except ValueError:
            print("Invalid! input, Pls enter a valid input (1-6)")

    print(f"Rolling {no_of_rolls} dice....")
    
    for i in range(no_of_rolls):
        roll = random.randint(1, 6)
        list_of_rolls.append(roll)
        print(f"Your roll no.{i+1}: {roll}")
    
    print(list_of_rolls)
    print(f"Sum of roll: {sum(list_of_rolls)}")
    
    print("")

    while True:
        reroll = input("Do you want to re-roll (y/n/yes/no): ").lower().strip()
        print("")
        if reroll == "y" or reroll == "yes":
            list_of_rolls.clear()
            dice_roll()
        
        elif reroll == "n" or reroll == "no":
            break
        
        else:
            break


dice_roll()