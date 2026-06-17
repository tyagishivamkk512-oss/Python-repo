from collections import deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.extendleft([4,5,6])
d.extend([7,8])
print(d)