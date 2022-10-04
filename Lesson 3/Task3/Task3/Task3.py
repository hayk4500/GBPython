num = int(input())
binary = []

while (num != 0):
    binary.append(num%2)
    num = num // 2

binary.reverse()
print(binary)