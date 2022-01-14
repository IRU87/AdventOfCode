import numpy as np
from time import time

# Day 4: Giant Squid

def make_board(lis):
    '''
    input: list of 5 valid bingo board strings (each representing 1 row)
    output:  5x5 np array of the given ints
    '''
    full = []
    for i in lis:
        a,b,c,d,e = int(i[0:2]), int(i[3:5]), int(i[6:8]), int(i[9:11]), int(i[12:14])
        full.append([a,b,c,d,e])
    return np.array(full)


def preprocess_input(txt = '..//input files//input_d4.txt' ):
    '''
    input: txt containing bingo boards and series
    outputs: list of drawn numbers, list of np.array boards
    '''
    with open(txt,'r') as fob:
        inp = fob.readlines()
    bingo_series = inp[0].split(',')
    nums = list(int(i) for i in bingo_series)
    bingo_boards  = list( make_board(inp[2+6*i:7+i*6]) for i in range(len(inp)//6))
    return nums, bingo_boards 

#part 1   
def play_bingo(bl, nums):
    '''
    inputs: list of boards (np.arrays) and list of ints
    output: sum of the remaining numbers of the winning board times the last drawn number
    '''
    for i in nums:
        for j in bl:
            j[j==i] = -1
            cond1 = np.sum(j,axis=1)
            cond2 = np.sum(j,axis=0)
            if -5 in cond1 or -5 in cond2:
                j[j==-1] = 0
                return np.sum(j)*i

#part 2
            
def play_to_lose(bl, nums):
    '''
    inputs: list of boards (np.arrays) and list of ints
    outputs: np.sum of the remaining numbers of the board that finishes last times the last drawn number
    '''
    count = 0 
    for i in nums:
        for j in bl:
            j[j==i] = -1
            cond1 = np.sum(j,axis=1)
            cond2 = np.sum(j,axis=0)
            if -5 in cond1 or -5 in cond2:
                count +=1
                if count ==100:
                    j[j==-1] = 0
                    return np.sum(j)*i
                j[j>-2] = -100
            
if __name__ == '__main__':
    start_time = time()
    nums, boards = preprocess_input()
    print(play_bingo(boards,nums) )
    print(play_to_lose(boards,nums))
    print('excecution took', time()-start_time, 's')

