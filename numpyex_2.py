import numpy as np

# creating a 1-dimensional array
arr1 = np.arange(0,16,4, dtype = np.int_)
print("array_1:",arr1)
print("array_1_shape_means dimension",arr1.shape)   #shape--> dimesnion

# creating a 2-dimensional array from arr1 1-dimensional array
arr2 = arr1.reshape((2,2))
print("array_2:",arr2)


#Basic array operation " sum, mean, max, min "
print("\nArray operations:")
print("sum of the elements in arr1:", np.sum(arr1))
print("mean of the elements in arr1:", np.mean(arr1))
print("maximum value in arr1:", np.max(arr1))
print("minimum value in arr1:", np.min(arr1))
print("sum of the elements in arr2:", np.sum(arr2))
print("mean of the elements in arr2:", np.mean(arr2))
print("maximum value in arr2:", np.max(arr2))
print("minimum value in arr2:", np.min(arr2))

###Element wise operation

print("\nElement wise operation:")
arr4 = arr1 +2
print("arr1 +2 :", arr4)
arrm = arr2 * 10
print("arrmultiplication of arr2 * 10 is :", arrm)

# Broadcasting

print("\nBroadcasting:")
arr5 = np.array([10, 20, 30, 40])
arr6 = arr1 * arr5
print("arr1*arr5 is :", arr6)

# Matrix Multiplication
print("\nMatrix Multiplication")
mat1 = np.array([[1, 2], [3,4]])   #we can use array or arange function
mat2 = np.array([[5, 6], [7,8]])
resultant_mat = np.dot(mat1, mat2)      #dot function is multiplication
print("Shape of mat1 and mat2 matrix is :", mat1.shape, mat2.shape)
print("mulitplication of two matrix are:", resultant_mat)