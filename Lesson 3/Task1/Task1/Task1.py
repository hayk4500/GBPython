from random import randint

n = int(input())
nums = []
for i in range(n):
    nums.append(randint(1, 10))
print(nums)

sum = 0

for i in range(n):
    if i % 2 == 0:
        sum = sum + nums[i]

print(sum)