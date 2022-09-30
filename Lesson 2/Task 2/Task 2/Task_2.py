number = int(input())
n = 1

while n <= number + 1:
    temp = 1
    i = 1
    for i in range(1, n):
        temp = temp * i
    n = n + 1
    print(temp, end=", ")