def removeDuplicates(arr):
    return list(set(arr))


array = [1, 2, 3, 3, 4, 5, 5, 6]
print(removeDuplicates(array))  # Output: [1, 2, 3, 4, 5, 6]

print("****Another Method****")


def removeDuplicatesUsingFilter(arr):
    return [item for i, item in enumerate(arr) if arr.index(item) == i]


array1 = [1, 2, 3, 3, 4, 5, 5, 6]
print(removeDuplicatesUsingFilter(array1))  # Output: [1, 2, 3, 4, 5, 6]


def removeDuplicate(arr):
    return [val for i, val in enumerate(arr) if arr.index(val) == i]


array2 = [1, 2, 3, 3, 4, 5, 5, 6, 6, 8, 8, 8]
print(removeDuplicate(array1))

print("****Another Method****")


def getDistinctElements(arr):
    unique = []
    for item in arr:
        if item not in unique:
            unique.append(item)
    return unique


array12 = [1, 2, 3, 3, 4, 5, 5, 6, 6, 8, 8, 8]
print(getDistinctElements(array12))  # Output: [1, 2, 3, 4, 5, 6, 8]

print("****Another Method****")


def eliminateDuplicates(arr):
    uniqueElements = []
    for i in range(len(arr)):
        if arr[i] not in uniqueElements:
            uniqueElements.append(arr[i])
    return uniqueElements


array3 = [1, 2, 3, 3, 4, 5, 5, 6, 6, 8, 8, 8]
print(eliminateDuplicates(array3))  # Output: [1, 2, 3, 4, 5, 6, 8]
print("****Another Method****")


def deduplicate(arr):
    seen = {}
    result = []
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen[arr[i]] = True
            result.append(arr[i])
    return result


array4 = [1, 2, 3, 3, 4, 5, 5, 6, 6, 8, 8, 8]
print(deduplicate(array4))  # Output: [1, 2, 3, 4, 5, 6, 8]
print("****Another Method****")


def uniqueArray(arr):
    uniqueSet = set()
    for item in arr:
        uniqueSet.add(item)
    return list(uniqueSet)


array5 = [1, 2, 3, 3, 4, 5, 5, 6, 6, 8, 8, 8]
print(uniqueArray(array5))  # Output: [1, 2, 3, 4, 5, 6, 8]
print("****Another Method****")


def getUniqueElements(arr):
    uniqueElements = []
    for item in arr:
        if item not in uniqueElements:
            uniqueElements.append(item)
    return uniqueElements


array6 = [1, 2, 3, 3, 4, 5, 5, 6, 6, 8, 8, 8]
print(getUniqueElements(array6))  # Output: [1, 2, 3, 4, 5, 6, 8]
print("****Another Method****")


def filterDuplicates(arr):
    acc = []
    for current in arr:
        if current not in acc:
            acc.append(current)
    return acc


array7 = [1, 2, 3, 3, 4, 5, 5, 6, 6, 8, 8, 8]
print(filterDuplicates(array7))  # Output: [1, 2, 3, 4, 5, 6, 8]
print("****Another Method****")


def distinctElements(arr):
    elementCount = {}
    result = []
    for i in range(len(arr)):
        if arr[i] not in elementCount:
            elementCount[arr[i]] = 1
            result.append(arr[i])
    return result


array8 = [1, 2, 3, 3, 4, 5, 5, 6, 6, 8, 8, 8]
print(distinctElements(array8))  # Output: [1, 2, 3, 4, 5, 6, 8]
print("****Another Method****")


def uniqueItems(arr):
    uniqueMap = {}
    for item in arr:
        if item not in uniqueMap:
            uniqueMap[item] = True
    return list(uniqueMap.keys())


array9 = [1, 2, 3, 3, 4, 5, 5, 6, 6, 8, 8, 8]
print(uniqueItems(array9))  # Output: [1, 2, 3, 4, 5, 6, 8]
print("****Another Method****")


def removeDupes(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


array10 = [1, 2, 3, 3, 4, 5, 5, 6, 6, 8, 8, 8]
print(removeDupes(array10))  # Output: [1, 2, 3, 4, 5, 6, 8]
print("****Another Method****")


def uniqueVals(arr):
    unique = {}
    result = []
    for i in range(len(arr)):
        if arr[i] not in unique:
            unique[arr[i]] = True
            result.append(arr[i])
    return result


array11 = [1, 2, 3, 3, 4, 5, 5, 6, 6, 8, 8, 8]
print(uniqueVals(array11))  # Output: [1, 2, 3, 4, 5, 6, 8]
print("****Another Method****")

