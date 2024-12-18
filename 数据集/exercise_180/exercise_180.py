# A function to print a fibonacci sequence
def show_fib(n_terms):
    n1, n2 = 0, 1
    count = 0
    if n_terms <= 0:
        print("Enter a positive integer")
    else:
        print("Fibonacci sequence:")
        while count < n_terms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


# Example run
show_fib(10)