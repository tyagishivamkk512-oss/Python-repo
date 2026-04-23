def bill(price,discount=0,tax=0.05):
    return (price * (1 - discount ) * ( 1 + tax ))

print(bill(100, 0, 0.08))
print(bill(100))
print(bill(100, 0.1))
#in default argument we can put value of arguments directly into function,
#also we can pass any value to argument 
#however the order is mandatory, the position of default argument should be after positional argument
# def bill(price=0,dicount,tax) is incorrect
