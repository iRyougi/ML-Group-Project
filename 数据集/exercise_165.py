# Document a function with a docstring """ """
def add(a, b):
    """
    This function adds two numbers and returns the result.
        - a is an integer
        - b is an integer

        - res is the result
    """
    res = a + b
    return res


# Example use:
help(add)