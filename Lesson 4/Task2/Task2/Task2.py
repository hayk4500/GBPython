def splnum(num):
    nums = []
    init = 2
    while num > 1:
        if num % init == 0:
            nums.append(init)
            num = num // init
        else:
            init = init + 1
    return nums;

numbers = int(input())
smplnums = splnum(numbers)
print(smplnums)