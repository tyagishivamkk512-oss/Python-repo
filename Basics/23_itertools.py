from itertools import product, permutations, combinations, accumulate, groupby
from itertools import count, cycle, repeat

a = [1,2,3]
b = [4,5,6]

prod = product(a,b) # this gives an iterator
print(list(prod))
print()

perm = permutations(a) # will give all permutations of a
print(list(perm))
# using it with argument like (a, 2) will make permutations of 2 numbers only

comb = combinations(b, 2) # now it will make combinations of 2 from b
print(list(comb)) 
# there is combination_with_replacement which is just like combination but can repeat elements

acc = accumulate(a)
print(list(acc)) # it will progrssively add elemnts and make a list


for j in count(5,2):
    print(j)
    if j == 99:
        break # it will print starting from 5 with step of 2 

for k in cycle(b):
    print(k)
    # will print elements of b in cycle

for l in repeat(7): # using(7,5) will print 7 five times
    print(l)