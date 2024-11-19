# A function that finds the intersection between two lists
def intersection(l1, l2):
    return [element for element in l1 if element in l2]

# Example run
names1 = ["Alice", "Bob", "Charlie"]
names2 = ["Alice", "Bob", "David", "Emmanuel"]

    names_in_common = intersection(names1, names2) #0

print(f"Common names among the lists are {names_in_common}")