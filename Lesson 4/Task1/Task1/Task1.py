from decimal import Decimal

def accur(n, acc):
    num = Decimal(f"{n}")
    return num.quantize(Decimal(f"{acc}"))

n = float(input("Number: "))
acc = float(input("Accuracy: "))
result = accur(n, acc)
print(result)
