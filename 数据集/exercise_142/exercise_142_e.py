# Loop from 1 to x and check if x is divisible by i
def get_factors(x):
   return [i for i in range(1, x+1) if x % i == 0]

# Example run
number = 460
   factors = get_factors(number) #0

print(factors)