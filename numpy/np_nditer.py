
import numpy as np

a=np.array([[2,4,5],[3,6,7],[4,8,9]])
for x in np.nditer(a, flags = ['external_loop'],order='F'): #Transpose array
  print(x)

