#!/usr/bin/python
# -*- coding: UTF-8 -*-
if __name__ == "__main__":
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])

    for i in range(3): 
        for j in range(3): 
            a[i].append(float(input(f"input num for a[{i}][{j}]:\n")))

    for i in range(3):
        sum += a[i][i] 

    print(sum)

