import numpy as np
from time import time


#Day 11: Dumbo Octopus
def preprocess_input(txt = '..//input files//input_d11.txt' ):
    '''
    input: AoC input text file
    outputs: np array filled with ints. each represent an octopus
    '''
    with open(txt,'r') as fob:
        inp = fob.readlines()
    arr0=[]
    for i in inp:
        temp=[]
        for j in i[:-1]:
            temp.append(int(j))
        arr0.append(temp)
    oct_array = np.array(arr0)
    return oct_array
    
class octo_board(object):
    '''
    class with the attributes:
    board - np array (octopus)
    flashnum - number of octos, that have flashed so far

    '''

    def __init__(self,octos_arr,flashes=0):
        self.board = octos_arr
        self.flashnum = flashes

    def plus_one(self):
        '''
        method that increases the counter of all octopusses in the array by 1
        '''
        self.board+=1

    def flashes(self):
        '''
        checks for flashes, resets flashed octos and increases adjacent counters
        adjusts flash number
        '''
        c = self.flashnum
        cf = -1
        board = self.board
        shape = board.shape
        while c != cf:
            cf = c
            for i in range(shape[0]):
                for j in range(shape[1]):
                    if 9 < board[i,j] < 20:
                        board[i,j]=20
                        helper = board[max(i-1,0):min(i+2,shape[0] ),max(j-1,0):min(j+2,shape[1])]+1
                        board[max(i-1,0):min(i+2,shape[0] ),max(j-1,0):min(j+2,shape[1])]= helper
                        c+=1
        board[board>9] = 0
        self.board = board
        self.flashnum = c

    def new_day(self):
        '''
        calls class methods plus_one and flashes
        '''
        self.plus_one()
        self.flashes()

    def show(self):
        '''
        prints board and flash number
        '''
        print(self.board)
        print(self.flashnum)

if __name__ == '__main__':
    start_time = time()
    octo_arr = preprocess_input()
    octos = octo_board(octo_arr)
    for _ in range(100):
        octos.new_day()
    print('Solution part 1:', octos.flashnum)
    for k in range(5000):
        octos.new_day()
        if (octos.board == np.zeros([10,10])).all():
            print('Solution part 2:',k+101)
            break
    print('script ran in', time()-start_time)
                
                        
                        
