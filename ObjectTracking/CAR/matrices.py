
m = [[8,7,1,2,3],
     [1,5,2,9,0],
     [8,2,2,4,1]]

### TODO: Use for loops to multiply each matrix element by 5
###       Store the answer in the r variable. This is called scalar
###       multiplication
###
### HINT: First write a for loop that iterates through the rows
###       one row at a time
###
###       Then write another for loop within the for loop that
###       iterates through the columns
###
###       If you used the variable i to represent rows and j
###       to represent columns, then m[i][j] would give you
###       access to each element in the matrix
###
###       Because r is an empty list, you cannot directly assign
###       a value like r[i][j] = m[i][j]. You might have to
###       work on one row at a time and then use r.append(row).
r = []

for i in range(len(m)):
    row = []
    for j in range(len(m[i])):
        row.append(m[i][j] * 5)
    r.append(row)

### TODO: Write a function called matrix_print()
###       that prints out a matrix in
###       a way that is easy to read.
###       Each element in a row should be separated by a tab
###       And each row should have its own line
###       You can test our your results with the m matrix

### HINT: You can use a for loop within a for loop
### In Python, the print() function will be useful
### print(5, '\t', end = '') will print out the integer 5,
###    then add a tab after the 5. The end = '' makes sure that
###    the print function does not print out a new line if you do
###    not want a new line.

### Your output should look like this
### 8   7   1   2   3
### 1   5   2   9   5
### 8   2   2   4   1

def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], '\t', end = '')
        print()

m = [
    [8, 7, 1, 2, 3],
    [1, 5, 2, 9, 5],
    [8, 2, 2, 4, 1]
]

matrix_print(m)

### TODO: Write a function called matrix_addition that
###     calculate the sum of two matrices
###
### INPUTS:
###    matrix A _ an m x n matrix
###    matrix B _ an m x n matrix
###
### OUPUT:
###   matrixSum _ sum of matrix A + matrix B

def matrix_addition(matrixA, matrixB):

    # initialize matrix to hold the results
    matrixSum = []

    # matrix to hold a row for appending sums of each element
    row = []

    # TODO: write a for loop within a for loop to iterate over
    # the matrices

    for i in range(len(matrixA)):
        for j in range(len(matrixA[i])):
            row.append(matrixA[i][j] + matrixB[i][j])
        matrixSum.append(row)
        row = []



    # TODO: As you iterate through the matrices, add matching
    # elements and append the sum to the row variable



    # TODO: When a row is filled, append the row to matrixSum.
    # Then reinitialize row as an empty list

    return matrixSum

### When you run this code cell, your matrix addition function
### will run on the A and B matrix.

A = [
    [2,5,1],
    [6,9,7.4],
    [2,1,1],
    [8,5,3],
    [2,1,6],
    [5,3,1]
]

B = [
    [7, 19, 5.1],
    [6.5,9.2,7.4],
    [2.8,1.5,12],
    [8,5,3],
    [2,1,6],
    [2,33,1]
]

matrix_addition(A, B)


### TODO: Write a function that receives a matrix and a column number.
###       the output should be the column in the form of a list


### Example input:
# matrix = [
#    [5, 9, 11, 2],
#    [3, 2, 99, 3],
#    [7, 1, 8, 2]
# ]
#
# column_number = 1

### Example output:
# [9, 2, 1]
#

def get_column(matrix, column_number):
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])
    return column

### TODO: Write a function called dot_product() that
###       has two vectors as inputs and outputs the dot product of the
###       two vectors. First, you will need to do element-wise
###       multiplication and then sum the results.

### HINT: You wrote this function previously in the vector coding
###        exercises

def dot_product(vector_one, vector_two):
    return sum([vector_one[i] * vector_two[i] for i in range(len(vector_one))])


### TODO: Write a function called matrix_multiplication that takes
###       two matrices,multiplies them together and then returns
###       the results
###
###       Make sure that your function can handle matrices that contain
###       only one row or one column. For example,
###       multiplying two matrices of size (4x1)x(1x4) should return a
###       4x4 matrix

def get_row(matrix, row):
    return matrix[row]

def matrix_multiplication(matrixA, matrixB):

    ### TODO: store the number of rows in A and the number
    ###       of columns in B. This will be the size of the output
    ###       matrix
    ### HINT: The len function in Python will be helpful
    m_rows = len(matrixA)
    p_columns = len(matrixB[0])


    # empty list that will hold the product of AxB
    result = []


    ### TODO:  Write a for loop within a for loop. The outside
    ###        for loop will iterate through m_rows.
    ###        The inside for loop will iterate through p_columns.

    ### TODO:  As you iterate through the m_rows and p_columns,
    ###        use your get_row function to grab the current A row
    ###        and use your get_column function to grab the current
    ###        B column.


    ### TODO: Calculate the dot product of the A row and the B column


    ### TODO: Append the dot product to an empty list called row_result.
    ###       This list will accumulate the values of a row
    ###        in the result matrix
    row_result = []

    for i in range(m_rows):
        for j in range(p_columns):
            row_result.append(dot_product(get_row(matrixA, i), get_column(matrixB, j)))
        result.append(row_result)
        row_result = []

    ### TODO: After iterating through all of the columns in matrix B,
    ###       append the row_result list to the result variable.
    ###       Reinitialize the row_result to row_result = [].
    ###       Your for loop will move down to the next row
    ###       of matrix A.
    ###       The loop will iterate through all of the columns
    ###       taking the dot product
    ###       between the row in A and each column in B.

    ### TODO: return the result of AxB


    return result

### TODO: Write a function called transpose() that
###       takes in a matrix and outputs the transpose of the matrix

def transpose(matrix):
    matrix_transpose = []
    for i in range(len(matrix[0])):
        matrix_transpose.append(get_column(matrix, i))

    return matrix_transpose

### TODO: Write a function called matrix_multiplication() that
###       takes in two matrices and outputs the product of the two
###       matrices

### TODO: Copy your dot_product() function here so that you can
###       use it in your matrix_multiplication function

def matrix_multiplication(matrixA, matrixB):
    product = []

    for i in range(len(matrixA)):
        row = []
        for j in range(len(matrixB[0])):
            row.append(dot_product(matrixA[i], get_column(matrixB, j)))
        product.append(row)

def identity_matrix(n):

    identity = []

    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        identity.append(row)

    # TODO: Write a nested for loop to iterate over the rows and
    # columns of the identity matrix. Remember that identity
    # matrices are square so they have the same number of rows
    # and columns

    # Make sure to assign 1 to the diagonal values and 0 everywhere
    # else

    return identity


    ## TODO: Take the transpose of matrixB and store the result
    ##       in a new variable


    ## TODO: Use a nested for loop to iterate through the rows
    ## of matrix A and the rows of the tranpose of matrix B

    ## TODO: Calculate the dot product between each row of matrix A
    ##         with each row in the transpose of matrix B

    ## TODO: As you calculate the results inside your for loops,
    ##       store the results in the product variable


    ## TODO:
    return product


# TODO: Copy your matrix multiplication function and any other helper
# funcitons here from the previous exercises

def matrix_multiplication(matrixA, matrixB):
    product = []

    for i in range(len(matrixA)):
        row = []
        for j in range(len(matrixB[0])):
            row.append(dot_product(matrixA[i], get_column(matrixB, j)))
        product.append(row)

    return product

### TODO: Write a function called inverse_matrix() that
###       receives a matrix and outputs the inverse
###
###       You are provided with start code that checks
###       if the matrix is square and if not, throws an error
###
###       You will also need to check the size of the matrix.
###       The formula for a 1x1 matrix and 2x2 matrix are different,
###       so your solution will need to take this into account.
###
###       If the user inputs a non-invertible 2x2 matrix or a matrix
###       of size 3 x 3 or greater, the function should raise an
###       error. A non-invertible
###       2x2 matrix has ad-bc = 0 as discussed in the lesson
###
###       Python has various options for raising errors
###       raise RuntimeError('this is the error message')
###       raise NotImplementedError('this functionality is not implemented')
###       raise ValueError('The denominator of a fraction cannot be zero')

def scalar_multiply(scalar, matrix):
    # TypeError: can't multiply sequence by non-int of type 'float'

    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(scalar * matrix[i][j])
        result.append(row)
    return result
    # return [scalar * v for v in vector]


def inverse_matrix(matrix):

    inverse = []

    if len(matrix) != len(matrix[0]):
        raise ValueError('The matrix must be square')

    ## TODO: Check if matrix is larger than 2x2.
    ## If matrix is too large, then raise an error

    ## TODO: Check if matrix is 1x1 or 2x2.
    ## Depending on the matrix size, the formula for calculating
    ## the inverse is different.
    # If the matrix is 2x2, check that the matrix is invertible

    # If the matrix is 1x1, then the inverse is 1 over the value
    # of the matrix

    if len(matrix) == 1:
        inverse.append([1/matrix[0][0]])
    elif len(matrix) == 2:
        if matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] == 0:
            raise ValueError('The matrix is not invertible')
        else:
            inverse.append([matrix[1][1], -matrix[0][1]])
            inverse.append([-matrix[1][0], matrix[0][0]])
            inverse = scalar_multiply(1/(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]), inverse)
    else:
        raise ValueError('The matrix is too large')




    ## TODO: Calculate the inverse of the square 1x1 or 2x2 matrix.

    return inverse

assert inverse_matrix([[100]]) == [[0.01]]
assert inverse_matrix([[4, 5], [7, 1]]) == [[-0.03225806451612903, 0.16129032258064516],
                                            [0.22580645161290322, -0.12903225806451613]]