#if/else

def basic_condition(num):
    
    if num == 0:
        print ("Zero")
    elif num < 0:
        print ("Negative")
    else:
        print ("Positive")

def even_or_odd(num):

    try:
        num = int(num)
    except ValueError:                      # Interview tip: Always catch specific exceptions (ValueError here).
        return "Invalid input"

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
        
def grade_calculator(score):

    if score not in range(0,101):
        print ("Invalid score")
    else:                                   # Nested if/else not necessary, use elif instead.
        if 90 <= score <= 100:
            print ("A")
        elif 80 <= score < 90:
            print ("B")
        elif 70 <= score < 80:
            print ("C")
        elif 60 <= score < 70:
            print ("D")
        else:
            print ("F")

def simple_login_system():

    username = "admin"
    password = "1234"

    username_input = input("Username: ")
    username_password = input("Password: ")

    if username_input == username:
        if username_password == password:
            print("Login successful")
        else:
            print("Wrong password")
    else:
        print("User not found")

'''

def number_comparison_game(num1, num2, num3):

    #I will not use max() because we are practicing if/else statements.

    if num1 == num2 == num3:
        print ("All numbers are equal")
    elif num1 >= num2:
        if num1 == num2:
            print ("A and B are equal")
            if num1 > num3:
                print ("The largest number is A")
            elif num3 >= num2:
                if num3 == num2:
                    print ("B and C are equal")
                    if num3 > num2:
                        print("The largest number is C")
    elif num2 > num3:
            print ("The largest number is B")

'''

def number_comparison_game(num1, num2, num3):
    # Check equality cases first
    if num1 == num2 == num3:
        print ("All numbers are equal")

    result = []

    # Check pair equality
    if num1 == num2 or num1 == num3 or num2 == num3:
        result.append("At least two numbers are equal")

    # Find largest manually
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    result.append(f"The largest number is {largest}")

    print (", ".join(result))

def discount_calculator(price, is_member):

    to_pay = price

    if price < 0:
        return "Invalid price"
    elif price == 0:
        return "Free item"
    elif price >= 100:
        if is_member:
            to_pay -= price * 0.2
            return f"Final price: {to_pay}, 20% discount applied."
        else:
            to_pay -= price * 0.1
            return f"Final price: {to_pay}, 10% discount applied."
    else:
        if is_member:
            to_pay -= price * 0.05
            return f"Final price: {to_pay}, 5% discount applied."
        else:
            return f"Final price: {to_pay}, no discount applied."
        
# interview ready:

def discount_calculator_2(price, is_member):
    if price < 0:
        return "Invalid price"
    if price == 0:
        return "Free item"

    # Determine discount rate
    if price >= 100:
        discount = 0.2 if is_member else 0.1
    else:
        discount = 0.05 if is_member else 0

    # Apply discount
    final_price = round(price * (1 - discount), 2)

    if discount == 0:
        message = "no discount applied"
    else:
        message = f"{int(discount * 100)}% discount applied"

    return f"Final price: {final_price} ({message})"

#for loops

def count_evens(integer_list):

    even_list = []

    for num in integer_list:
        if num%2 == 0:
            even_list.append(num)

    return len(even_list)

'''
def count_evens(integer_list):
    count = 0
    for num in integer_list:
        if num % 2 == 0:
            count += 1
    return count
    
'''

def remove_vowels(my_string):

    vowels = ['a','e','i','o','u','A','E','I','O','U']              #I can do this with '.lower()'
    vowels_removed = ''

    for letter in my_string:
        if letter not in vowels:
            vowels_removed += letter

    print(vowels_removed)

'''
def remove_vowels(my_string):
    vowels = "aeiouAEIOU"
    result = []

    for letter in my_string:
        if letter not in vowels:
            result.append(letter)

    return ''.join(result)

def remove_vowels(my_string):
    vowels = "aeiou"
    result = []

    for letter in my_string:
        if letter.lower() not in vowels:
            result.append(letter)

    return ''.join(result)
''' 

    #Interview tip: Avoid += on strings inside loops—mention immutability if you want bonus points.

def second_largest(integer_list):

    #Don’t use built-in sorting functions.
    #Assume the list has at least 2 distinct numbers.

    largest = 0
    second_largest = 0

    for num in integer_list:
        if num >= largest:
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    
    #Why is this not working?

    return(second_largest)

'''

def second_largest(integer_list):
    largest = float('-inf')
    second_largest = float('-inf')

    for num in integer_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest

'''

def greater_than_avg(numbers):
    
    #Write a function that takes a list of integers and returns how many numbers are greater than the average.

    avg = 0

    #Determine the average:

    for num in numbers:
        avg += num
    
    avg /= len(numbers)

    #How many numbers are higher than average:

    counter = 0

    for num in numbers:
        if num > avg:
            counter += 1

    return(counter)

'''

def greater_than_avg(numbers):
    if not numbers:
        return 0

    total = 0
    for num in numbers:
        total += num

    avg = total / len(numbers)

    count = 0
    for num in numbers:
        if num > avg:
            count += 1

    return count

    Interview tip: Say “This is O(n) time, since I iterate twice, which is still linear.”
'''


def has_duplicates(numbers):

    #Write a function that takes a list and returns True if it contains any duplicates, otherwise False.

    for num in numbers:
        if numbers.count(num) > 1:
            return True
    else:
        return False
    
    #This one has a logic bug, check notes:

'''

def has_duplicates(numbers):
    seen = set()

    for num in numbers:
        if num in seen:
            return True
        seen.add(num)

    return False

    #COMPLEXITY IN NOTES!

'''

def running_sum(numbers):

    #Write a function that takes a list of integers and returns a new list where each element is the running sum up to that index.

    new_sum_list = []
    my_sum = 0

    for num in numbers:
        my_sum += num
        new_sum_list.append(my_sum)

    return(new_sum_list)

# While loops

def count_to_n():

    #Write a program that:
        #Asks the user for a positive integer N
        #Prints numbers from 1 to N using a while loop
    
    while True:
        try:
            n = int(input("Please provide a valid positive integer: "))
            if n <= 0:
                print("Not a positive number!")
            else:
                break   
        except ValueError:
            print("Not a number!")

    counter = 1

    while counter <= n:
        print(counter)
        counter += 1

def sum_of_numbers():

    #Write a program that:
        #Repeatedly asks the user for numbers
        #Stops when the user enters 0
        #Prints the total sum of all entered numbers (excluding the final 0)

    print("This program will give you the sum of all numbers you entered until you enter 0.")

    #For simplicity, I will not do the input validation again since I did it in the previous exercise. I will assume the user provides an integer.

    my_sum = 0
    n = 1

    while n != 0:
        n = int(input("Please provide a number to be added: "))
        my_sum += n
    
    print(my_sum)

#Improved version:

'''

def sum_of_numbers():
    print("Enter numbers. Enter 0 to stop.")

    total = 0

    while True:
        n = int(input("Number: "))
        if n == 0:
            break
        total += n

    print(total)

    Interview note: Using while True + break is often cleaner than sentinel conditions.
'''

def guess_the_number():

    #Write a program that:
        #Has a fixed secret number (e.g., 7)
        #Keeps asking the user to guess the number
        #Stops only when the correct number is guessed
        #Prints how many attempts the user took

    #For simplicity, I will not do the input validation again since I did it in the previous exercise. I will assume the user provides an integer.

    secret_number = 7
    n = 0
    attempts = 0
    
    while n != secret_number:
        n = int(input("Guess the number!"))
        attempts += 1
    
    print(f"Correct! the number was {secret_number}!")
    print(f"Number of attempts: {attempts}")

'''
Improved version:

def guess_the_number():
    secret_number = 7
    attempts = 0

    while True:
        guess = int(input("Guess the number: "))
        attempts += 1

        if guess == secret_number:
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

    print(f"Correct! The number was {secret_number}.")
    print(f"Attempts: {attempts}")

'''

def reverse_a_number():

    #Write a program that:
        #Takes an integer input from the user
        #Reverses the number using a while loop
        #(e.g., 1234 → 4321)

    while True:
        try:
            n = int(input("Please provide a valid integer: "))  
            break
        except ValueError:
            print("Not a number!")
            continue

#Correct solution involving % and //:

'''

def reverse_a_number():
    while True:
        try:
            n = int(input("Please provide a valid integer: "))
            break
        except ValueError:
            print("Not a number!")

    reversed_num = 0
    original = n  # optional, for clarity

    while n != 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10

    print(f"Reversed number: {reversed_num}")

'''

'''
For negative numbers:

def reverse_a_number():
    while True:
        try:
            n = int(input("Please provide a valid integer: "))
            break
        except ValueError:
            print("Not a number!")

    sign = -1 if n < 0 else 1   # preserve the sign
    n = abs(n)                  # work with positive number

    reversed_num = 0

    while n != 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10

    reversed_num *= sign        # restore the sign

    print(f"Reversed number: {reversed_num}")

'''

def input_validation_loop():

    #Write a program that:
        #Keeps asking the user for a number between 1 and 10
        #Only stops when the user provides a valid number
        #Then prints "Valid input!"

    while True:
        try:
            n = int(input("Please provide a number between 1 and 10: "))
            if n not in range(1, 11):
                print("Not a number between 1 and 10!")
            else:
                break   
        except ValueError:
            print("Not a number!")
    
    print("Valid input!")

    #Slight improvement:

'''
def input_validation_loop():
    while True:
        try:
            n = int(input("Please provide a number between 1 and 10: "))
            if 1 <= n <= 10:
                break
            print("Number must be between 1 and 10!")
        except ValueError:
            print("Not a number!")

    print("Valid input!")

Interview note: 1 <= n <= 10 is more Pythonic than range()
'''



# Practice loops:                   Need to practice, list comprehensions and the index issue.

def p1():

    nums = [4,5,2,1]
    objective = 6
    for i in range(len(nums)):
        for j in range (i+1, len(nums)):
            if nums[i] + nums[j] == objective:
                print(nums[i], nums[j])


def p2(): #Print all unique pairs (no repeats, no self-pairing).

    nums = [1,5,7,-1,5]
    target = 6
    results = []                        #or better use a set()

    for i in range(len(nums)):
        for j in range(i+1, (len(nums))):
            if nums[i] + nums[j] == target:
                pair = (nums[i], nums[j])

            #normalize pair (so (5, 1) == (1, 5))
            normalized = tuple(sorted(pair))            #the sorted pair means (1,5 is the same as 5,1) which prevents duplicates.
            if normalized not in results:
                results.append(normalized)

    print(results)

#With set:

def find_pairs():
    nums = [1, 5, 7, -1, 5]
    target = 6
    results = set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = (nums[i], nums[j])
                normalized = tuple(sorted(pair))                    #sorted returns a list, lists cannot go into a set (error unhashable type), tuples can go into a set.
                results.add(normalized)                             #sets require hashable (immutable) elements.

    print(results)