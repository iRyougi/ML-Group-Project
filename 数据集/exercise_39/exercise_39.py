#!/usr/bin/python
# -*- coding: UTF-8 -*-
if __name__ == '__main__':
    a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100, 0]
    
    print('原始列表:')
    for i in range(len(a)):
        print(a[i])
    
    number = int(input("\n插入一个数字:\n"))
    end = a[10]
    
    if number > end:
        a[10] = number
    else:
        for i in range(10):
            if a[i] > number:
                temp1 = a[i]
                a[i] = number
                for j in range(i + 1, 11):
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                break
    
    print('排序后列表:')
    for i in range(11):
        print(a[i])
