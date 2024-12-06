import numpy as np
def dot_op(array1,array2):
    if(array1.shape!=array2.shape):
        print("Their orders are different, hence getting dot product is not possible.")
        return
    else:
        for i in range(array1.shape[0]):
            for j in range(array1.shape[1]):
                result = [array1[i][j] * array2[i][j]]
        print("Their dot product is : \n", np.array(result))
        return

def matrix_op(array1,array2):
    if(array1.shape[1]!=array2.shape[0]):
        print("Matrix multiplication is not possible.")
        return
    else:
        for i in range(array1.shape[0]):
            for j in range(array2.shape[1]):
                for k in range(array1.shape[1]):
                    result = [sum(array1[i][k] * array2[k][j])]
        print("Their product matrix is : \n", np.array(result))
        return

def matrix_operation(array1,array2,operation):
    if(operation=="dot"):
        dot_op(array1,array2)
    elif(operation=="matrix"):
        matrix_op(array1,array2)
    else:
        print("Invalid operation")
        return

row1 = int(input("Enter the no. of rows in array1 : "))
col1 = int(input("Enter the no. of columns in array1 : "))
a1 = []
print("Enter the elements row-wise : ")
for i in range(row1):
    row = input().split()
    row = [int(x) for x in row]
    a1.append(row)
array1=np.array(a1)

row2 = int(input("Enter the no. of rows in array2 : "))
col2 = int(input("Enter the no. of columns in array2 : "))
a2 = []
print("Enter the elements row-wise : ")
for i in range(row2):
    row = input().split()
    row = [int(x) for x in row]
    a2.append(row)
array2=np.array(a2)

operation=input("Operation to perform : ")

matrix_operation(array1,array2,operation)