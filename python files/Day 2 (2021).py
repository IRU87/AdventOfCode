from time import time

#Day 2: Dive!

def prepare_input(txt ='..//input files//input_d2.txt'):
    '''
    input: AoC txt file
    output: list of strings where each string is one instruction
    '''
    with open(txt,'r') as fob:
        inp = fob.readlines()
    return inp

def step(element):
    '''
    input: string containing the instruction
    output: returns a tuple consisting  of 2 ints that give the change in x,y direction
    '''
    if element[0] == 'f':
        return (int(element[-2]), 0)
    elif element[0] == 'd':
        return (0,int(element[-2]))
    else:
        return (0,-int(element[-2]))

def go_along(liste):
    '''
    input: list of steps (prepared input)
    output: product of the final destination of x,y
    '''
    x= 0
    y= 0
    for i in liste:
        a,b = step(i)
        x+= a
        y+= b
    return x*y

#part 2

def go_along_with_aim(liste):
    '''
    input: list of steps (prepared input)
    output: product of the final destination of x,y (now considering aim)
    '''
    x= 0
    y= 0
    aim = 0
    for i in liste:
        a,b = step(i)
        x+= a
        aim+= b
        y+=a*aim
    return x*y

if __name__ =='__main__':
    start_time = time()
    steps = prepare_input()
    print('solution part 1:', go_along(steps))
    print('solution part 2:', go_along_with_aim(steps))
    print('script ran in ', time()- start_time,'s')



