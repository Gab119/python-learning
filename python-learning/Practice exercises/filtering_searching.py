#Filtering, Searching.

#Linear search:

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#Cleaner version:

def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

#Filtering:

def filter_greater_than_five(arr):
    result = []
    for x in arr:
        if x > 5:
            result.append(x)
    return result

#Using list comprehension:
#[x for x in arr if x > 5]

#Out of problems question, why did you use return -1 at the end of the linear search example? Why did you return -1?

#Searching:

def find_target():

    arr = [3, 8, 2 ,10, 5]
    target = 10

    for i, value in enumerate(arr):
        if value == target:
            return i
    
    return -1 # Target not found.

def return_index(arr, num):

    for i, value in enumerate(arr):
        if value == num:
            return i
        
    return -1 # Target not found.
    
def return_index_not_found():

    arr = [5, 3, 8, 6, 2, 7]
    target = 7

    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def search_target(arr, target):

    for i, value in enumerate(arr):
        if value == target:
            return i
        

def count_occurrences(arr, target):

    counter = 0

    for i, value in enumerate(arr):                 #for value in arr:
        if value == target:
            counter += 1

    return counter

#Filtering:

def keep_even_numbers():

    arr = [1, 2, 3, 4, 5, 6]
    even_nums = []

    for num in arr:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums

#return [num for num in arr if num % 2 == 0]

def numbers_higher_than_ten():

    arr = [4, 15, 9, 22, 3]
    higher_than_ten = []

    for num in arr:
        if num > 10:
            higher_than_ten.append(num)

    return higher_than_ten

#return [num for num in arr if num > 10]

def names_starting_with_letter(names_list, letter):

    names_with_letter = []

    for name in names_list:
        if name[0] == letter:
            names_with_letter.append(name)

    return names_with_letter

#What if name == ""? → crash, safer:
#if name and name.startswith(letter):

#Even better, case insensitive:
#if name.lower().startswith(letter.lower()):

def remove_negatives():

    arr = [-3, 5, -1, 8, -2]

    for num in arr:
        if num < 0:
            arr.remove(num)
        
    return arr

#Classic bugm you're modifying the list while iterating over it. This causes elements to be skipped, correct version:

#return [num for num in arr if num >= 0]

def numbers_divisible_by_three():

    arr = [3, 7, 9, 10, 12, 14]
    divisible_by_three = []

    for num in arr:
        if num % 3 == 0:
            divisible_by_three.append(num)

    return divisible_by_three

#return [num for num in arr if num % 3 == 0]

# Slightly harder problems:

def first_occurrence():

    # Return the first index of a target in a list that may contain duplicates.

    arr = [4, 2, 7, 2 ,9 ,2]
    target = 2

    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1  

'''
Interview ready:

def first_occurrence(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1
    
'''

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

def remove_duplicates():
    arr = [1, 2, 2, 3, 1, 4]
    seen = []
    result = []

    for num in arr:
        if num not in seen:
            seen.append(num)
            result.append(num)

    return result

'''
More advanced:

def remove_duplicates(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result
    
'''

def filtering_with_conditions():

    arr = [2, 6, 7, 10, 3, 12]
    filtered_list = []

    for num in arr:
        if num > 5 and num % 2 == 0:
            filtered_list.append(num)

    return filtered_list

#Pythonic version:

#def filtering_with_conditions(arr):
   #return [num for num in arr if num > 5 and num % 2 == 0]

def first_greater_than_ten():

    #Return the index of the first even number greater than 10.

    arr = [3, 7, 11, 14, 9, 20]

    for i, value in enumerate(arr):
        if value > 10 and value % 2 == 0:
            return i   
        
    return -1

