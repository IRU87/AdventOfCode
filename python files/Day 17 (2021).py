import numpy as np
from time import time
import sympy as sym

#Day 17: Trick Shot


'''
part 1 is mathematically trivial. y velocities will be symmetric around the top
        so the final y velocity will be y_min and thus v_y_initial must be -y_min-1
        using gauss theorem it can be calculated.
        interestingly this does not even depend on v_x if there is an integer A
        that satisfys x_min < A*(A+1)/2 < x_max
'''

def step(x,y, vel_x, vel_y):
    '''
    input: 4 int - current coordinates and velocities
    output: 4 int - new coordinates and velocities

    '''
    new_x = x+vel_x
    new_vel_x = max((vel_x -1,0))
    new_y = y+vel_y
    new_vel_y = vel_y -1
    return new_x, new_y, new_vel_x, new_vel_y

def check(x,y,v_x,v_y):
    '''
    input: 4 int - current coordinates and velocities
    output: int (1: inside the box, 0: outside the box, 2: indetermined)

    '''
    if x_min <= x <= x_max and y_min <= y <= y_max:
        return 1
    elif x> x_max or (v_x == 0 and v_y < y_min) :
        return 0
    else:
        return 2

def throw(v_x_initial,v_y_initial):
    '''
    input: 4 int - initial coordinates and velocities
    output: bool/int representing hit or miss

    '''
    x,y,v_x,v_y = step(0,0,v_x_initial,v_y_initial)
    control = check(x,y,v_x,v_y)
    y_max = 0
    while control >1:
        x,y,v_x,v_y= step(x,y,v_x,v_y)
        control = check(x,y,v_x,v_y)
    if control == 1:
        return 1
    else:
        return 0

def max_v_x(X1= 56, X2 = 76):
    '''
    input: ints boundaries for the target
    output: bool checks if a 0 final velocity solution for x exists
    '''
    x= sym.Symbol('x')
    eq1 = x*(x+1)/2-X2
    bound =sym.solvers.solve(eq,x)[0]
    sol = sym.N(bound)//1
    return sol*(sol+1)/2 >= X1
        


def brute_f(x1,x2,y1,y2):
    '''
    inputs: ints parameter range for x, y
    output: int number of valid solutions in parameter range
    '''
    return sum(throw(i,j) for i in range(x1,x2) for j in range(y1,y2))


#at least somewhat smart bounds for x,y velocities:
# never reaching: x < 11
# too far x > x_max = 76
# too low y < y_min
# too_high y> -y_max-1


if __name__ == '__main__':
    start_time = time()
    x_min, x_max = 56, 76
    y_min, y_max = -162, -134
    yy = -y_min -1
    print(yy*(yy+1)/2)
    print(brute_f(11,77,-163,162))
    print(time()-start_time)
