import numpy as np
from time import time

#DAY 6

def get_started(txt = '..//input files//input_d6.txt'):
    '''
    input: AoC input text file
    outputs: string of ints representing fishes with their timer
    '''
    with open(txt,'r') as fob:
        inp = fob.readlines()

    fish_string = inp[0][0:-1:2]
    return fish_string

def make_fish_dict(iterable):
    '''
    input: iterable of ints (or string representation) representing fishes
    outputs: dictionary that counts fishes at given timer
    '''
    fidi = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    for i in iterable:
        fidi[int(i)]+=1
    return fidi

def next_day_dict(fish_dict):
    fidi = fish_dict
    newf = fidi[0]
    for i in range(8):
        fidi[i]=fidi[i+1]
    fidi[8] = newf
    fidi[6] += newf
    return fidi

if __name__ == '__main__':
    start_time = time()
    fish_string = get_started()
    fidi = make_fish_dict(fish_string)
    for _ in range(80):
        fidi= next_day_dict(fidi)
    print('Solution part 1:', sum(fidi.values()))
    for _ in range(176):
        fidi= next_day_dict(fidi)
    print('Solution part 2:', sum(fidi.values()))
    print('script ran in', time()-start_time, 's')

