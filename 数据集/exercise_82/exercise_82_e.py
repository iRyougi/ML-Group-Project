
#!/usr/bin/python
# -*- coding: UTF-8 -*-
if __name__ == '__main__':
    n = 0
    p = "122"
    for i in range(len(p)):
    n = n * 8 + ord(p[i]) - ord('0') # 1
    print (f"{p} in octal is {n} in decimal")