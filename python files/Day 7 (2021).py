import numpy as np
from time import time

#DAY 7

def preprocess_input(txt = '..//input files//input_d7.txt' ):
    '''
    input: AoC input text file
    outputs: list of integers
    '''

    with open(txt,'r') as fob:
        inp = fob.readlines()
    nums = list(int(i) for i in inp[0].split(','))
    return nums


#brute force
def min_sum_dist(lis, custom_metric = 0):
    '''
    input: integer valued list
        optional: different metrixs
    output: minimunm sum of distances to all numbers in the input
    '''
    start = min(nums)
    end = max(nums)
    vals = []
    if not custom_metric: 
        for i in range(start,end):
            temp = sum( abs(x-i) for x in nums)
            vals.append(temp)
    else:
        for i in range(start,end):
            temp = sum( custom_metric(x-i) for x in nums)
            vals.append(temp)        
    return min(vals)


def metric_p2(n):
    '''
    input: classical metric
    output: part 2 metric
    '''
    dist= abs(n)*(abs(n)+1)/2
    return int(dist)

if __name__ == '__main__':
    start_time = time()
    nums = preprocess_input()
    print(min_sum_dist(nums))
    print(min_sum_dist(nums, metric_p2))
    print('elapsed time', time()-start_time, 's')


