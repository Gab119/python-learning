#Dictionaries

def basic_access():

    #Create a dictionary with 3 key-value pairs (name, age, city). Print each value using its key.

    person = {"name" : "Mark", "age" : 30, "city" : "Dublin"}

    for element in person:
        print(person[element])
    
    '''
    for value in person.values():
    print(value)
    '''

def add_and_update():

    person = {"name": "Alice", "age": 25}

    #Add a new key "city" with value "Paris"
    #Update "age" to 26

    person["city"] = "Paris"
    person["age"] = 26

    for element in person:
        print(person[element])

def loop_through():

    student = {"name": "Bob", "grade": 9, "passed": True}

    for key,value in student.items():
        print(f"{key}: {value}")

def check_key_existance(my_dict, my_key):

    #Write a function that takes a dictionary and a key, and returns True if the key exists, otherwise False.

    if my_key in my_dict.keys():
        return True
    else:
        return False
    
#Too verbose.
#.keys() is unnecessary.
'''
return my_key in my_dict
'''
    
def count_frequency():

    #Given a list, create a dictionary that counts how many times each word appears.

    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    my_dict = {}

    for item in words:
        my_dict[item] = words.count(item)
    
    return my_dict

#Big issue: inefficiency (O(n^2))
#my_dict[item] = words.count(item)
#This recalculates the count every time → bad for large inputs.

'''
my_dict = {}

for word in words:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

or even better:

from collections import Counter
Counter(words)
'''

def find_max_val_key():

    #Return the name of the person with the highest score.

    scores = {"Alice": 85, "Bob": 92, "Charlie": 88}
    counter = 0

    for score in scores.values():
        if score > counter:
            counter = score

    for key, value in scores.items():
        if value == counter:
            return key
        
#This is a very common interview trick.
#Overcomplicated with two loops:
#return max(scores, key=scores.get)

def merge_dictionaries():

    #Merge them into one dictionary. If a key exists in both, sum the values.

    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    my_dict = {}

    for key, value in dict1.items():
        my_dict[key] = value

    for key, value in dict2.items():
        if key in my_dict.keys():                           #if key in my_dict, no need for .keys() here.
            my_dict[key] += value
        else:
            my_dict[key] = value

    return my_dict

'''
Cleaner:

result = dict1.copy()

for key, value in dict2.items():
    result[key] = result.get(key, 0) + value
'''

def invert_dictionary():

    #Invert the dictionary so that values map to lists of keys:

    d = {"a": 1, "b": 2, "c": 1}

    my_list = []
    placeholder = 0
    my_dict = {}

    for value in d.values():
        placeholder = value
        for k,v in d.items():
            if v == placeholder:
                my_list.append(k)
        my_dict[value] = my_list
        my_list = []
    
    return my_dict

#Works but inefficient (nested loops).
#You’re doing O(n^2)

'''
my_dict = {}

for key, value in d.items():
    if value not in my_dict:
        my_dict[value] = []
    my_dict[value].append(key)

cleaner:

my_dict.setdefault(value, []).append(key)
'''

def group_words_by_length():

    #Create a dictionary where:
        #keys = word lengths
        #values = lists of words with that length

    words = ["hi", "hello", "test", "hey", "python", "code",]

    placeholder_length = 0
    placeholder_word = []
    my_dict = {}

    for word in words:
        placeholder_length = len(word)
        for el in words:
            if len(el) == placeholder_length:
                placeholder_word.append(el)
        my_dict[placeholder_length] = placeholder_word
        placeholder_length = 0
        placeholder_word = []

    return my_dict

#Same issue, unnecessary nested loop.
#You recompute groups repeatedly.

'''
my_dict = {}

for word in words:
    length = len(word)
    if length not in my_dict:
        my_dict[length] = []
    my_dict[length].append(word)
'''

def nested_dictionary_access():

    students = {
    "Alice": {"math": 90, "english": 85},
    "Bob": {"math": 78, "english": 82}
    }

    #Write a function that:
        #takes a student name
        #returns their average grade

    sum_of_grades = 0
    no_of_subjects = 0
    mean = 0

    for key, value in students.items():
        for v in value.values():
            no_of_subjects += 1
            sum_of_grades += v
            mean = sum_of_grades // no_of_subjects
        print(f"Student {key}, average grade = {mean}.")
        sum_of_grades = 0
        no_of_subjects = 0

#Does not meet requirements fully.
#Problem:
    #Should take a student name as parameter
    #Should return not print
    #Currently calculates for all students

'''
Correct version:

def get_average(student_name):
    students = {
        "Alice": {"math": 90, "english": 85},
        "Bob": {"math": 78, "english": 82}
    }

    grades = students.get(student_name)

    if not grades:
        return None

    return sum(grades.values()) / len(grades)
'''

#Get comfortable with:
#dict.get()
#dict.setdefault()
#max(dict, key=dict.get)

#setdefault() method will return the value of a dictionary entry for a specified key.
#If the specified key does not exist in the dictionary, it will create an entry for it with the specified value.

#Sets:

def remove_duplicates(int_list):                    #Given a list of integers, return a new list with duplicates removed using a set.

    return list(set(int_list))

#This does not preserve order, which interviewers often care about.
'''
def remove_duplicates(int_list):
    seen = set()
    result = []
    for num in int_list:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
'''

def check_membership(int_list, value):              #Write a function that takes a list and a value, and returns True if the value exists in the list (using a set for efficiency).

    num_list = set(int_list)
    for num in num_list:
        if num == value:
            return True
        else:
            return False
        
#Problem: The loop exits on the first iteration, so it only checks one element.

'''
def check_membership(int_list, value):
    return value in set(int_list)
'''
        
def common_elements(list1, list2):                  #Given two lists, return a set of elements that appear in both.

    x = set(list1)
    y = set(list2)
    my_set = x.intersection(y)
    
    return my_set

#slightly cleaner: return set(list1) & set(list2)

def unique_elements(list1, list2):                  #Given two lists, return elements that appear in either list but not both (symmetric difference).

    x = set(list1)
    y = set(list2)
    my_set = x.symmetric_difference(y)

    return my_set

#cleaner: return set(list1) ^ set(list2)

def count_unique_values(my_list):                   #Write a function that returns the number of unique elements in a list.

    return len(set(my_list))

def is_this_subset(list1, list2):                   #Write a function that checks if one list is a subset of another.

    x = set(list1)
    y = set(list2)

    z = x.issubset(y)
    
    return(z)

#clearner: return set(list1).issubset(set(list2))

def find_missing_numbers(list1, n):                 #Given a list of numbers from 1 to n with some missing, return the missing numbers using sets.

    list2 = range((1, n+1))
    set2 = set(list2)
    set1 = set(list1)

    z = set2.difference(set1)

    return z

#Improvement: Return a sorted list (more practical in interviews)

'''
def find_missing_numbers(list1, n):
    return sorted(set(range(1, n + 1)) - set(list1))
'''

def remove_common_elements(list1, list2):           #Given two lists, remove elements from the first list that also appear in the second.

    x = set(list1)
    y = set(list2)

    x.difference_update(y)
    return x

#Problems:
    # You're modifying a set (fine), but:
        #You lose original order.

'''
def remove_common_elements(list1, list2):
    exclude = set(list2)
    return [x for x in list1 if x not in exclude]
'''    

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
    
'''
Why frozenset?

Normal sets can't be dictionary keys (they're mutable)
frozenset is immutable → valid key
'''