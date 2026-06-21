def gen1():
    yield 1
    yield 2
    yield 3

gen = gen1()
print(next(gen))
print(next(gen))
print(next(gen))


# next() continues the function wherever it was paused 
# but using for loop uses next() in background so no need to use it seperately

def gen2(n):
    while(n > 0):
        yield n
        n -= 1

for i in gen2(3):
    print(i)

# there is another way to use generator similar to list comprehension 
# in which we use () instead of []

squares = (k*k for k in range(5)) # this produce one value at a time

for num in squares:
    print(num)