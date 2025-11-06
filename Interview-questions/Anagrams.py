def areAnagrams(str1, str2):
    # remove spaces and convert to lowercase
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    
    # check the length are different
    if len(str1) != len(str2):
        return False
    
    # create chatacter frequency maps
    frequencyMap1 = {}
    frequencyMap2 = {}
    for char in str1:
        frequencyMap1[char] = frequencyMap1.get(char, 0) + 1
    for char in str2:
        frequencyMap2[char] = frequencyMap2.get(char, 0) + 1
    # compare frequency maps
    for char in frequencyMap1:
        if frequencyMap1[char] != frequencyMap2.get(char, 0):
            return False
    return True


print(areAnagrams("listen", "silent"))  # Output: true
print(areAnagrams("hello", "world"))

