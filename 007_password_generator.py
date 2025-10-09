import string
import random
import pyperclip

lower_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

final_list = [

]

password_list = [

]

no_of_selection = 0

# print(lower_case, upper_case, numbers, symbols)

print("========== Password Generator (12-32 characters) ==========")
print("")
print('''Security Levels:
  12-15 chars: Good security
  16-24 chars: Strong security  
  25-32 chars: Maximum security''')
print("")

while True:
    try:
        password_length = int(input("Enter the length of password you want (12-32): "))

        if password_length >= 12 and password_length <= 32:
            break

        else:
            print("Invalid input, Pls enter a valid password length (12-32)")
        
    except ValueError:
        print("Invalid input, Pls enter a valid password length (12-32)")

print("Character types to include: ")

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

# print(password_length, lower_case_complexity, upper_case_complexity, numbers_complexity, symbols_complexity, no_of_selection)

if lower_case_complexity == "y":
    final_list.extend(lower_case)
    password_list.append(random.choice(lower_case))

if upper_case_complexity == "y":
    final_list.extend(upper_case)
    password_list.append(random.choice(upper_case))

if numbers_complexity == "y":
    final_list.extend(numbers)
    password_list.append(random.choice(numbers))

if symbols_complexity == "y":
    final_list.extend(symbols)
    password_list.append(random.choice(symbols))

if not final_list:
    print("No character categories selected, Can't generate password.")
    exit()

# print(final_list)

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
            
# print(final_list)

for i in range(password_length - no_of_selection):
    password_list.append(random.choice(final_list))

# print(password_list)

random.shuffle(password_list)

shuffled_password = "".join (password_list)

print("")
print(f"Generated Password: {shuffled_password}")
print(f"Length: {password_length} characters")

pyperclip.copy(shuffled_password)

print("Password copied to clipboard!")

