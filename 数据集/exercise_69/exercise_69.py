nmax = 50
n = int(34)
num = []
for i in range(n):
        num.append(i + 1)
i = 0
k = 0
m = 0
while m < n - 1:
        if num[i] != 0: 
                k += 1
        if k == 3:
                num[i] = 0
                k = 0
                m += 1
        i += 1
        if i == n: 
                i = 0

i = 0
while num[i] == 0: 
        i += 1
print (num[i])
