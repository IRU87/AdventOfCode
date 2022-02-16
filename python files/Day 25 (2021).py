import numpy as np
from time import time


#Day 25: Sea Cucumber

#bad, but still acceptable, performance ( about 5 s)



def preprocess(inp = '..//input files//input_d25.txt'):
    '''
    input: AoC txt file
    output: np.array representing the snails

    '''
    with open(inp, 'r') as fob:
        strs = fob.readlines()
    # make numpy array, . = 0 , v = 2, > = 1
    lis = []
    for i in strs:
        k = i[:-1].replace('.','0').replace('v','2').replace('>','1')
        temp = list( int(j) for j in k)
        lis.append(temp)
    arr = np.array(lis)
    return arr

def step(arra):
    '''
    input: np.array representing the snails
    output: np.array representing the snails after one time step
    '''
    arr = arra
    temp = arra+0
    leny, lenx = arra.shape
    for y in range(leny):
        for x in range(lenx):
            if arr[y,x] == 1:
                if not arr[y,(x+1)%lenx]:
                    temp[y,x] = 0
                    temp[y,(x+1)%lenx]=1
    temp2 = temp+0
    for y in range(leny):
        for x in range(lenx):
            if temp[y,x] == 2:
                if not temp[(y+1)%leny,x]:
                    temp2[y,x] = 0
                    temp2[(y+1)%leny,x]=2              
    return temp2

def run(ar):
    '''
    input:
        np.array representing the snails
    output:
        np.array representing the final snail configuration
        int number of steps
    '''
    temp1 = ar
    temp2 = ar+1
    counter = 1
    while True:
        temp2 = temp1 + 0
        temp1 = step(temp1)
        if (temp1 == temp2).all():
            break
        counter+=1
    return temp1, counter


if __name__ == '__main__':
    start_time = time()
    a = preprocess()
    array , count = run(a)
    print(count)
    print('run time', time()-start_time)
