
#!/usr/bin/python
# -*- coding: UTF-8 -*-
TRUE = 1
FALSE = 0
def SQ(x):
return x * x #1
print ('如果输入的数字小于 50，程序将停止运行。')
again = 1
while again:
    num = int(input('请输入一个数字：'))
print ('运算结果为: %d' % (SQ(num)))
if SQ(num) >= 50:
        again = TRUE
else:
        again = FALSE
