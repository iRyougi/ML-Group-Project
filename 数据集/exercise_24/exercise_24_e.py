#!/usr/bin/python
from functools import reduce

a = 2.0
b = 1.0
l = []
l.append(a / b)
for n in range(1, 20):
b, a = a, a + b #1
l.append(a / b)
print(reduce(lambda x, y: x + y, l))
