import numpy as np


#Day 13: Transparent Origami 

def prepare_inputs(textfile = '../input files/input_d13.txt' ):
    '''
    takes the inputs from a textfiile
    and generates tuples with dots-coordinates and fold coordinates
    '''
    with open(textfile,'r') as fob:
        inp = fob.readlines()
    numerals = tuple(str(i) for i in range(0,10))
    points, folding_lines = [],[]
    for i in inp:
        if i[0] in numerals:
            temp = i.split(',')
            points.append( (int(temp[0]),int(temp[1]) ) )
        elif i[0:4] == 'fold':
            if i[11]=='x':
                folding_lines.append((int(i[13:-1]),0))
            else:
                folding_lines.append((0,int(i[13:-1])))
    return points, folding_lines
            

def dots_on_paper(dots):
    '''returns numpy array with 1s representing dots'''
    size = np.max(np.array(dots).T, axis=1)
    size+=10
    paper= np.zeros(size)
    for i in dots:
        paper[i[0],i[1]] =1
    return paper

def fold(paper, fold_line):
    '''
    returns the fold the paper (numpy array) at the specified fold_line( tuple )
    '''
    if fold_line[1] == 0:
        x = fold_line[0]
        new_paper = paper[0:x,:] +np.flipud(paper[x+1:2*x+1,:])
    else:
        y= fold_line[1]
        new_paper = paper[:,0:y] +np.fliplr(paper[:,y+1:2*y+1])
    new_paper[new_paper>1] =1
    return new_paper

def fold_all(paper, folds):
    '''
    input:
        nparray representing dots on paper
        list of folding instructions
            
    output:
        nparray representing dots on folded paper
    '''
    pap = paper
    for i in folds:
        pap = fold(pap, i)
    return pap

def printout(paper):
    ''' prints the secret code in a readable format'''
    out = ''
    pap = paper.T
    for i in pap:
        out += '\n'
        for j in i:
            if j:
                out+= '#'
            else:
                out+= ' '
    print(out)

if __name__ == '__main__':
    
    dots, folds = prepare_inputs()
    paper = dots_on_paper(dots)
    folded = fold(paper,folds[0])
    print('number of dots: ', np.sum(folded))
    pap = fold_all(paper,folds)
    printout(pap)
            
