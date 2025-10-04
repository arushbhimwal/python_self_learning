import random

valid_no_of_roles = (1,2,3,4,5,6)

list_of_roles = [

]

print("================== dice roller ==================")

while True:
    try:
        no_of_roles = int(input("How many dice do you want to role (1-6): "))
        if no_of_roles in valid_no_of_roles:
            break
        else:
            print("Invalid! input, Pls enter a valid input (1-6)")

    except ValueError:
        print("Invalid! input, Pls enter a valid input (1-6)")

def dice_roll():

    print(f"Rolling {no_of_roles} dice....")

    for i in range(no_of_roles):
        role = random.randint(1, 6)
        list_of_roles.append(role)
        print(f"Your roll no.{i+1}: {role}")
    
    print (list_of_roles)

dice_roll()

print("")

while True:
    rerole = input("Do you want to re-role (y/n/yes/no)").lower().strip()
    print("")
    if rerole == "y" or rerole == "yes":
        list_of_roles.clear()
        dice_roll()
    
    else:
        break

