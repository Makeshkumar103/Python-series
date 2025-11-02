def count_character_occurrences(input_str):
    counts = {}
    for char in input_str:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

input_string = "hello world"
result = count_character_occurrences(input_string)

print(result)  # { 'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1 }
print("***************Another way*********************")

def char_count(input_str):
    char_map = {}
    for char in input_str:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    return char_map

input_text = "character"
output = char_count(input_text)
print(output)  # { 'c': 2, 'h': 1, 'a': 2, 'r': 2, 't': 1, 'e': 1 }
print("***************Another way*********************")

