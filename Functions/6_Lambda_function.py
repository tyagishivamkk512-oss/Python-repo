# function name = lambda arguments: expression 
rem = lambda x, y: x % y # we have defined remainder function using lambda
print(rem(3,2))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

c = [x for x in a if x%2==0]
print(c)