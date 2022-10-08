from random import randrange


def rndnum(n: int):
    if n < 0:
        print("Negative!!!")
        return []
    nums = []
    for i in range(n):
        nums.append(randrange(n))
    return nums

    
def unq(nums: list):
    res = []
    d = {}.fromkeys(nums, 0)

    for i in nums:
        d[i] += 1

    for j in d:
        if d[j] == 1:
            res.append(j)

    return res


n = int(input())
numbers = rndnum(n)
print(numbers)
print(unq(numbers))
