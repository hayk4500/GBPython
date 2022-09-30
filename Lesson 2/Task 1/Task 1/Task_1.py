num = float(input())
result = 0
n = len(str(num))
num *= 10 ** n

while num > 0:
   temp = num % 10
   result += temp
   num = num // 10

print(int(result))
