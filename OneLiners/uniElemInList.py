# Get Unique elements from a List in Python (remove duplicates)
unique_elements = lambda lst: list(set(lst))
print(unique_elements([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(unique_elements(['apple', 'banana', 'apple', 'orange']))  # Output:
# Output: ['apple', 'banana', 'orange']

# Get Unique elements while preserving order
unique_elements_ordered = lambda lst: list(dict.fromkeys(lst))
print(unique_elements_ordered([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(unique_elements_ordered(['apple', 'banana', 'apple', 'orange']))  # Output: ['apple', 'banana', 'orange']

# Get Unique elements using list comprehension
unique_elements_comp = lambda lst: []
def unique_elements_comp(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
print(unique_elements_comp([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(unique_elements_comp(['apple', 'banana', 'apple', 'orange']))  # Output

