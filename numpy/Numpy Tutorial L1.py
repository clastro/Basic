# Difficulty Level: L1 

# Q. Import numpy as `np` and print the version number.

import numpy as np
print(np.__version__)

# Q. Create a 1D array of numbers from 0 to 9 Desired output
#> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

np.array(range(0,10)) #내가 쓴 답
np.arange(10)

# Q. Create a 3×3 numpy array of all True’s

np.array([[True,True,True], [True, True,True], [True, True,True]], np.bool) # 내가 쓴 답

np.full((3,3), 1, dtype=bool)
np.ones((3,3), dtype=bool)

# Q. Extract all odd numbers from arr Input
#> array([1, 3, 5, 7, 9])

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr[(arr % 2 == 1)] # 내가 쓴 답
arr[arr % 2 == 1]


# Q. Replace all odd numbers in arr with -1 Input:

arr[arr % 2 == 1] = -1
arr.put([1,3,5,7,9],-1)
np.where(arr % 2 ==1,-1,arr)


# Q. Convert a 1D array to a 2D array with 2 rows Input:

A = np.arange(10)

# Desired Output:
#> array([[0, 1, 2, 3, 4],
#>        [5, 6, 7, 8, 9]])

A.reshape(2,-1)
