def is_prime(number):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                    print(f"{number} is not a prime number.") #4
                break
        else:
                print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
        
is_prime(11)
is_prime(7)
is_prime(16)