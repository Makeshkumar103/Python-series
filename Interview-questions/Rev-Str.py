String = 'hello'
stringReversed = ''.join(reversed(String))
print(stringReversed)  # Output: 'olleh'
print("***************Another way*********************")

ogStr = 'world'
revStr = ''.join(char for char in reversed(ogStr))
print(revStr)  # Output: 'dlrow'
print("***************Another way*********************")

str = 'JavaScript'


def rev(s):
    result = ''
    for char in s:
        result = char + result
    return result


print(rev(str))  # Output: 'tpircSavaJ'
print("***************Another way*********************")


def reverseString(str):
    reversed = ''
    for i in range(len(str) - 1, -1, -1):
        reversed += str[i]
    return reversed


originalString = 'example'
reversedString = reverseString(originalString)
print(reversedString)  # Output: 'elpmaxe'

