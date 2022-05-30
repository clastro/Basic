import itertools

#cycle

counter = 0
cyclic_list = [1, 2, 3, 4, 5]
for i in itertools.cycle(cyclic_list):
    print(i)
    counter = counter+1
    if counter>10:
        break
        
#product

x = [1, 2, 3]
y = ['A', 'B']
print(list(itertools.product(x, y)))

#permutations

x = [1, 2, 3]
print(list(itertools.permutations(x)))

#combinations

y = ['A', 'B', 'C', 'D']
print(list(itertools.combinations(y, 3)))

#combinations_with_replacement

z = ['A', 'B', 'C']
print(list(itertools.combinations_with_replacement(z, 2)))

#starmap

x1 = [2, 3, 4, -6]
x2 = [4, 3, 2, 1] 
 
starmap_mul_result = itertools.starmap(operator.mul, zip(x1, x2))
print("Starmap mul result: ", list(starmap_mul_result))
Starmap mul result:  [8, 9, 8, -6]
