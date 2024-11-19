#!/usr/bin/python3
for i in range(1, 10):
print() #1
for j in range(1, i + 1):
    print("%d*%d=%d" % (i, j, i * j), end=" ")
