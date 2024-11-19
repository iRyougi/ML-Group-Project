# A function that multiplies two matrices
def multiply_matrices(X, Y):
    return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]

# Example run
X = [
    [1,7,1],
    [4,2,1],
    [7,9,9]
]

Y = [
    [1,8,1],
    [9,0,3],
    [2,4,7]
]

# Print rows to make the output readable in the console
for r in multiply_matrices(X, Y):
print(r) #1