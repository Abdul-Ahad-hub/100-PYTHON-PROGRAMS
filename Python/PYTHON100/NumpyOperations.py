import numpy as np




def createArray():
    arr = np.array([1,2,3,4,5])
    return arr


def reshape():
    arr = np.arange(1,13)
    arr = arr.reshape(3,4)
    return arr

def multiplyArrays():
    arr1 = [[1,2,3],[4,5,6], [7,8,9]]
    arr2 = [[4,3,2], [2,4,5], [7,8,9]]
    return np.dot(arr1, arr2)


print(createArray())
print(reshape())
print(multiplyArrays())

