#list comprehensions = concise way to create list
#                      compact and easier to rad than loop 
#                      [expression for value in iterable if condition] 

square = [x**2 for x in range(0,9)]
print (square)

fruits = ['apple','amrood','santra','leechi']
firstletter = [fruit[0] for fruit in fruits]
print(firstletter)

number = [-1,-2,0,9,8,66,-5,-4]
positive = [num for num in number if num >=0]
negative = [num for num in number if num < 0]
even = [num for num in number if num%2==0]