# Check if a string is a palindrome
is_palindrome = lambda s: s == s[::-1]
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False

