_3d_array = np.zeros(1024 * 8 * 32).reshape(1024,8,32)

np.transpose(_3d_array, axes=(1, 0, 2)).shape 

# axis 변환 ( 1 -> 0 , 0 -> 1 , 2 -> 2)
