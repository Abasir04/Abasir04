def binary_search(array, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(array) - 1
    if high < low:
        return -1

    midpoint = (low + high) // 2

    if array[midpoint] == target:
        return midpoint
    elif target < array[midpoint]:
        return binary_search(array, target, low, midpoint - 1)
    else:
        return binary_search(array, target, midpoint + 1, high)


s_array = input('Enter your array separated by comma: ').rsplit(',')
search = input('Enter your search: ')

index = binary_search(s_array, search)
result = s_array[index]

if index == -1:
    print("Your search is not in the array")
elif len(set(s_array)) < len(s_array):
    print("Duplicate entries are not allowed")
else:
    print('At index', index, 'you have', result)
