import random

'''
1 == rock
0 == paper
-1 == scissores
'''
    
computer_score = 0

you_score = 0

text_to_binary = {
    "r": 1,
    "p":0,
    "s":-1
}

binary_to_text = {
    1:"rock",
    0:"paper",
    -1:"scissores"
}

print("======= Welcome to rock paper scissor matchup =======")
print("Enter you choice with 'r' = rock, 'p' = paper, 's' = scissores")
print("")

for i in range(5):

    computer = random.choice([1,0,-1])
    
    while True:
        you = input("enter you choice: ").lower().strip()

        if you in text_to_binary:
            break
        else:
            print("Invalid! input, Pls enter a valid input from 'r', 'p' or 's'")

    you_formated = text_to_binary[you]


    print(f"Computer Choose: {binary_to_text[computer]}, You Choose: {binary_to_text[you_formated]}")

    if computer == you_formated:
        print("It's a draw")
        print("")
        

    else:
        if (computer == 1 and you_formated == 0):
            print("You won!")
            print("")
            you_score += 1

        if (computer == 0 and you_formated == -1):
            print("You won!")
            print("")
            you_score += 1

        if (computer == -1 and you_formated == 1):
            print("You won!")
            print("")
            you_score += 1

        if (computer == 1 and you_formated == -1):
            print("You lose!")
            print("")
            computer_score += 1

        if (computer == 0 and you_formated == 1):
            print("You lose!")
            print("")
            computer_score += 1

        if (computer == -1 and you_formated == 0):
            print("You lose!")
            print("")
            computer_score += 1

if (you_score == computer_score): 
    print("It's a Draw! in Bo5")
elif (you_score > computer_score):
    print(f"You Won! the Bo5, Your Score: {you_score}, Computer's Score: {computer_score}")
elif (you_score < computer_score):
    print(f"You Lose! the Bo5, Your Score {you_score}, Computer's Score: {computer_score}")