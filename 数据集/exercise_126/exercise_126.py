def factorial(number):
    result = 1
    while number >= 1:
        result *= number
        number -= 1
    return result
    
print(factorial(5))