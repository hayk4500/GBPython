from random import sample

def rndlist_w(count: int, let: str = 'abc'):
    wlist = []
    for i in range(count):
        lets = sample(let, 3)
        wlist.append("".join(lets))
    return " ".join(wlist)

def dlt_let(w: str) -> str:
    return " ".join(i for i in w.split() if i != "abc")

n = int(input())
lists = rndlist_w(n)
print(lists)
print(dlt_let(lists))
