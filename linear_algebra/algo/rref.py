

# ROW REDUCED ECHELON FORM
# (row, col) is the way
import numpy as np


def rref(matrix):
    #1. step one check if the pivot pos is zero
    #FORWARD PHASE
    forward_phase(matrix) #Gaussian Elimination
    #BACKWARD PHASE
    #backward_phase(matrix) #Jordan 

def forward_phase(matrix):
    for i in range(0, matrix.shape[1]):
        matrix,row = check_pivot_pos(matrix,column=i)
        matrix = make_pivot_pos_one(matrix,column=i,row=row)
        matrix = make_below_entries_zero(matrix,row=row,column=i)
        print(matrix)

def make_below_entries_zero(matrix,row,column):
    for i in range(1,matrix.shape[0]):
        if(row+i == matrix.shape[0]):
            break
        else:
            entry = matrix[row+i][column]
            if(entry != 0):
                matrix = row_substraction(multiplier=entry,matrix=matrix,row1=row, row2=row+i)
    return matrix

#Applies on row2 : row2 = row2 - multiplier*row1
def row_substraction(row1,row2,matrix,multiplier):
    for i in range(0, matrix.shape[1]):
        matrix[row2][i] -= matrix[row1][i]*multiplier
    return matrix


def make_pivot_pos_one(matrix,row,column):

    multiplier = 1 if matrix[row][column] == 0 else 1.0/matrix[row][column] 
    return multiplier_operation(multiplier,matrix,row)


def multiplier_operation(multiplier,matrix,row=0):
    for i in range(0,matrix.shape[1]): #multiplier effect happens on the whole row(which is total columns)
        matrix[row][i] = matrix[row][i]*multiplier

    return matrix
    

def check_pivot_pos(matrix,column):
    counter = 0
    row = check_prev_column(matrix,column-1) if (column > 0)  else 0
    result=np.copy(matrix)
    while (matrix[row][column] == 0):  
        result = np.copy(matrix)
        result[row:] = interchange(matrix[row:])
        counter = counter + 1
        if(counter == matrix.shape[0]): # No pivot in first column
            break
    return result , row
def check_prev_column(matrix,p_column):
    flag = False
    for i in range(0,matrix.shape[0]):
        if matrix[i][p_column] != 0:
            max_row = i+1
            flag = True
    return max_row if flag else 0

def interchange(matrix):
    return np.roll(matrix,-1,axis=0) #roll over row axis

mat = np.array([[0,2,3],[0,3,4],[0,0,0]])
rref(mat)
