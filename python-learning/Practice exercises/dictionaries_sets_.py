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