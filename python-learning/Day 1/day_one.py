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