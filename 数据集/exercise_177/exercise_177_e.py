items = ["Alice", 2, 3, "Bob", "Charlie", 30]

# Let's remove numbers

    names = filter(lambda x: not isinstance(x, int), items) #0

print(list(names))