#Lists, Slicing, Loops, Filtering, Searching

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