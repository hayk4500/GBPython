import random

def gen_nums(num):
    genlist = [random.randint(0, 101) for _ in range(num)]
    return genlist;

def is_bigger(listus : list):
    bignums = []
    i = 1
    for i in range(len(listus)):
        if listus[i] - listus[i - 1] > 0:
            bignums.append(listus[i])
    return bignums
    

randomnums = gen_nums(int(input()))
print(randomnums)

biggernums = []
biggernums = is_bigger(randomnums)
print(biggernums)
