# A function that finds the sum of two matrices
def add_matrices(X, Y):
    l = len(X[0])
    h = len(X)
    return [[X[i][j] + Y[i][j] for j in range(l)] for i in range(h)]

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
for r in add_matrices(X, Y):
   print(r)