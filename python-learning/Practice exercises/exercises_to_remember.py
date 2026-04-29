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

# FOR THOSE TWO -> CHECK THE EXPLAINATION IN 29.05.2026 BOTTOM PAGE!

#How it works:
    # Check middle
    # If target is bigger -> go right
    # If smaller -> go left
    # Repeat until found or exhausted

def first_non_repeating_element(my_list):           #Given a list, return the first element that does not repeat (hint: combine sets with counting logic).

    #How to do this without a loop and with counting logic?

    counts = {}
    
    for item in my_list:
        counts[item] = counts.get(item, 0) + 1
    
    for item in my_list:
        if counts[item] == 1:
            return item
    
    return None

'''
O(n) time
Preserves order
Clear logic
'''

def group_unique_characters(my_list):               #Given a list of words, group words that have the same set of characters.

    #How to do this with sets?
    
    #You can use sets as keys (via frozenset).

    groups = {}
    
    for word in my_list:
        key = frozenset(word)  # set of characters
        groups.setdefault(key, []).append(word)
    
    return list(groups.values())

