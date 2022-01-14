import time

#Day 1: Sonar Sweep


def make_integer_valued_list(inp= '..//input files//input_d1.txt'):
    ''' transforms the text file input into a list of integers representing sea depths'''
    with open(inp,'r') as fob:
        inputs = fob.readlines()
    sea_depths=[]
    for i in inputs:
        sea_depths.append(int(i))
    return sea_depths

def number_inc_values(liste):
    '''
    input: list of integers
    output int: Number of times a value is followed by a larger one
    '''
    count = 0
    for i in range(0,len(liste)-1):
        if liste[i+1]-liste[i] >0:
            count+=1
    return count

#part 2

def sliding_windows_len3(lis):
    '''
    input: int value list
    output: list of sums of 3 consecutrive values
    '''
    sliding_windows=[]
    for i in range(0,len(lis)-2):
        sliding_windows.append(sum(lis[i:i+3]))
    return sliding_windows





if __name__ =='__main__':
    start_time = time.time()
    sea_depths= make_integer_valued_list()
    print('solution part 1:', number_inc_values(sea_depths))
    sliding_windows=sliding_windows_len3(sea_depths)
    print('solution part 2:', number_inc_values(sliding_windows))
    print('script ran in ',time.time()- start_time, ' s')


