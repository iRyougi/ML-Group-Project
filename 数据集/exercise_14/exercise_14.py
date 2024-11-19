#!/usr/bin/python3

def reduceNum(n):
    if not isinstance(n, int) or n <= 0:
        print('请输入一个正确的数字!')
        return  # Return early on invalid input
    
    print('{} = '.format(n), end="")

    if n == 1:
        print(n)
        return
    
    factors = []  # To store the prime factors
    for index in range(2, n + 1):
        while n % index == 0:
            factors.append(index)
            n //= index
    
    # Print the prime factorization
    print(' * '.join(map(str, factors)))

# Test the function with different values
reduceNum(90)
reduceNum(100)
