def findMissingNumber(arr):
    n = len(arr) + 1  # Since one number is missing
    totalSum = (n * (n + 1)) / 2  # Sum of numbers from 1 to n.
    arraySum = sum(arr)  # sum of elements in the array
    return totalSum - arraySum


print(findMissingNumber([1, 2, 4, 5]))  # Output: 3
