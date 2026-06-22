#This is my first Python program
#print("Hello World!")
#print("I like pizza!")
# -------- Variable = A container for a value (string, integer, float, boolean) --------
#            A variable behaves as if it was the value it contains

# -------- Strings (text) --------
#first_name = "Emile"
#food = "Pizza"
#email = "myemail@email.com"

#print(f"Hello {first_name}")
#print(f"You like {food}")
#print(f"Your email is: {email}")

#-------- Integers (whole numbers) --------
#age = 25
#quantity = 3
#num_of_students = 30

#print(f"You are {age} years old.")
#print(f"You are buying {quantity} items")
#print(f"Your class has {num_of_students} students")

# -------- Float (a number that contains a decimal portion) --------

#price = 10.99
#gpa = 3.2
#distance = 5.5

#print(f"The price is ${price}")
#print(f"Your GPA is {gpa}")
#print(f"You ran {distance}Kilometers")

# -------- Boolean (is either true or false) --------

#is_student = True
#for_sale = False
#is_online = True

#if is_student:
 #   print("You are a student")
#else:
 #   print("You are not a student")

#if for_sale:
 #   print("That item is for sale")
#else:
 #   print("That item is not for sale")

#if is_online:
 #   print("You are online")
#else:
 #   print("You are not online")

# -------- Typecasting = the process of converting a variable from one data type to another --------
#              str(), int(), float(), bool()

#name = ("Emile")
#age = 25
#gpa = 3.2
#is_student = True

#gpa = int(gpa)
#age = float(age)

#age +=1

#name = bool(name)

#print(gpa)
#print(age)
#print(name)

# -------- input() = A function that prompts the user to enter data ---------
#          Returns the entered data as a string

#name = input("What is your name?: ")
#To make it cleaner use age = int(input("How old are you?: ")) This typescripts the string variable to an integer, making it so the +1 mathematic works.
#age = input("How old are you?: ")
#age = int(age)
#age = age +1

#print(f"Hello {name}!")
#print("HAPPY BIRTHDAY!")
#print(f"You are {age} years old")

# --------Exercise 1 Rectangle Area Calc --------

#length = float(input("Enter the length: "))
#width = float(input("Enter the width: "))
#area = length * width

#print(f"The area is: {area}cm^")

# -------- Exercise 2 - Shopping Cart Program --------

#item = input("What item would you like to buy?: ")
#price = float(input("What is the price?: "))
#quantity = int(input("How many would you like?: "))
#total = price * quantity

#print(f"You have bought {quantity} {item}s")
#print(f"Your total is ${total}")

# -------Madlibs game--------

#adjective1 = input("Enter an adjective (description): ")
#noun1 = input("Enter a noun (person, place, thing): ")
#adjective2 = input("Enter an adjective (description): ")
#verb1 = input("Enter a verb ending with 'ing'")
#adjective3 = input("Enter an adjective (description): ")
#print(f"Today I went to a {adjective1} zoo.")
#print(f"In an exhibit, I saw a {noun1}")
#print(f"{noun1} was {adjective2} and {verb1}")
#print(f"I was {adjective3}!")

# --------arithmetic operators, math functions, exercises --------

#friends = 5

#friends = friends + 1
#friends +=1 -------- this is an augmented assignment operator --------
#friends = friends -2
#friends -= 2 -------- this is an augmented assignment operator --------
#friends = friends * 3
#friends *= 3 -------- this is an augmented assignment operator --------
#friends = friends /2
#friends /= 2 -------- this is an augmented assignment operator ---------
#friends = friends ** 2
#friends **= 2 -------- this is an augmented assignment operator ---------
#remainder = friends % 3 -------- this is a modulus operator --------

#x = 3.14
#y = 4
#z = 5

#result = round(x) -------- this is the round function --------
#result = abs(y) -------- this is the absolute function --------
#result = pow(y,3) -------- this is the power function --------
#result = max(x,y,z) -------- this is the max function. finds the max number between x,y,z --------
#result = min(x,y,z) -------- this is the min function. finds the min number between x,y,z --------
#print(result)

#print(friends)

# --------- Math Functions --------

#import math -------- as long as this is not commented out you do not need to have this numerous times. ---------

# x = 9.9
#print(math.pi)
#print(math.e)
#result = math.sqrt(x) -------- this finds the square root --------
#result = math.ceil(x) -------- this rounds up --------
#result = math.floor(x) -------- this rounds down --------
#print(result)

# -------- Exercise: Calculate the circumference of a circle --------

#import math
#radius = float(input("Enter radius of a circle: "))

#circumference = 2 * math.pi * radius

#print(f"The circumference of the circle is {round(circumference, 2)}cm")

# -------- Exercise: Calculate the area of a circle --------

#import math

#radius = float(input("Enter the radius of a circle: "))

#area = math.pi * radius ** 2

#print(f"The area of a circle is {round(area, 2)}cm^2")

# -------- Exercise: find the hypotenuse of a right triangle --------

#import math

#a = float(input("Enter side A: "))
#b = float(input("Enter side B: "))

#c = math.sqrt(pow(a, 2) + pow(b, 2))

#print(f"Side C = {c}")

# -------- If Else statements --------
# if = Do some code only IF some condition is True
#      Else do something else
# elif -------- checks else statements from top to bottom. if no else statements matches the condition it goes to else --------
 # make sure to order the elif statements properly

#age = int(input("Enter your age: "))

#if age >= 100:
 #   print("You are too old to sign up!")
#elif age >= 18:
 #   print("You are now signed up!")
#elif age < 0:
 #   print("You haven't been born yet!")
#else:
 #   print("You must be 18+ to sign up")

 # -------- Example 2 ---------

#response = input("Would you like food? (Y/N): ")

#if response == "Y":
 #   print("Have some food!")
#else:
 #   print("No food for you!")

#name = input("Enter your name: ")

#if name == "":
 #   print("You did not type in your name!")
#else:
 #   print(f"Hello {name}!")

# -------- Booleans with If statements --------

#for_sale = True
#online = True

#if for_sale:
 #   print("This item is for sale")
#else:
 #   print("This item is not for sale")

#if online:
 #   print("This user is online")
#else:
 #   print("This user is not online")

# -------- Python calculator --------

#operator = input("Enter an operator (+ - * /): ")
#num1 = float(input("Enter the first number: "))
#num2 = float(input("Enter the second number: "))

#if operator == "+":
   # result = num1 + num2
   # print(round(result, 3))
#elif operator == "-":
 #   result = num1 - num2
 #   print(round(result, 3))
#elif operator == "*":
 #   result = num1 * num2
 #   print(round(result, 3))
#elif operator == "/":
 #   result = num1 / num2
 #   print(round(result, 3))
#else:
 #   print(f"{operator} is not a valid operator")

 # --------Python weight converter --------

#weight = float(input("Enter your weight: "))
#unit = input("Kilograms or pounds? (K or L): ")

#if unit == "K":
 #    weight = weight * 2.205
 #    unit = "Lbs."
 #    print(f"Your weight is {round(weight, 1)} {unit}")

#elif unit == "L":
 #   weight = weight / 2.205
 #   unit ="Kgs."
 #   print(f"Your weight is {round(weight, 1)} {unit}")

#else:
 #   print(f"{unit} was not valid")

# --------- Temperature conversion program exercise --------

#unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
#temp = float(input("Enter the temperature: "))

#if unit == "C":
 #   temp = round((9 * temp) / 5 + 32, 1)
 #   print(f"The temperature in Fahrenheit is: {temp}°F")
#elif unit == "F":
 #   temp = round((temp - 32) * 5 / 9, 1)
 #   print(f"The temperature in Celsius is: {temp}°C")
#else:
 #   print(f"{unit} is an invalid unit of measurement")

# --------- Logical Operators --------
# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

# -------- or --------
#temp = 20
#is_raining = True

#if temp > 35 or temp <0 or is_raining:
#    print("The outdoor event is canceled")
#else:
#    print("The outdoor event is still scheduled")

# -------- and --------

#temp = 20
#is_sunny = False

#if temp >= 28 and is_sunny:
#    print("It is HOT outside 🥵")
#    print("It is SUNNY ☀️")
#elif temp <= 0 and is_sunny:
#    print("It is COLD outside 🥶")
#    print("It is SUNNY ☀️")
#elif 28 > temp > 0 and is_sunny:
#    print("It is WARM outside 😌")
#    print("It is SUNNY ☀️")

# -------- not --------

#temp = 20
#is_sunny = False

#if temp >= 28 and is_sunny:
#    print("It is HOT outside 🥵")
#    print("It is SUNNY ☀️")
#elif temp <= 0 and is_sunny:
#    print("It is COLD outside 🥶")
#    print("It is SUNNY ☀️")
#elif 28 > temp > 0 and is_sunny:
#    print("It is WARM outside 😌")
#    print("It is SUNNY ☀️")
#elif temp >= 28 and not is_sunny:
#    print("It is HOT outside 🥵")
#    print("It is CLOUDY ☁️")
#elif temp <= 0 and not is_sunny:
#    print("It is COLD outside 🥶")
#    print("It is CLOUDY ☁️")
#elif 28 > temp > 0 and not is_sunny:
#    print("It is WARM outside 😌")
#    print("It is CLOUDY ☁️")

# --------Conditional Expressions --------
# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

#num = 5
#a = 6
#b = 7
#age = 25
#temperature = 30
#user_role = "admin"

#print("Positive" if num > 0 else "Negative")
#result = "EVEN" if num % 2 == 0 else "ODD"
#max_num = a if a > b else b
#min_num = a if a < b else b
#status = "Adult" if age >= 18 else "Child"
#weather = "Hot" if temperature > 20 else "Cold"
#access_level = "Full Access" if user_role == "admin" else "Limited Access"

#print(access_level)

# -------- String Methods --------

#name = input("Enter your full name: ")
#phone_number = input("Enter your phone #: ")

#result = len(name) # -------- this (len) will give you the length of a string --------
#result = name.find("o") # -------- this will find the amount of the entered character starting from first occurance of the given characters. will return "-1" if not occurances are found  --------
#result = name.rfind("o") # -------- this will find the amount of the entered character starting from last occurance of the given characters will return "-1" if not occurances are found --------
#name = name.capitalize() # -------- this will capatalize the first letter of the string --------
#name = name.upper() # -------- this will make all the characters uppercase --------
#name = name.lower() # -------- this will make all the characters lowercase --------
#result = name.isdigit() # -------- this will return a true or false if the string contains only digits ( can not include alphabetical characrters. has to be only digits.)--------
#result = name.isalpha() # -------- this will return a true or false if the string contains only alphabetical characters (space is not an alphabetical character)--------
#result = phone_number.count("-") # -------- this will count how many characters are within the string ("-") used in this example for a phone number. --------
#phone_number = phone_number.replace("-", " ") # -------- this will replace one character with another within the string --------

#print(phone_number)

#print(help(str)) # -------- use this to see more string methods --------

# -------- String Methods Exercise 1 --------
#validate user input exercise
#1. username no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

#username = input("Enter a username: ")


#if len(username) > 12:
#    print("Your username can't be more than 12 characters")
#elif not  username.find(" ") == -1:
#    print("Your username can't contain spaces")
#elif not username.isalpha():
#    print("Your username can't contain numbers")
#else:
#    print(f"Welcome {username}")

# -------- String Indexing --------
# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end: step]

#credit_number = "1234-5678-9012-3456"

# print(credit_number[0]) # -------- computers always start with 0 so that why it returns "1" --------
# print(credit_number[0:4]) # -------- this will return all numbers starting from the "0" place and ending in the "4" space. can alternatively have it like this: [:4] --------
#print(credit_number[5:9]) # -------- this will return all numbers starting from the "5" position and ending in the "9" position --------
#print(credit_number[5:]) # --------- this will return all numbers starting from "5" all the way to the end of the string. --------
#print(credit_number[-1]) # -------- This is a negative index. this will print the last number in the string --------
#print(credit_number[::2]) # -------- this will return the character after every 2 steps --------

# --------- Exercise: show last 4 digits of cc number --------

#last_digits = credit_number[-4:]
#print(f"XXXX-XXXX-XXXX-{last_digits}")

# -------- Exercise: Reverse the characters in the string --------

#credit_number = credit_number[::-1]
#print(credit_number)

# -------- Format Specifiers = {value:flags} format a value based on what flags are inserted

#price1 = 3.14159
#price2 = -987.65
#price3 = 12.34
#price4 = 1000000

#print(f"Price 1 is ${price1:.1f}") # -------- this will display the number variable to 1 decimal point as a floating number --------
#print(f"Price 2 is ${price2:.2f}") # -------- this will display the number variable to 2 decimal points as a floating number --------
#print(f"Price 3 is ${price3:.3f}") # -------- this will display the number variable to 3 decimal points as a floating number --------
#print(f"Price 1 is ${price1:10}")  # -------- this will display the number using 10 spaces before --------
#print(f"Price 2 is ${price2:010}") # -------- this is called zero padding. it places "0" in front of the number --------
#print(f"Price 3 is ${price3:<10}") # -------- this will make all numbers left justified --------
#print(f"Price 1 is ${price1:>10}") # -------- this will make all numbers right justified ---------
#print(f"Price 2 is ${price2:^10}") # -------- this will make all numbers center aligned ---------
#print(f"Price 3 is ${price3:+}")   # -------- this will make positive numbers have a + sign --------
#print(f"Price 2 is ${price2:-}")   # -------- this will make negative numbers have a - sign --------
#print(f"Price 4 is ${price4:,}")   # -------- this will make thousandth place numbers have a comma seperator ---------
#print(f"Price 4 is ${price4:+,.2f}") # --------- can combine flags to present how you want --------

# -------- while loop = execute some code WHILE some condition remains true --------

#name = input("Enter your name: ")

#while name == "":
#    print("You did not enter your name")
#    name = input("Enter your name: ")
#print(f"hello {name}")

#age = int(input("Enter your age: "))
#while age < 0:
#    print("Age can't be negative.")
#    age = int(input("Enter your age: "))
#print(f"You are {age} years old")

#food = input("Enter a food you like (q to quit): ")

#while not food == "q":
#    print(f" You like {food}")
#    food = input("Enter another food you like (q to quit): ")

#print("bye")

#num = int(input("Enter a # between 1 - 10:"))
#while num < 1 or num > 10:
#    print(f"{num} is not valid")
#    num = int(input("Enter a # between 1 - 10:"))
#print(f"Your number is {num}")

# -------- Python Compound Interest Calculator --------

#principle = 0
#rate = 0
#time = 0

#while principle <= 0:
#    principle = float(input("Enter the principle amount: "))
#    if principle <= 0:
#        print("Principle can't be less than or equal to zero")
#print(principle)

#while rate <= 0:
#    rate = float(input("Enter the interest rate: "))
#    if rate <= 0:
#        print("Interest rate can't be less than or equal to zero")
#print(rate)

#while time <= 0:
#    time = int(input("Enter the time in years: "))
#    if principle <= 0:
#        print("Time can't be less than or equal to zero")
#print(time)

#print(principle)
#print(rate)
#print(time)

#total = principle * pow((1 + rate / 100), time)
#print(f"Balance after {time} year/s: ${total:.2f}")

#while True:
#    principle = float(input("Enter the principle amount: "))
#    if principle < 0:
#        print("Principle can't be less than zero")
#    else:
#        break # -------- while using True or False, must use else break to break out of the while loop --------

#while True:
#   rate = float(input("Enter the interest rate: "))
#   if rate < 0:
#       print("Interest rate can't be less than zero")
#   else:
#        break # -------- while using True or False, must use else break to break out of the while loop --------

#while True:
#    time = int(input("Enter the time in years: "))
#    if time < 0:
#        print("Time can't be less than or equal to zero")
#    else:
#        break # -------- while using True or False, must use else break to break out of the while loop --------

#total = principle * pow((1 + rate / 100), time)
#print(f"Balance after {time} year/s: ${total:.2f}")

# -------- For Loops --------
# for loops = execute a block of code a fixed number of time
#             You can iterate over a range, string, sequence, etc.

#for x in range(1, 11):
#    print(x)

#print("HAPPY NEW YEAR!")

#for x in reversed(range(1, 11)): # -------- This is the reversed countdown --------
#    print(x)

#print("HAPPY NEW YEAR!")

#for x in range(1, 11, 2): # -------- This will count by 2 --------
#    print(x)

#credit_card = "1234-5678-9012-3456" # --------You can iterate over a string as well! --------

#for x in credit_card:
#    print(x)

#for x in range(1,21):
#    if x == 13:
#        continue # -------- You can use the "continue" keyword to skip over numbers --------
#    else:
#        print(x)

#for x in range(1, 21):
#    if x == 13:
#        break # -------- You can use the "break" keyword to stop at a specific number --------
#    else:
#        print(x)

# -------- Python Countdown Timer Program --------

import time

#my_time = int(input("Enter the time in seconds: "))

#for x in range(0,my_time): # -------- This will make it so it counts from 1 to specified number --------
#    print(x)
#    time.sleep(1)

#print("TIME'S UP!")

#for x in reversed(range(0,my_time)): # -------- This will make it count reverse --------
#    print(x)
#    time.sleep(1)

#print("TIME'S UP!")

#for x in range(my_time,0,-1): # -------- This will make it reverse as well --------
#    print(x)
#    time.sleep(1)

#print("Times UP!")

#for x in range(my_time,0,-1): # -------- This is how to make it display with hours, minutes, and seconds --------
#    seconds = x % 60
#    print(f"00:00:{seconds}")
#    time.sleep(1)

#print("TIMES UP!")

#for x in range(my_time,0,-1):
#    seconds = x % 60
#    print(f"00:00:{seconds:02}") # -------- This will add the 0 padding --------
#    time.sleep(1)

#print("TIME'S UP!")

#for x in range(my_time,0,-1):
#    seconds = x % 60
#    minutes = int(x / 60) % 60
#    print(f"00:{minutes:02}:{seconds:02}") # -------- Adding in minutes --------
#    time.sleep(1)

#print("TIME'S UP!")

#for x in range(my_time,0,-1):
#    seconds = x % 60
#    minutes = int(x / 60) % 60
#    hours = int(x / 3600)
#    print(f"{hours:02}:{minutes:02}:{seconds:02}")
#    time.sleep(1)

#print("TIME'S UP!")

# -------- Nested Loops --------
# A loop within another loop (outer, inner)
#          outer loop:
#              inner loop:

#for x in range(1, 10):
#    print(x, end="") # -------- This will make it so the numbers are side by side, can also add in "-" or " " to format it differently --------

# -------- This is a nested loop -------

#for x in range(3):
#    for y in range(1, 10):
#        print(y, end="")
#    print()

# -------- This is also a nested loop --------

#rows = int(input("Enter the number of rows: "))
#columns = int(input("Enter the number of columns: "))
#symbol = input("Enter a symbol to use: ")

#for x in range(rows):
#    for y in range(columns):
#        print(symbol, end="")
#    print()

# -------- Collections --------
# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

