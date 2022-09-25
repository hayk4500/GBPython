X = int(input("X = "))
Y = int(input("Y = "))
Z = int(input("Z = "))

statement1 = not (X or Y or Z)
statement2 = not (X) and not (Y) and not (Z)

if statement1 == statement2:
    print("true")
else:
    print("false")