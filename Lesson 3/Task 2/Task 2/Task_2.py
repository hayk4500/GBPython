from random import randint
import math

n = int(input())
nums = []
for i in range(n):
    nums.append(randint(1, 10))
print(nums)

mult = []
k = math.ceil(n/2)

for i in range(k):
    if i != n-i-1:
        mult.append(nums[i]*nums[n-i-1])
    else:
        mult.append(nums[i])

print(mult)