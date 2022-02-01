# Q. Convert the function maxx that works on two scalars, to work on two arrays?

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max(a, b)
#> array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])

#내가 쓴 답
def pair_max(x,y):
    r = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] >= y[i]:
            r[i] = x[i]
        else:
            r[i] = y[i]
    return r

#정답
 def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

pair_max = np.vectorize(maxx, otypes=[float])

  
pair_max(a,b)
