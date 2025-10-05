print("Emergency Freight Calculator")

while True:
    try:
        length = float(input("Please enter length of the package in cm: "))
        if length <= 0:
            print("Sorry, input must be a positive number, try again")
            continue
        break
    except ValueError:
        print("Sorry, input must be numeric, try again")

while True:
    try:
        width = float(input("Please enter width of the package in cm: "))
        if width <= 0:
            print("Sorry, input must be a positive number, try again")
            continue
        break
    except ValueError:
        print("Sorry, input must be numeric, try again")

while True:
    try:
        height = float(input("Please enter height of the package in cm: "))
        if height <= 0:
            print("Sorry, input must be a positive number, try again")
            continue
        break
    except ValueError:
        print("Sorry, input must be numeric, try again")

while True:
    try:
        weight = float(input("Please enter actual weight of the package in kg: "))
        if weight <= 0:
            print("Sorry, input must be a positive number, try again")
            continue
        break
    except ValueError:
        print("Sorry, input must be numeric, try again")

dim_weight = (length * width * height) / 6000

print("Emergency Freight Calculator input values")
print(f"Length of package: {length} cm")
print(f"Width of package: {width} cm")
print(f"Height of package: {height} cm")
print(f"Actual Weight: {weight} kg")
print(f"Chargeable Weight: {dim_weight:.2f} kg")
print("==============================================")
print("Calculation results:")
