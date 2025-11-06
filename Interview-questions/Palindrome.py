import re


def isPalindrome(str):
    cleanedStr = re.sub(r'[^A-Za-z0-9]', '', str).lower()
    reversedStr = cleanedStr[::-1]
    return cleanedStr == reversedStr


print(isPalindrome("mkm"))  # true
print(isPalindrome("makesh"))  # false
print("***************Another way*********************")


def checkPalindrome(str):
    cleanedStr = re.sub(r'[^A-Za-z0-9]', '', str).lower()
    left = 0
    right = len(cleanedStr) - 1
    while left < right:
        if cleanedStr[left] != cleanedStr[right]:
            return False
        left += 1
        right -= 1
    return True


print(checkPalindrome("racecar"))  # true
print(checkPalindrome("kumar"))  # false
print("***************Another way*********************")


def isPalin(str):
    def reverseString(s):
        reversed = ''
        for i in range(len(s) - 1, -1, -1):
            reversed += s[i]
        return reversed
    
    cleanedStr = str.lower()
    return cleanedStr == reverseString(cleanedStr)


print(isPalin("madam"))  # true
print(isPalin("hello"))  # false
print("***************Another way*********************")

