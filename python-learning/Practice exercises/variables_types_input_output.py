


# The first day:

#D1 - Variables - Types - Input/Output

def ex_1():

    x = input(f"Please provide your name: ")
    print (f'Hello, {x}')

def ex_2():

    y = int(input(f"Give me the first number to add: "))
    z = int(input(f"Give me the second number to add: "))
    print (y+z)

def ex_3():

    number = int(input(f"Please provide a valid number: "))
    print(number)
    print(type(number))

def ex_4():

    # Principal ammount:
    p = int(input("Please provide the principal ammount: "))
    # Rate:
    r = int(input("Please provide the rate: "))
    # Time:
    t = int(input("Please provide the time: "))

    si = (p*r*t)/100
    print (si)

def ex_5():

    # Note for review: I was not able do do this without using a third variable.

    a = int(input("Provide the first number: "))
    b = int(input("Provide the second number: "))

    print(f'Numbers are: 1st={a}, 2nd={b}')

    c = 0  
    c = a
    a = b
    b = c

    print(f"Reversed numbers are 1st={a}, 2nd={b}")

    # You can do this (interview trick) using tuple unpacking:

def ex_5_rev():

    a = int(input("First number: "))
    b = int(input("Second number: "))
    
    print (f"Before swap: a={a}, b={b}")
    a, b = b, a

    print(f"After swap: a={a}, b={b}")
     
def ex_6():

    c = int(input("Please provide the Celsius temperature so I can convert it to Fahrenheit: "))
    f = (c*9/5)+32

    print(f"The Fahrenheit value is: {f}")

def ex_7():

    # Note for review: I will only count letters not spaces.

    b = input("Give me a string so I can count the letters: ")
    b= b.replace(" ","")
    print(b)
    print(len(b))

def ex_8():

    a = int(input("Please provide a number so I can verify if it is even or odd: "))

    if a%2 == 0:
        print ("Number is even!")
    elif a%2 != 0:
        print ("Number is odd!")

def ex_9():

    ammount = float(input("Please provide the bill amount: "))
    no_of_poeple = int(input("Please provide the number of people: "))
    pay = float(ammount/no_of_poeple)
    print(pay)

def ex_10():

    # I will cover error handling in another day.

    a = input("Please provide an input: ")
    b = int(a)
    c = float(a)
    d = str(a)

    print (f"int {b}, float {c}, string {d}")

    








# Second day one

# Variables, types, input/output practice d2 (improving efficiency, readability from d1)

def ex_1_1(): # Ask the user for their name and print a greeting.

    name = input("What is your name?")
    print(f"Hello, {name}!")

def ex_2_1(): #Ask the user for two numbers and print their sum.

    no_1 = int(input("Provide first number: "))
    no_2 = int(input("Provide second number: "))

    the_sum = no_1 + no_2
    print(the_sum)

    #Please show me here how to make an infinite input question as long as the user does not provide an integer, can I make this without try, exept?

    #while True:
    #    user_input = input("Provide a number: ")
    #    try:
    #        num = int(user_input)
    #        break
    #    except ValueError:
    #        print("Invalid input, try again.")

def ex_3_1(): #Ask the user for a number and print whether it is even or odd.

    number = int(input("Provide a number: "))

    if number%2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")

def ex_4_1(): #Ask for two numbers and an operator (+, -, *, /) and print the result.

    no_1 = int(input("Provide first number: "))
    no_2 = int(input("Provide second number: "))
    operation = input("Provide requested operation (+,-,*,/)")

    if operation == "+":
        the_sum = no_1 + no_2
        print(the_sum)
    elif operation == "-":
        if no_1 >= no_2:
            the_substraction = no_1 - no_2
            print(the_substraction)
        else:
            the_substraction = no_2 - no_1
            print(the_substraction)
    elif operation == "*":
        the_multiplication = no_1 * no_2
        print(the_multiplication)
    elif operation == "/":
        if no_2 == 0:
            print("Number 2 cannot be 0")
            return
        else:
            the_division = no_1 / no_2
            print(the_division)

def ex_5_1(): #Ask for two variables and swap their values.
    
    no_1 = input("Provide the first number: ")
    no_2 = input("Provide the second number: ")

    no_1, no_2 = no_2, no_1 
    print(f"Swapped numbers: no_1 = {no_1}, no_2 = {no_2}")

def ex_6_1(): #Ask the user for a word and print its length.

    word = input("Provide a word: ")
    print(len(word))
    print(word[0])
    print(word[-1])

def ex_7_1(): #Convert temperature from Celsius to Fahrenheit.

    celsius = float(input("What is the temperature in celsius? "))
    f = celsius * 9/5 + 32
    print(f"temperature in fahrenheit is: {f}")

def ex_8_1(): #I did not cover the leap year, provide me with a leap year example please.

    age = int(input("What is your age? "))
    age_in_days = age * 365
    print(f"You are {age_in_days} days old.")

def ex_9_1(): #Ask for first name and last name, then generate a username like: john_doe (Bonus: make it lowercase and remove spaces)

    name = input("What is your name?")
    spaceless_name = name.replace(" ","_")
    final_name = spaceless_name.lower()
    print(final_name)

def ex_10_1(): #Ask the user for any input and print its type:

    placeholder = input("Please provide something: ")
    
    try:
        float(placeholder)
        print("number")
    except:
        print ("string")
   













#Third day one

#Variables, types, i/o

#Variables - 5ex:

def basic_assignment():

    name = "Alex"
    age = 30
    height = 1.76

    #print(f"My name is {name}, I am {age} years old and {height} meters tall.")

    #In interviews, sometimes they care about formatting floats: (Shows attention to detail)
    print(f"My name is {name}, I am {age} years old and {height:.2f} meters tall.")

def swapping_variables():

    a = 5
    b = 10
    print(f"a is {a} and b is {b}")

    a, b = b, a
    # How does this work? -> Python creates a tuple (b, a) and unpacks it into (a, b).
    print(f"a becomes {a} and b becomes {b}")

def type_awareness():

    my_integer = 10
    my_float = 0.15
    my_string = "Example string!"
    my_boolean = False

    print (f"{my_integer} {type(my_integer)}")
    print (f"{my_float} {type(my_float)}")
    print (f"{my_string} {type(my_string)}")
    print (f"{my_boolean} {type(my_boolean)}")

    #Improvement (spacing):
    # print(f"{my_integer} {type(my_integer)}")
    
    #Improvement (clearer output):
    # print(f"Value: {my_integer}, Type: {type(my_integer)}")

def dynamic_typing_trick():

    # Python is dynamically typed, meaning variables don’t have fixed types—only values do.

    x = 10
    print (f"{x} {type(x)}")
    x = "ten"
    print (f"{x} {type(x)}")
    x = [10, "ten", 10.0]
    print (f"{x} {type(x)}")

def variable_naming_and_logic():

    """
    Original code:

    x = 100
    y = 0.2
    z = x * y
    print(z)
    
    """

    product_price = 100                                                     # The price of the product.
    product_discount_percentage = 0.2                                       # The percentage discount for the product.
    discount_amount = product_price * product_discount_percentage           # The discount amount.

    print(f"The discount amount is: {discount_amount}")

    #Improvement:
    #Shorten slightly while keeping clarity -> discount_rate = 0.2
    #Interviewers prefer clear but not overly verbose names.

'''

To improve on this you need to shift from script to reusable logic:

For example for the last exercise:

def calculate_discount(price, discount_rate):
    """
    Calculate the discount amount based on price and discount rate.
    """
    return price * discount_rate


price = 100
discount_rate = 0.2

discount = calculate_discount(price, discount_rate)
print(f"The discount amount is: {discount}")

'''

#Types:

def type_conversion_basics():

    num_str = "25"

    int_str = int(num_str)
    float_str = float(num_str)

    print(f"String: {num_str}, Verification: {type(num_str)}")
    print(f"Integer: {int_str}, Verification: {type(int_str)}")
    print(f"Float: {float_str}, Verification: {type(float_str)}")

    #Type conversion creates a new object — it does not modify the original variable.

def mixing_types():

    #What happens here?

    #a = 10
    #b = "5"
    #result = a + int(b)
    #print(result)

    #My result is a sum of an integer and a conversion of an integer, the program will have to first convert my integer then add it to the other integer to show the result.
    #I may not have understood the asignment. My solution still uses int() but not in the result.

    number_one = 10
    string_number_two = "5"
    number_two = int(string_number_two)

    result = number_one + number_two
    print(result)

    #Solution:

    '''
    a = 10
    b = "5"

    result = str(a) + b
    print(result)
    '''
    #It was expected to make the result a string not an integer.

def truthy_vs_falsy():

    my_int = 0
    my_str = ""
    my_list = []
    random_string = "Hello"

    print(f"Value: {my_int}, Type: {type(my_int)}, Bool value: {bool(my_int)}")
    print(f"Value: {my_str}, Type: {type(my_str)}, Bool value: {bool(my_str)}")
    print(f"Value: {my_list}, Type: {type(my_list)}, Bool value: {bool(my_list)}")
    print(f"Value: {random_string}, Type: {type(random_string)}, Bool value: {bool(random_string)}")

    # So an empty type will return False.
    # In Python, values are considered falsy if they are empty or zero, such as 0, "", [], {}, None. Everything else is truthy.

    #Bonus:

    bool(None) #False

def mutable_vs_immputable():

    first_list = [1, 2, 3]
    second_list = first_list

    second_list.append(4)

    print(first_list)
    print(second_list)

    #Why did both change?
    #I am not sure, I suppose because by saying second_list = first_list they both point now to the same location in memory.

    #Lists are mutable, and variables store references to objects. Assigning b = a makes both variables reference the same list, so modifying one affects the other.

    #So how to fix it?

    # b = a.copy()

def tricky_type_behavior():

    #What will this output?

    x = (1,2,3)
    y = x
    y = y + (4,)

    print(x)
    print(y)

    #Tuples are different from lists as they don't permit the values to be changed (immutable). This means that each of the tuples will point to a different location in memory.
    
    #Refined:
    #Tuples are immutable, so operations like y + (4,) create a new tuple instead of modifying the original. Therefore, y points to a new object, while x remains unchanged.


#Input/Output:

def basic_input():

    user_name = input("What is your name?")

    #Add a space for better UX (this actually gets noticed).
    #user_name = input("What is your name? ")

    print(f"Hello, {user_name}! Welcome back to Python.")

def input_and_type_conversion():         #I will use try/except and some logic to see if I can do it, even if the exercise does not require it.

    while True:
        user_age = input("What is your age?")
        try: 
            user_age = int(user_age)
        except ValueError:
            print("Please provide a valid age!")
            continue

        if user_age in range(0,110):
        # Better range check: if 0 <= user_age <= 110 -> The above one excludes 110.
            break
        else:
            print("Your age should be between 0 and 110!")

    user_age_in_5_years = user_age + 5
    print(f'You will be {user_age_in_5_years} years old in 5 years.')

    # Interview: I validate user input using a loop and exception handling to ensure the program doesn't crash and only accepts valid integers.

def multiple_inputs():

    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    birth_year = int(input("What is your birth year?"))

    age = 2026 - birth_year

    print(f"Hello {first_name} {last_name}, you are approximately {age} years old.")

    #Avoid hardcoding values when they can change (like the current year).
    #from datetime import datetime
    #age = datetime.now().year - birth_year

def simple_calculator():

    number_one = float(input("Provide the first number!"))                  #if you use int() will break floats.
    number_two = float(input("Provide the second number!"))
    operation = input("Provide the operation (+, -, *, /)")

    if operation == "+":
        print(number_one + number_two)
    elif operation == "-":
        print(number_one - number_two)
    elif operation == "*":
        print(number_one * number_two)
    elif operation == "/":
        if number_two == 0:
            print("Second number cannot be 0.")
        else:
            print(number_one / number_two)
    else:
        print("Not a valid operation!")

def input_validation():

    while True:
        number = input("Provide a number!")

        try:
            number = int(number)                                #double conversion if you only do int(number)
            break
        except ValueError:
            print("Please provide a valid number!")
    
    if number % 2 == 0:                                         #then int(number) here again
        print("Number is even.")
    else:
        print("Number is odd.")

simple_calculator()