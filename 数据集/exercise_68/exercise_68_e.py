
#!/usr/bin/python
# -*- coding: UTF-8 -*-
n = int(8)
m = int(5)
def move(array,n,m):
        array_end = array[n - 1]
        for i in range(n - 1,-1,- 1):
        array[i] = array[i - 1] # 1
        array[0] = array_end
        m -= 1
        if m > 0:move(array,n,m)

number = [2, 8, 6, 1, 78, 45, 34, 2]
print ("original:",number)
move(number,n,m)
print ("altered:",number)

