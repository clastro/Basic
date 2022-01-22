import numpy as np
# Q. Stack arrays a and b vertically 

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

np.vstack([a,b]) # 내가 쓴 답
np.concatenate([a, b], axis=0) # 다른 정답

# [a,b] 도 되지만 (a,b)도 됨, {a,b}는 안 된다. unhashable

# Q. Stack the arrays a and b horizontally.

np.concatenate([a, b], axis=1)
np.hstack([a,b])

# Q. Create the following pattern without hardcoding. Use only numpy functions and the below input array a.

a = np.array([1,2,3])
#> array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

np.concatenate([np.repeat(a,3),a,a,a]) # 내가 쓴 답
np.r_[np.repeat(a, 3), np.tile(a, 3)] # 정답

# Q. Get the common items between a and b

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
# array([2, 4])

np.array(list(set(a) & set(b))) #내가 쓴 답
np.intersect1d(a,b) #정답

# Q. From array a remove all items present in array b

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
# array([1,2,3,4])

np.delete(a,np.in1d(a,b)) # 내가 쓴 답
np.setdiff1d(a,b) # 정답

# Q. Get the positions where elements of a and b match

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

#> (array([1, 3, 5, 7]),)

np.where(a==b)

