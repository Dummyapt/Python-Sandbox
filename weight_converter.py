weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ").upper()

if unit == "K":
    print(f"Weight in lbs: {weight * 2.205}")
elif unit == "L":
    print(f"Weight in kg: {weight / 2.205}")
else:
    print("Please try again!")
