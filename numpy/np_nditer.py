
import numpy as np

a=np.array([[2,4,5],[3,6,7],[4,8,9]])
for x in np.nditer(a, flags = ['external_loop'],order='F'): #Transpose array
  print(x)

# [2,3,4]
  [4,6,8]
  [5,7,9]

arr = np.array([1, 2, 3, 4, 5])  

it = np.nditer(arr, flags=['c_index'])

while not it.finished:
    idx = it.index
    print(arr[idx], end=' ')
    it.iternext()
    
# 1 2 3 4 5
