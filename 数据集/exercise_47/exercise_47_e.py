
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def exchange(a,b):
    a,b = b,a
    return (a,b)
 
if __name__ == '__main__':
    x = 10
    y = 20
            print ('x = %d,y = %d' % (x,y)) #2(多了两个缩进)
    x,y = exchange(x,y)
    print ('x = %d,y = %d' % (x,y))
