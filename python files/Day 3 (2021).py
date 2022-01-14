import numpy as np
from time import time

#DAY 3

def prep_inputs(txt = '..//input files//input_d3.txt'):
    '''
    input: AoC input text file
    outputs: sorted list of strings representing 12 digit binary numbers
    '''
    with open(txt,'r') as fob:
        inp = fob.readlines()
    lis = list( i.strip() for i in inp)
    lis.sort(reverse=True)
    return lis

def get_gamma_eps(inp):
    '''
    inputs: list of strings representing 12 digit binary numbers
    outputs: "gamma" and "epsilon" binary values in form of an np.array
        (gamma = rounded mean of all digits /same but flipped for eps)
    '''
    counts = np.zeros(12)
    for i in inp:
        for j in range(len(i)-1):
            counts[j] += int(i[j])
    gamma = counts*2//len(inp)
    epsilon = np.ones(12) - gamma
    return gamma, epsilon

def binary_to_decimal(iterable):
    '''
    inputs: iterable of integers/binary numbers
    output: number in decimal
    '''
    dec = 0
    for num,i in enumerate(iterable):
        dec+= 2**(len(iterable)-num-1)*int(i)
    return dec

#part 2
def o2_val(lis):
    '''
    inputs: list of strings representing 12 digit binary numbers
    outputs: "o2 value" binary number as a string
    '''
    o2str= ''
    inp = lis
    for i in range(len(inp[0])):
        su= sum(int(inp[j][i]) for j in range(len(inp)))
        if su/len(inp) >= 0.5:
            o2str += '1'
            inp = inp[0:su]
        else:
            o2str += '0'
            inp = inp[su:]
        if len(inp)==1:
            return inp[0]
    return o2str

def co2_val(lis):
    '''
    inputs: list of strings representing 12 digit binary numbers
    outputs: "co2 value" binary number as a string
    '''
    co2str= ''
    inp = lis
    for i in range(len(inp[0])):
        su= sum(int(inp[j][i]) for j in range(len(inp)))
        if su/len(inp) < 0.5:
            co2str += '1'
            inp = inp[0:su]
        else:
            co2str += '0'
            inp = inp[su:]
        if len(inp)==1:
            return inp[0]
    return co2str


if __name__ == '__main__':
    start_time = time()
    inp = prep_inputs()
    gamma, epsilon = get_gamma_eps(inp)
    print('part 1 solution', binary_to_decimal(gamma)*binary_to_decimal(epsilon))   
    o2 = binary_to_decimal(o2_val(inp))
    co2= binary_to_decimal(co2_val(inp))
    print('part 2 solution', co2*o2)
    print('elapsed time', time()-start_time, 's')
