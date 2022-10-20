
import math
n1 = complex(0 + 0*1j)
n2 = complex(0 + 0*1j)
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
    if op_t not in ['1', '2', '3', '4', '5', '6', '0']:
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
        case 4: operation = div
        case 5: operation = pow
        case 6: operation = sqrt
    return operation


def init_value():
    global n1
    global n2
    global op
    if op != 6 and op != 5:
        real1  = float(input('Enetr 1 real part: '))
        imag1 = float(input('Enetr 1 imaginary number: '))
        real2  = float(input('Enetr 2 real part: '))
        imag2 = float(input('Enetr 2 imaginary number: '))
        n1 = complex( real1 + imag1 *1j)
        n2 = complex( real2 + imag2 *1j)
    elif op == 5:
        real1  = float(input('Enetr 1 real part: '))
        imag1 = float(input('Enetr 1 imaginary number: '))
        p = int(input('Enter pow: '))
        n1 = complex( real1 + imag1 *1j)
        n2 = complex( p + 0*1j)
    elif op == 6:
        real1  = float(input('Enetr 1 real part: '))
        imag1 = float(input('Enetr 1 imaginary number: '))
        n1 = complex( real1 + imag1 *1j)
        n2 = complex( 0 + 0*1j)
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

def div():
    if n2:
        return n1 / n2

def pow():
    p = int(round(n2.real))
    if p >=0:
     return complex( math.pow(n1.real,p) + math.pow(n1.imag,p) * 1j )

def sqrt():
    return complex( math.sqrt(n1.real) + math.sqrt(n1.imag) * 1j )

