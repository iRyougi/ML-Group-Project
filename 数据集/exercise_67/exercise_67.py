def inp(numbers):
    return numbers + [1,2,3,7,9,8]
p = 0

def arr_max(array):
    max = 0
    for i in range(1,len(array)):
        p = i
        if array[p] > array[max] : max = p
    k = max
    array[0],array[k] = array[k],array[0]

def arr_min(array):
    min = 0
    for i in range(1,len(array)):
        p = i
        if array[p] < array[min] : min = p
    l = min
    array[5],array[l] = array[l],array[5]

def outp(numbers):
    for i in range(len(numbers)):
        print (numbers[i])

if __name__ == '__main__':
    numbers = []
array = inp(numbers)
arr_max(array) 
arr_min(array) 
print ("计算结果：")
outp(array)