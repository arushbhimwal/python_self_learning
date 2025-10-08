import string
import random
import pyperclip

lower_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

no_of_selection = 0

print(lower_case, upper_case, numbers, symbols)

while True:
    try:
        password_length = int(input("Enter the length of password you want (12-32): "))

        if password_length >= 12 and password_length <= 32:
            break
        else:
            print("Invalid input, Pls enter a valid password length (12-32)")
    except ValueError:
        print("Invalid input, Pls enter a valid password length (12-32)")

while True:
    try:
        lower_case_complexity = str(input("Lowercase letters? (y/n): ")).lower().strip()

        if lower_case_complexity == "y":
            no_of_selection += 1
            break
        
        elif lower_case_complexity == "n":
            break
        
        else:
            print("Invalid input, Pls enter a valid input (y-n)")
        
    except ValueError:
        print("Invalid input, Pls enter a valid input (y-n)")

while True:
    try:
        upper_case_complexity = str(input("Uppercase letters? (y/n): ")).lower().strip()

        if upper_case_complexity == "y":
            no_of_selection += 1
            break
        
        elif upper_case_complexity == "n":
            break
        
        else:
            print("Invalid input, Pls enter a valid input (y-n)")
        
    except ValueError:
        print("Invalid input, Pls enter a valid input (y-n)")

while True:
    try:
        numbers_complexity = str(input("Numbers? (y/n): ")).lower().strip()

        if numbers_complexity == "y":
            no_of_selection += 1
            break
        
        elif numbers_complexity == "n":
            break
        
        else:
            print("Invalid input, Pls enter a valid input (y-n)")
        
    except ValueError:
        print("Invalid input, Pls enter a valid input (y-n)")

while True:
    try:
        symbols_complexity = str(input("Symbols? (y/n): ")).lower().strip()

        if symbols_complexity == "y":
            no_of_selection += 1
            break
        
        elif symbols_complexity == "n":
            break
        
        else:
            print("Invalid input, Pls enter a valid input (y-n)")
        
    except ValueError:
        print("Invalid input, Pls enter a valid input (y-n)")

print(password_length, lower_case_complexity, upper_case_complexity, numbers_complexity, symbols_complexity, no_of_selection)

final_list = [

]

if lower_case_complexity == "y":
    final_list.extend(lower_case)

if upper_case_complexity == "y":
    final_list.extend(upper_case)

if numbers_complexity == "y":
    final_list.extend(numbers)

if symbols_complexity == "y":
    final_list.extend(symbols)

print(final_list)

while True:
    try:
        exclude_similars = str(input("Exclude similar characters (1, l, I, 0, O, o)? (y/n): ")).lower().strip()

        if exclude_similars == "y":
            break
        
        elif exclude_similars == "n":
            break
        
        else:
            print("Invalid input, Pls enter a valid input (y-n)")
        
    except ValueError:
        print("Invalid input, Pls enter a valid input (y-n)")

if exclude_similars == "y":
    for ch in ["1", "l", "I", "0", "O", "o"]:
        while ch in final_list:
            final_list.remove(ch)
        while ch in lower_case:
            lower_case.remove(ch)
        while ch in upper_case:
            upper_case.remove(ch)
        while ch in numbers:
            numbers.remove(ch)
        while ch in symbols:
            symbols.remove(ch)
            

print(final_list)

password_list = [

]

for i in range(password_length - no_of_selection):
    pass