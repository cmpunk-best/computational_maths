
"""

Matrix multiply

"""
import numpy as np


 
def multiply(matrix1, matrix2):
    if not column_row_check(matrix1.shape,matrix2.shape):
        raise ValueError(" Cannot multiply ")
    else:
        col = np.zeros((matrix1.shape[0],matrix2.shape[1]))
        for i in range(0, matrix2.shape[1]):
            col[:,i] = vector_prod(matrix1,(matrix2[:,i]).reshape(-1,1)).flatten()
    print(col)
                    

def vector_prod(matrix1,column_vector):
    column = np.zeros((matrix1.shape[0],1))
    for k in range(0, matrix1.shape[0]):
        for j in range(0, column_vector.shape[0]):
            column[k][0] += column_vector[j][0] * matrix1[k][j]
    
    print(column)
    return column


def column_row_check(shape1,shape2):
    return True if shape1[1] == shape2[0] else False


#mat1 = np.array([[0,2,3],[0,3,4],[0,0,0]])
#mat2 = np.array([[0,2,3],[0,3,4],[0,0,0]])
#
#multiply(mat1, mat2)
#
 
