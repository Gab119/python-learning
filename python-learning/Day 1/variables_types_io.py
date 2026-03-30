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