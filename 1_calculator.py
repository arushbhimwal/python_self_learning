def get_number(prompt):
    try:
        return float(input(prompt))
    
    except ValueError:
        print("Error : Invalid number, Pls enter a valid number")

def formate_number(num):
    if num == int(num):
        return int(num)

    else:
        return round(num, 2)

print("=======Simpel Calculator=======")

a = get_number("Enter first number to be evaluated: ")
b = get_number("Enter second number to be evaluated: ")

print("\noperations : + (add), - (subtract), * (multiply), / (divide)")

while True:
    
    operation = input("what operation do you want to perform: ").strip()

    if operation == "+":
        result = a+b
        print(f"{formate_number(a)} + {formate_number(b)} = {formate_number(result)}")
        break
    elif operation == "-":
        result = a-b
        print(f"{formate_number(a)} - {formate_number(b)} = {formate_number(result)}")
        break
    elif operation == "*":
        result = a*b
        print(f"{formate_number(a)} * {formate_number(b)} = {formate_number(result)}")
        break
    elif operation == "/":
        if b == 0:
            print("Error : division by 0 is not allowed!")
        else:
            result = a/b
            print(f"{formate_number(a)} / {formate_number(b)} = {formate_number(result)}")
        break
    else:
        print("Error : Invalid operation performed, Valid operations '+', '-', '*', '/'")