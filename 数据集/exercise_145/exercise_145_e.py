# A function that transposes a matrix
def transpose(X):
    l = len(X[0])
    h = len(X)
    return [[X[j][i] for j in range(h)] for i in range(l)]

# Example run
X = [
    [1,7,1],
    [4,2,1],
    [7,9,9]
]

# Print rows to make the output readable in the console
for r in transpose(X):
print(r) #1