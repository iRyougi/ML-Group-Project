
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sys import stdout
a = int(1234)
aa = []
aa.append(a % 10)
aa.append(a % 100 / 10)
aa.append(a % 1000 / 100)
aa.append(a / 1000)
for i in range(4):
        aa[i] += 5
        aa[i] %= 10
for i in range(2):
        aa[i],aa[3 - i] = aa[3 - i],aa[i]
for i in range(3,-1,-1):
stdout.write(str(aa[i])) # 1
