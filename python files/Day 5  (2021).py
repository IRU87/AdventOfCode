import numpy as np
from time import time

#Day 5: Hydrothermal Venture

def preprocess_inputs(txt = '..//input files//input_d5.txt'):
    '''
    inputs: AoC txt file
    outputs: list of tuples representing lines (x_start, x_end, y_start,y_end)
    '''
    with open(txt,'r') as fob:
        inp = fob.readlines()
    lines = []
    for i in inp:
        x_start,temp,y_end= i.split(',')
        x_end,y_start = temp.split('->')
        lines.append([int(x_start),int(x_end),int(y_start),int(y_end)])
    return lines

    
def points_from_line(line,value_dict):
    '''
    inputs: 4d-tuple representing a line
            dictionary (keys = 2d tuple representing coordinate, values= # of lines at tgat coordniate)
            

    transform line functions into points and adds to dictionary
    
    outputs: None

    '''
    a,b,c,d = line
    #ordering
    if a-c ==0:
        if b>d:
            b,d=d,b
        for i in range(b,d+1):
            value_dict[(a,i)] = value_dict.get((a,i),0) + 1
    elif b-d ==0:
        if a>c:
            a,c = c,a
        for i in range(a,c+1):
            value_dict[(i,b)] = value_dict.get((i,b),0) + 1
    elif a<c:
        for i in range(a,c+1):
            if d>b:
                dire = 1
            else:
                dire = -1
            value_dict[(i,b+dire*(i-a))] = value_dict.get((i,b+dire*(i-a)),0) + 1
    else:
        a,b,c,d = c,d,a,b
        for i in range(a,c+1):
            if d>b:
                dire = 1
            else:
                dire = -1
            value_dict[(i,b+dire*(i-a))] = value_dict.get((i,b+dire*(i-a)),0) + 1

## I can't read properly and did part 2 before part 1 and truncated my general function
            
def non_diag_points_from_line(line,value_dict):
    '''
    inputs: 4d-tuple representing a line
            dictionary (keys = 2d tuple representing coordinate, values= # of lines at tgat coordniate)
            

    transform (non-diagonal) line functions into points and adds to dictionary
    
    outputs: None

    '''
    a,b,c,d = line
    #ordering
    if a-c ==0:
        if b>d:
            b,d=d,b
        for i in range(b,d+1):
            value_dict[(a,i)] = value_dict.get((a,i),0) + 1
    elif b-d ==0:
        if a>c:
            a,c = c,a
        for i in range(a,c+1):
            value_dict[(i,b)] = value_dict.get((i,b),0) + 1

if __name__ == '__main__':
    start_time = time()
    lines = preprocess_inputs()
    vals1 = {}
    vals2 = {}
    for line in lines :
        non_diag_points_from_line(line,vals1)
    sol_1 = len(list(filter(lambda y: y>1, vals1.values())))
    for line in lines :
        points_from_line(line,vals2)
    sol_2 = len(list(filter(lambda y: y>1, vals2.values())))

    print('Solution part1: ', sol_1)
    print('Solution part2: ', sol_2)
    print('script ran in:', time()-start_time, 's')
      

