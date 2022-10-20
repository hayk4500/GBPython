from datetime import datetime

def save_ratio_logs(line):
    time = datetime.now().strftime('%H:%M')
    with open('calc_logs_ratio.txt', 'a') as l_file:
        l_file.write('{} {};\n'.format(time,line))
    return line


def save_complex_logs(line):
    time = datetime.now().strftime('%H:%M')
    with open('calc_logs_complex.txt', 'a') as l_file:
        l_file.write('{} {};\n'.format(time,line))
    return line

