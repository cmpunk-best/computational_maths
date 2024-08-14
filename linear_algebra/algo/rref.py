

# ROW REDUCED ECHELON FORM
# (row, col) is the way
import numpy as np


def rref(matrix):
    #1. step one check if the pivot pos is zero
    matrix = check_pivot_pos(matrix)
    matrix = make_pivot_zeros(matrix)
    pass

def make_pivot_zeros(matrix):
#    if():
#        return 
#    else:
#        return make_pivot_zeros(matrix)
#    pass
    multiplier = matrix[i+1][j]/matrix[i][j]
    row_operation(multiplier, row1 = i , row2 = i+1 )


def row_operation(multiplier, row1 , row2):
    matrix[row2][j] = matrix[row2][j] - matrix[row1][j]*multiplier
    

def check_pivot_pos(matrix):
    counter = 0
    while (matrix[0][0] == 0):  
        matrix = interchange(matrix)
        counter = counter + 1
        if(counter == matrix.shape[0]): # No pivot in first column
            break
    print(matrix)
    return matrix

def interchange(matrix):
    return np.roll(matrix,-1,axis=0) #Need to see what axis does

mat = np.array([[0,2,3],[2,3,4],[0,0,0]])
rref(mat)
