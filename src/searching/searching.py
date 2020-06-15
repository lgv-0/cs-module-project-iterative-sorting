def linear_search(arr, target):
    for z in range(0, len(arr)):
        if arr[z] == target:
            return z

    return -1   # not found

import math
# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    if (len(arr) < 1):
        return -1

    _min = 0
    _max = len(arr) - 1
    
    # Your code here
    if arr[_max] == target:
        return len(arr) - 1
    elif arr[_min] == target:
        return 0
    else:
        while _min != _max:
            _next = math.floor((_min + _max) / 2)

            if arr[_next] == target:
                return _next
            elif arr[_next] < target:
                _min = _next
            else:
                _max = _next

    return -1  # not found