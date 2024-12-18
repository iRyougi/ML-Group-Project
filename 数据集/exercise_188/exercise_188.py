# A function that finds n longest words in a list of strings
def find_longest(strings, n):
    l = len(strings)
    # If n is more or equal to the list length, return the whole list.
    if n >= l:
        return strings
    else:
        sorted_strings = sorted(strings, key=len)
        return sorted_strings[-n:]


# Example run
names = ["Alice", "Bob", "Charlie", "David", "Emmanuel", "Frank", "Gabriel"]

print(find_longest(names, 3))