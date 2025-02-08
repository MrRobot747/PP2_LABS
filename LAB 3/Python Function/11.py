def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A Santa at NASA"))  # True
