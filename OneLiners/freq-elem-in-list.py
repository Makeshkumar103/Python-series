# find most frequent element in a list
from collections import Counter
def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]    
print(most_frequent([1, 2, 3, 1, 2, 1, 1]))  # Output: 1
print(most_frequent(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))  # Output: apple 

# find most frequent element in list using max and set
def most_frequent_max_set(lst):
    return max(set(lst), key=lst.count)
print(most_frequent_max_set([1, 2, 3, 1, 2, 1, 1]))  # Output: 1
print(most_frequent_max_set(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))  # Output: apple


# find least frequent element in a list in one line
def least_frequent(lst):
    return Counter(lst).most_common()[-1][0]
print(least_frequent([1, 2, 3, 1, 2, 1, 1]))  # Output: 3
print(least_frequent(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))  # Output: orange
# find frequency of each element in a list
def frequency_count(lst):
    return dict(Counter(lst))
print(frequency_count([1, 2, 3, 1, 2, 1, 1]))  # Output: {1: 4, 2: 2, 3: 1}
print(frequency_count(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))  # Output: {'apple': 3, 'banana': 2, 'orange': 1}