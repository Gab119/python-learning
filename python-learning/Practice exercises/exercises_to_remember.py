# BINARY SEARCH EXERCISE:                                    

def binary_search(arr, target):
    
    #Given a sorted list, return the index of target using binary search.

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

#How it works:
    # Check middle
    # If target is bigger -> go right
    # If smaller -> go left
    # Repeat until found or exhausted

