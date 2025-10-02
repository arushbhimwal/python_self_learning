import random

a = random.randint(1,100)

i = 0

while True:
    try:
        b = int(input("Enter you guess: "))
        i += 1
    
    except ValueError:
        print("Invalid input! Pleas enter a number between 1-100")
        continue

    if a == b :
        print(f"You won!, in {i} tries")
        break

    elif a < b :
        print("too high")

    elif a > b :
        print("too low")
        
