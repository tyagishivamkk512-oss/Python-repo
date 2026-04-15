numpad = [(1, 2, 3),
          (4, 5, 6),
          ("*",0,"#")]

# we can make 2d collection tuples in any combination of tuples,list and set 

for rows in numpad: 
    for nums in rows:
        print(nums, end= " ")
    print()


one = ['a','b','c']
two = ['d','e','f']
three = ['g','h','i']

characters = [one,two,three]

print(characters)