def is_palindrome(word):
    if word == word[::-1]:
        print(f"The word {word} is a palindrome.")
    else:
        print(f"The word {word} is not a palindrome.")

is_palindrome("redivider")