from user_interface import calc_welcome

def main():
   calc_welcome()

main()a
import math

n1 = float(0)
n2 = float(0)
op = 0
result = None


def init_operation():
    global op
    op_t = input('\nOperations:\n'
               '1 - sum  \n'
               '2 - sub  \n'
               '3 - mult \n'
               '4 - div  \n'
               '5 - pow  \n'
               '6 - sqrt \n'
               '0 - previous menu\n') 
    if op_t not in ['1','2','3','4','5','6','0']:
        return 0
    op = int(op_t)
    return op

def get_op_num():
    return op

def get_operation():
    match op:
        case 1: operation = sum
        case 2: operation = sub
        case 3: operation = mult
        case 4: operation = div_st
        case 5: operation = pow
        case 6: operation = sqrt
        case 7: operation = div
        case 8: operation = mod
    return operation


def init_value():
    global n1
    global n2
    global op
    if op != 6:
        n1 = float(input('Enetr 1 number: '))
        n2 = float(input('Enetr 2 number: '))
        op_t = input("7 - '//'\n"
                     "8 - '%'\n"
                     "9 - continue\n"
                     "0 - previous menu\n")
        if op_t in ['7','8']:
            op = int(op_t)
        elif op_t == '0':
            op = 0
            return 0
        elif op_t != '9':
            op = 0
            return 0
    else:
        n1 = float(input('Enetr a number: '))
        n2 = 0
    return (n1, n2)

def calculate():
     global result
     result = get_operation()()
     return result

def get_result():
    return result
    
def get_value(): 
    return (n1, n2)

def sum():
    return n1 + n2

def sub():
    return n1 - n2

def mult():
    return n1 * n2

def div_st():
    if n2:
        return n1 / n2

def div():
    return n1 // n2

def mod():
    return n1 % n2

def pow():
    if n2 >= 0:
       p = int(round(n2))
    return math.pow(n1,p)
    
def sqrt():
    return math.sqrt(n1)  



