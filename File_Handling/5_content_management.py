# we can use try method to open files

file = open('text.txt', 'w')
try:
    file.write('some work...')
finally:
    file.close()