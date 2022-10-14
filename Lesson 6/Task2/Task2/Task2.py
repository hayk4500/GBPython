def genum(num):
    gens = [n for n in range(20, num)]
    return gens

def _2021x(listus : list):
    newlist = [n for n in listus if (n % 20 == 0 or n % 21 == 0)]
    return newlist

genlist = genum(int(input()))
print(genlist)

xlist = _2021x(genlist)
print(xlist)
