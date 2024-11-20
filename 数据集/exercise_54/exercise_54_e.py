
#!/usr/bin/python
# -*- coding: UTF-8 -*-
if __name__ == '__main__':
a = 16 #1
b = a >> 4
c = ~(~0 << 4)
d = b & c
print ('%o\t%o' %(a,d))
