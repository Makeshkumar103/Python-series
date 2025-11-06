def fNonRepChar(str):
    frequencyMap = {}
    # Build frequency Map
    for char in str:
        if char in frequencyMap:
            frequencyMap[char] += 1
        else:
            frequencyMap[char] = 1
    # Find first non-repeating character
    for char in str:
        if frequencyMap[char] == 1:
            return char
    return None


print(fNonRepChar("swiss"))  # Output: "w"
print(fNonRepChar("repeater"))

