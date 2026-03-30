# Variables, types, input/output practice d2 (improving efficiency, readability from d1)

def ex_1(): # Ask the user for their name and print a greeting.

    name = input("What is your name?")
    print(f"Hello, {name}!")

def ex_2(): #Ask the user for two numbers and print their sum.

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

def ex_3(): #Ask the user for a number and print whether it is even or odd.

    number = int(input("Provide a number: "))

    if number%2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")

def ex_4(): #Ask for two numbers and an operator (+, -, *, /) and print the result.

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

def ex_5(): #Ask for two variables and swap their values.
    
    no_1 = input("Provide the first number: ")
    no_2 = input("Provide the second number: ")

    no_1, no_2 = no_2, no_1 
    print(f"Swapped numbers: no_1 = {no_1}, no_2 = {no_2}")

def ex_6(): #Ask the user for a word and print its length.

    word = input("Provide a word: ")
    print(len(word))
    print(word[0])
    print(word[-1])

def ex_7(): #Convert temperature from Celsius to Fahrenheit.

    celsius = float(input("What is the temperature in celsius? "))
    f = celsius * 9/5 + 32
    print(f"temperature in fahrenheit is: {f}")

def ex_8(): #I did not cover the leap year, provide me with a leap year example please.

    age = int(input("What is your age? "))
    age_in_days = age * 365
    print(f"You are {age_in_days} days old.")

def ex_9(): #Ask for first name and last name, then generate a username like: john_doe (Bonus: make it lowercase and remove spaces)

    name = input("What is your name?")
    spaceless_name = name.replace(" ","_")
    final_name = spaceless_name.lower()
    print(final_name)

def ex_10(): #Ask the user for any input and print its type:

    placeholder = input("Please provide something: ")
    
    try:
        float(placeholder)
        print("number")
    except:
        print ("string")
   
