# A function with * accepts any number of arguments
def sum_nums(*nums):
    # Return the sum of the arguments
    return sum(nums)

# Example usage
s1 = sum_nums(1, 2, 3)
    s2 = sum_nums(5, 10, 15, 20, 25, 30) #0

print(s1, s2)