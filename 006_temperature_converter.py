#def section start
def c_to_f(c):
    return (c * 9/5) + 32

def c_to_k(c):
    return c + 273.15

def f_to_c(f):
    return (f - 32) * 5/9

def f_to_k(f):
    return (f - 32) * 5/9 + 273.15

def k_to_c(k):
    return k - 273.15

def k_to_f(k):
    return (k - 273.15) * 9/5 + 32

def formate_number(num):
    if num == int(num):
        return int(num)

    else:
        return round(num, 2)
#def section end

#input section start
try:
    input_temp = float(input("Enter the temperature: "))

except ValueError:
    print("Invalid! input, Pls enter a valid input")


formated_units = {
    "c": "C°",
    "f": "F°",
    "k":"K"
}

while True:
    try:
        input_unit = str(input("Enter the unit of temperature you just entered: ")).lower().strip()
        if input_unit in ["c", "k", "f"]:
            break
        
        else:
            print("Invalid! unit, Pls enter a valid unit (c/f/k)")
            
    except ValueError:
        print("Invalid! input, Pls enter a valid input")

while True:
    try:
        convertion_unit = str(input("Enter the unit in which you want to convert it into: ")).lower().strip()
        if convertion_unit in ["c", "k", "f"]:
            break
        
        else:
            print("Invalid! unit, Pls enter a valid unit (c/f/k)")
            
    except ValueError:
        print("Invalid! input, Pls enter a valid input")

#input section end

# value section start
if input_unit == "c":
    c = input_temp

elif input_unit == "f":
    f = input_temp

elif input_unit == "k":
    k = input_temp
#value section end

#main loop
while True:
    if input_unit == convertion_unit:
        print("convertion into same unit will not affect the temperature")
        print(f"Temperature = {input_temp} {formated_units[input_unit]}")
        break

    else:
        if input_unit == "c" and convertion_unit == "f":
            converted_temp = c_to_f(c)
            print(f"The conversion of {formated_units[input_unit]} into {formated_units[convertion_unit]} is : {formate_number(converted_temp)}{formated_units[convertion_unit]}")
            break

        elif input_unit == "c" and convertion_unit == "k":
            converted_temp = c_to_k(c)
            print(f"The conversion of {formated_units[input_unit]} into {formated_units[convertion_unit]} is : {formate_number(converted_temp)}{formated_units[convertion_unit]}")
            break

        elif input_unit == "f" and convertion_unit == "c":
            converted_temp = f_to_c(f)
            print(f"The conversion of {formated_units[input_unit]} into {formated_units[convertion_unit]} is : {formate_number(converted_temp)}{formated_units[convertion_unit]}")
            break

        elif input_unit == "f" and convertion_unit == "k":
            converted_temp = f_to_k(f)
            print(f"The conversion of {formated_units[input_unit]} into {formated_units[convertion_unit]} is : {formate_number(converted_temp)}{formated_units[convertion_unit]}")
            break

        elif input_unit == "k" and convertion_unit == "c":
            converted_temp = k_to_c(k)
            print(f"The conversion of {formated_units[input_unit]} into {formated_units[convertion_unit]} is : {formate_number(converted_temp)}{formated_units[convertion_unit]}")
            break

        elif input_unit == "k" and convertion_unit == "f":
            converted_temp = k_to_f(k)
            print(f"The conversion of {formated_units[input_unit]} into {formated_units[convertion_unit]} is : {formate_number(converted_temp)}{formated_units[convertion_unit]}")
            break

        else:
            print("Something went wrong!")
            break