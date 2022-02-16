import numpy as np
from collections import deque
from time import time

#Day 9: Smoke Basin

def preprocess_input(txt = '..//input files//input_d9.txt' ):
    '''
    input: AoC input text file
    outputs: dict - where the coordinates are the keys and the values are the depths at that point
    '''

    with open(txt,'r') as fob:
        inp = fob.readlines()
    basin_map ={}
    for i in range(len(inp)):
        for j in range(len(inp[0])-1):
            basin_map[i,j] = int(inp[i][j])
    return basin_map, inp
            


def find_low_points(basin_map, inp):
    '''
    input: dict (basin map)
    output: list of tuples, where each 2d touple represents coordinates (x,y) of a lowpoint
    '''
    lowpoints=[]
    total_risk=0
    for i in range(len(inp)):
        for j in range(len(inp[0])-1):
            cond1 =  basin_map[i,j] < basin_map.get((i-1,j),10)
            cond2 =  basin_map[i,j] < basin_map.get((i+1,j),10)
            cond3 =  basin_map[i,j] < basin_map.get((i,j-1),10)
            cond4 =  basin_map[i,j] < basin_map.get((i,j+1),10)
            if cond1 and cond2 and cond3 and cond4 :
                lowpoints.append((i,j))
                total_risk += 1+basin_map[i,j]
    return lowpoints, total_risk

def bfs(start, basin_map):
    '''
    inputs: 2d-tuple, dict - starting (x,y)-coordinates, dict representing the map
    outputs: int - size of the crater
    '''
    explored= set()
    queued = deque()
    queued.append(start)
    def add_neighb(a,b):
        x,y = a,b
        neighbours = ((x+1,y), (x,y+1), (x-1,y), (x,y-1))
        for nbs in neighbours:
            if  nbs[0] >=0 and nbs[1] >=0:
                if basin_map.get(nbs,9) != 9  and nbs not in explored:
                    queued.append(nbs)
        explored.add((x,y))

    while queued:
        temp = queued.popleft()
        a,b = temp
        add_neighb(a,b)
    return len(explored)

if __name__ == '__main__':
    start_time = time()
    basin_map, raw_inp = preprocess_input()
    lowpoints, total_risk = find_low_points(basin_map, raw_inp)
    qq = list(bfs(i, basin_map) for i in lowpoints)
    qq.sort()
    print(f'solution part 1: {total_risk}')
    print(f'solution part 2: {qq[-1]*qq[-2]*qq[-3]}')
    print('script ran in:', time()-start_time)
    
