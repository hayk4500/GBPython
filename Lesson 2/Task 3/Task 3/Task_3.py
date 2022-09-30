n = int(input()) + 1
i = 1
summ = 0

while i < n :
    res = (1+1/i)**i
    print(round(res), end=", ")
    i = i + 1
    summ = summ + round(res)
print("\n",summ)
