def as_fahrenheit(celcius):
    return 9/5 * celcius + 32
    
c = 37
f = as_fahrenheit(c)

print(f"{c} is {f} in Fahrenheits")