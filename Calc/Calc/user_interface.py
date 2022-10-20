import ratio
import compl
from logger import save_ratio_logs
from logger import save_complex_logs

mode = int


def calc_welcome():
    print('\nCalculator welcomes you!\n')
    while common_menu():
      match get_mode():
         case 1:
            ratio_menu()
         case 2:
           complex_menu()
         case _:
            print('end')
            break

def common_menu():
    global mode
    mode = int(input('\nWorking with:\n'
                     '1 - rational\n'
                     '2 - complex\n'
                     '0 - exit\n'))
    if mode not in [0,1,2]:
        print('Input incorrect\n')
        mode = 0
    return mode

def get_mode():
    return mode

def get_op_symb(i_op):
    match i_op:
        case 1: return '+'
        case 2: return '-'
        case 3: return '*'
        case 4: return '/'
        case 5: return '**' 
        case 6: return 'sqrt'
        case 7: return '//'
        case 8: return '%'
        case _: return ''

def ratio_menu():
    if ratio.init_operation():
        if ratio.init_value():
            ratio.calculate()
            print(save_ratio_logs(ratio_view_result()))
            
def ratio_view_result():
    numbs = ratio.get_value()
    op_symb = get_op_symb(ratio.get_op_num())
    result = ratio.get_result()
    if op_symb == 'sqrt':
        line =  str(f'{op_symb} {numbs[0]} = {result}')
    else:
        line = str(f'{numbs[0]} {op_symb} {numbs[1]} = {result}')
    return line

def complex_menu():
    if compl.init_operation():
        if compl.init_value():
            compl.calculate()
            print(save_complex_logs(complex_view_result()))


def complex_view_result():
    numbs = compl.get_value()
    op_symb = get_op_symb(compl.get_op_num())
    result = compl.get_result()
    if op_symb == 'sqrt':
        line =  str(f'{op_symb} {numbs[0]} = {result}')
    else:
        line = str(f'{numbs[0]} {op_symb} {numbs[1]} = {result}')
    return line

