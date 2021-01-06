weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ").upper()
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Kg: " + str(converted))
elif unit.upper() == "L":
    converted = weight * 0.45
    print("Weight in Lbs: " + str(converted))
else:
    print(""" Try again! 
Select 'K' or 'L'
    You can do it, I'm sure=)
    """)