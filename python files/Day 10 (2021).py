import numpy as np


#DAY 10

def get_brackets(txt ='..//input files//input_d10.txt'):
    '''
    input: AoC text file
    output: list of strings representing the series of brackets
    '''
    with open(txt,'r') as fob:
        inp = fob.readlines()
    return inp

def ini_dicts():
    '''
    output: helper dictionaries
    '''
    openb = ['(','[','{','<']
    closedb=[')',']','}','>']
    bracket_dic = { '{':'}', '[':']', '(':')', '<':'>'}
    error_vals= {')': 3, ']':57, '}':1197, '>':25137}
    comp_cost={'(':1, '[':2,'{':3, '<':4}
    return openb, closedb, bracket_dic, error_vals, comp_cost


#could use deuqe from collections, but for this task a
#list acting as a stack is fast enough

def get_error(entry):
    '''
    inout: iterable representing the brackets
    output: int error value
    '''
    stack =[]
    for i in entry:
        if i in openb:
            stack.append(i)
        elif i in closedb:
            if bracket_dic[stack[-1]] == i:
                stack.pop()
            else:
                return error_vals[i]

def error_list(liste):
    '''
    input: iterable of bracket iterables
    output: list of error values, list of incomplete strings
    '''
    errors =[]
    incomplete=[]
    for i in liste:
        a= get_error(i)
        if a:
            errors.append(a)
        else:
            incomplete.append(i)
    return errors, incomplete

def completion_cost(entry):
    '''
    input: iterable of (incoplete) brackets
    output: int completion cost

    '''
    stack =[]
    for i in entry[:-1]:
        if i in openb:
            stack.append(i)
        elif i in closedb:
            if bracket_dic[stack[-1]] == i:
                stack.pop()
    total_cost = 0
    sta = stack[::-1]
    for j in sta:
        total_cost= total_cost*5+ comp_cost[j]
    return total_cost







if __name__ == '__main__':
    openb, closedb, bracket_dic, error_vals, comp_cost = ini_dicts()
    inputs = get_brackets()
    errors, incomplete = error_list(inputs)
    print('The sum of all errors os:', sum(errors))
    costs = list(completion_cost(x) for x in incomplete)
    costs.sort()
    print('The total completion cost is:', costs[23])
