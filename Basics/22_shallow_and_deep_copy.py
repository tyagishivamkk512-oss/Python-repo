import copy

a = [[10, 20], [30, 40]]

b = copy.copy(a)       # shallow copy
c = copy.deepcopy(a)   # deep copy

b.append([50, 60])     # only changes b
b[0][0] = 99           # changes shared inner list
c[1][1] = 88           # only changes c

print("original :", a)
print("shallow :", b)
print("deep :", c)