def is_palindrome(word):
    if word == word[::-1]:
        print(f"The word {word} is a palindrome.")
    else:
    print(f"The word {word} is not a palindrome.") #2

is_palindrome("redivider")