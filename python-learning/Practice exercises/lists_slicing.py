#Lists:

def basic_filtering():                  #Given a list of integers, return a new list containing only the even numbers.

    nums = [3, 7, 10, 4, 9, 12, 15]
    even_nums = []

    for element in nums:
        if element % 2 == 0:
            even_nums.append(element)

    return even_nums

""" More pythonic version:

def basic_filtering():
    nums = [3, 7, 10, 4, 9, 12, 15]
    return [x for x in nums if x % 2 == 0]
    
"""

def remove_duplicates():                #Given a list, return a new list with duplicates removed while preserving the original order.

    items = [1, 2, 2, 3, 4 ,1 ,5]
    unique_numbers = []

    for element in items:
        if element not in unique_numbers:
            unique_numbers.append(element)

    return(unique_numbers)

#O(n2) because of element not in unique_numbers
"""Interview friendly version:

def remove_duplicates():
    items = [1, 2, 2, 3, 4, 1, 5]
    seen = set()
    result = []

    for x in items:
        if x not in seen:
            seen.add(x)
            result.append(x)

    return result

set lookup is O(1)
Total becomes O(n)
"""

def second_largest_number():            #Given a list of integers, return the second largest number. Do not use sort() directly (interviewers often restrict this). Handle duplicates properly

    nums = [10, 20, 4, 45, 99, 99]
    uniques_list = []
    objective_number = 0

    for element in nums:
        if element not in uniques_list:
            uniques_list.append(element)

    uniques_list.pop()

    objective_number = uniques_list.pop()

    return(objective_number)

'''
Issues:

uniques_list.pop()
objective_number = uniques_list.pop()

Problems:

You assume the largest numbers are at the end → not guaranteed
You never sort or track max properly
This breaks for many inputs

Correct approach (no sorting):

def second_largest_number():
    nums = [10, 20, 4, 45, 99, 99]

    first = second = float('-inf')                          #sets a value to something resembling infinite (lowest infinite in this case)

    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second

    Interview explaination: “I track the largest and second largest in one pass.
    When I find a new max, I shift the old max to second.”
    
'''

def rotate_list():                      #Rotate a list to the right by k steps. (right rotation). Without using lists, this was too advanced for me at the moment.

    nums = [1, 2, 3, 4, 5]
    k = 2
    list_one = []
    list_two = []

    list_one = nums[0:k+1]
    list_two = nums[k+1:]

    list_two.extend(list_one)

    return(list_two)

    #To handle the case where k > len(nums) I can do a check with try, except block in which is k is larger than len(nums) I can show an error but I don't think this is what is requested of me.
    #I don't know how to do it in place, this was too advanced for me.

'''
close conceptually, but:

list_one = nums[0:k+1]

This is not correct for right rotation
You're slicing incorrectly

correct solution:

def rotate_list():
    nums = [1, 2, 3, 4, 5]
    k = 2

    k = k % len(nums)  # handles k > len(nums)

    return nums[-k:] + nums[:-k]


In-place version (advanced, interview gold)

def rotate_list_in_place():
    nums = [1, 2, 3, 4, 5]
    k = 2

    k %= len(nums)

    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

    return nums

'''

def longest_increasing_subsequence():   #Given a list of integers, find the length of the longest strictly increasing subsequence (not necessarily contiguous).

    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    #I am bad at optimization, I will try the simple approach first.

    longest_subsequence = []
    counter = 0

    for i in range(len(nums)):
        longest_subsequence.append(i)

        for j in (i+1, len(nums)):
            if j > i:
                longest_subsequence.append(j)
                counter += 1

    #I got lost here, I don't know how to memorize the largest length and show the longest subsequence.


'''

# Hard interview problem: Simple O(n2) solution for my level: check notes for explaination:

def longest_increasing_subsequence():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    dp = [1] * len(nums)                                    #In Python, this line creates a list named dp that is the same length as an existing list called nums, where every element is initialized to the integer 1

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

'''

#Slicing:

#No need for () around return!!!!!

def basic_slicing():

    # Given a list of integers, return a new list containing only the first 3 elements.

    nums = [10, 20, 30, 40, 50]
    return(nums[:3])

def skip_elements():

    # Return every second element from the list (starting from index 0).

    nums = [1, 2, 3, 4, 5, 6]

    return(nums[::2])

def reverse_with_slicing():

    # Return the list reversed, using slicing only (no .reverse() or loops). 

    nums = [1,2,3,4]
    reversed_nums = nums[::-1]

    return(reversed_nums)

    #unnecessary variable: return directly nums[::-1]

def middle_slice():

    # Given a list, return the middle part, excluding the first and last elements.
    # Edge case to think about: what if the list has fewer than 3 elements?

    nums = [5, 10, 15, 20, 25]
    if len(nums) < 3:
        return(nums)
    else:
        return(nums[1:-1])

def rotate_list(k):

    # Rotate a list to the right by 2 positions using slicing.
    # Bonus: make it work for any k (not just 2), including when k > len(nums).

    nums = [1, 2, 3, 4, 5]
    k = k % len(nums)

    #nums.reverse()
    #nums[k:] = reversed(nums[k:])
    #nums[:k] = reversed(nums[:k])

    return nums[-k:] + nums [:-k]

    #missed edge case:
    #len(nums) == 0
    
    '''
    def rotate_list(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    return nums[-k:] + nums[:-k]
    '''

#solution (check notes):

def remove_centered_chunk(nums, n):
    if n >= len(nums):
        return []
    
    start = (len(nums) - n) // 2
    return nums[:start] + nums[start + n:]







#First day:


def ex_1():

    nums = [1, 2, 3, 4, 5, 6, 7]
    first_3 = nums[0:3]
    last_3 = nums[-3::]
    reversed_nums = nums[::-1]

    print(first_3)
    print(last_3)
    print(reversed_nums)

def ex_2(numbers):
    
    even_list = []

    for num in numbers:
        if num%2 == 0:
            even_list.append(num)
        else:
            continue
    
    print(even_list)

def ex_3():

    nums = [1,2,3,4,5]
    my_sum = 0
    for num in nums:
        my_sum += num
    
    print(my_sum)

def ex_4():

    nums = [1,2,3,2,346,123,4,6,22351,24,6,2,4,9,19345,92,91,19,0]
    max_number = 0

    for num in nums:
        if num > max_number:
            max_number = num
        else:
            continue

    print(max_number)

def ex_5():

    nums = [1,2,2,3,4,4,5]
                                    #since the result has to be an ordered list, I will not use set
                                    #result = set(nums)
                                    #print(list(result))
    
    result_list = []
    for num in nums:
        if num in result_list:
            continue
        else:
            result_list.append(num)
    
    print(result_list)

def ex_6():             #I can ask for the parameters inside the () of the functions, but for simplicity I will make a list and a value variable inside the function.

    nums = [2,3,4,32,3,4,6,2,3,2,9,2,2,6]
    value = 2
    counter = 0
    
    for num in nums:
        if num == value:
            counter += 1
        else:
            continue
    
    print(counter)

def ex_7():

    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    new_list = []

    for num in nums:
        if num > 10 and num % 3 == 0:
            new_list.append(num)
        else:
            continue
    
    print(new_list)

def ex_8():

    nums = [4,5,1,2,0,4,1,0]
    counter = 0
    first_repeat = []

    for num in nums:
        counter = nums.count(num)
        if counter == 1:
            first_repeat = num
            break
        else:
            continue
    
    print(first_repeat)

# ex 9 and 10 I will do tomorrow, I found difficulty in understanding how ex 9 is done, I will practice ex9.