x = int(input("x = "))
y = int(input("y = "))

if x > 0 and y > 0:
    print("1")
elif x > 0 and y < 0:
    print("4")
elif x < 0 and y < 0:
    print("3")
elif x < 0 and y > 0:
    print("2")
elif x == 0 and y != 0:
    print("Y-axis")
elif x != 0 and y == 0:
    print("X-axis")
else:
    print("Wrong input!")