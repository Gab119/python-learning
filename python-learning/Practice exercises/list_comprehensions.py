def ex_1():

    #Create a list of numbers from 0 to 9.

    return [num for num in range(10)]

def ex_2():

    #Create a list of squares from 0 to 9.

    return [num * num for num in range(10)]                 #num**2

def ex_3():

    #Create a list of even numbers from 0 to 20.

    return [num for num in range(21) if num % 2 == 0]

def ex_4():

    #Given words = ["apple", "banana", "cherry"], create a list of their lengths.

    words = ["apple", "banana", "cherry"]
    return [len(word) for word in words]

def ex_5():

    #Given nums = [1, 2, 3, 4, 5], create a list with each number doubled.

    nums = [1, 2, 3, 4, 5]

    return [num*2 for num in nums]


def ex_6():

    #From 0 to 20, create a list of numbers divisible by 3.

    return [num for num in range(21) if num % 3 == 0]

def ex_7():

    #Given names = ["Alice", "Bob", "Charlie", "David"], create a list of names that have more than 3 characters.

    names = ["Alice", "Bob", "Charlie", "David"]

    return [name for name in names if len(name) > 3]

def ex_8():

    #Create a list like ["even", "odd", "even", ...], for numbers 0-9.

    return ["even" if num % 2 == 0 else "odd" for num in range(10)]

def ex_9():

    #Flatten this list: matrix = [[1, 2], [3, 4], [5, 6]]
    
    matrix = [[1, 2], [3, 4], [5, 6]]
    
    flat_list = [x for x in matrix for y in range(2)]

    return flat_list

    #Correct version:

    '''
    
    [x for row in matrix for x in row]

    Mental model:

    for row in matrix:
    for x in row:
        add x
    
    If unsure, expand it:

    flat = []
    for row in matrix:
        for x in row:
            flat.append(x)

    Then compress it back into a comprehension.

    '''

def ex_10():

    #Create all pairs (x, y) where:
        #x is from 0-2
        #y is from 0-2
        #but only include pairs where x!=y

    return [(x,y) for x in range(3) for y in range(3) if x!=y]