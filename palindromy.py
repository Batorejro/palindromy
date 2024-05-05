#wersja 1
"""
def czy_palindrom(n):
    return "tak" if n == n[::-1] else "nie"

print(czy_palindrom(input()))

"""
# wersja 2


def is_palindrome(string):
    inverse = string[::-1]
    if string == inverse:
        return True
    else:
        return False
print(is_palindrome(input()))

