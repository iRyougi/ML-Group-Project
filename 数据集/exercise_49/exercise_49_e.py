
#!/usr/bin/python
# -*- coding: UTF-8 -*-
MAXIMUM = lambda x,y :  (x > y) * x + (x < y) * y
MINIMUM = lambda x,y :  (x > y) * y + (x < y) * x
if __name__ == '__main__':
    a = 10
b = 20
        print ('The largar one is %d' % MAXIMUM(a,b)) #2(多了两个缩进)
print ('The lower one is %d' % MINIMUM(a,b))
