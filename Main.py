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
#To make it cleaner use age = int(input("How old are you?: ")) This typescripts the string variable to an integer, making it so the +1 mathematics works.
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

# -------Mad-libs game--------

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
#result = name.find("o") # -------- this will find the amount of the entered character starting from first occurrence of the given characters. will return "-1" if not occurrences are found  --------
#result = name.rfind("o") # -------- this will find the amount of the entered character starting from last occurrence of the given characters will return "-1" if not occurrences are found --------
#name = name.capitalize() # -------- this will capitalize the first letter of the string --------
#name = name.upper() # -------- this will make all the characters uppercase --------
#name = name.lower() # -------- this will make all the characters lowercase --------
#result = name.isdigit() # -------- this will return a true or false if the string contains only digits ( can not include alphabetical characters. has to be only digits.)--------
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

#import time
#from distutils import version

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

# -------- Lists --------

#fruits = ["apple", "orange", "banana", "coconut"] # -------- This is a list --------
# print(dir(fruits)) # -------- use the dir function to show all of the different attributes and methods --------
# print(help(fruits)) # -------- use the help function to show in depth descriptions of all of the methods --------
# print(len(fruits)) # -------- use this to show the length --------
# print("pineapple" in fruits) # -------- use the in operator to find if a value is found within --------

#fruits[0] = "pineapple"
# print(fruits[0])
#for fruit in fruits:
#    print(fruit)
#fruits.append("pineapple") # -------- use the append method to add an element to the end of a list --------
#fruits.remove("apple") # -------- use the remove method to remove an element from a list --------
#fruits.insert(0, "pineapple") # -------- use the insert method to add an element at a given index --------
#fruits.sort() # -------- use the sort method to sort elements alphabetically --------
#fruits.reverse() # -------- use the reverse method to reverse the list based off of the order in which you placed them, not alphabetically --------
#fruits.clear() # -------- use this method to clear a list --------
#print(fruits.index("apple")) # -------- use the index method to show the index value of the element within the list --------
#print(fruits.count("banana")) # -------- use the count method to show how many times the element is shown within the list --------
#print(fruits)

# -------- Sets --------

#fruits = {"apple", "orange", "banana", "coconut"} # -------- This is a set --------
# print(dir(fruits)) # -------- use the dir function to show all the different attributes and methods --------
# print(help(fruits)) # -------- use the help function to show in depth descriptions of all of the methods --------
# print(len(fruits)) # -------- use this to show the length --------
# print("pineapple" in fruits) # -------- use the in operator to find if a value is found within --------
# print(fruits[0]) # -------- not able to use indexing on a set because a set is unordered --------
#fruits.add("pineapple") # -------- use the add function to add an element --------
#fruits.remove("banana") # -------- use the remove function to remove an element --------
#fruits.pop() # -------- use the pop function to remove whichever element is first but it will be random since sets are unordered  --------
#fruits.clear() # -------- use the clear function to clear the set --------
#print(fruits)

# -------- Tuples --------

#fruits = ("apple", "orange", "banana", "coconut", "coconut")
# print(dir(fruits)) # -------- use the dir function to show all the different attributes and methods --------
# print(help(fruits)) # -------- use the help function to show in depth descriptions of all of the methods --------
# print(len(fruits)) # -------- use this to show the length --------

# print(fruits.index("apple")) # -------- use index method to show the place of the element within the tuple --------
# print(fruits.count("apple")) # -------- use count method to show how many times the element is within the tuple --------
#for fruit in fruits:
#    print(fruit)

# -------- Exercise: Shopping cart program. ( lists, sets, tuples) --------

#foods = []
#prices = []
#total = 0

#while True:
#    food = input("Enter a food to buy (q to quit): ")
#    if food.lower() == "q": # -------- use .lower to make it so the user can input both uppercase and lowercase to quit --------
#        break
#    else:
#        price = float(input(f"Enter the price of a {food}: $"))
#        foods.append(food)
#        prices.append(price)

#print("----- YOUR CART -----")

#for food in foods:
    #print(food)
#    print(food, end=" ") # -------- use end to make the list horizontal --------

#for price in prices:
#    total = total + price

#print() # -------- this empty print statement allows spacing/new line to cleanly display the items and then the total below the items --------
#print(f"Your total is: ${total}")

# -------- 2D Lists --------

#fruits = ["apple", "orange", "banana", "coconut"] # -------- This is a 1D list --------
#vegetables = ["celery", "carrots", "potatoes"] # -------- This is a 1D list --------
#meats = ["chicken", "fish", "turkey"] # -------- This is a 1D list --------

# -------- To create a 2D list you must create a new 1D list and place the 1D list elements inside --------

#groceries = [fruits, vegetables, meats] # -------- This is a 2D list --------

#print(groceries) # -------- This will print all of the elements within the lists --------
#print(groceries[0][3]) # -------- This will print specific items. the indexing acts like rows and columns. ie; 0 is fruits, 3 is coconut so it prints "coconut" --------

# -------- 2D lists can also be formatted like this --------
#groceries = [["apple", "orange", "banana", "coconut"],
#             ["celery", "carrots", "potatoes"],
#             ["chicken", "fish", "turkey"]]
#print(groceries[0][0])

# -------- To iterate over the elements of a 2D list you can use nested loops --------

#for collection in groceries:
#    for food in collection:
#        print(food, end=" ")
#    print()

# -------- Exercise: 2D Key pad --------

#num_pad = ((1,2,3),
#           (4,5,6),
#           (7,8,9),
#           ("*",0,"#"))

#for row in num_pad:
#    for num in row:
#        print(num, end=" ")
#    print()

# -------- Python quiz game --------

#questions = ("How many elements are in the periodic table?: ",
#             "Which animal lays the largest eggs?: ",
#             "What is the most abundant gas in Earth's atmosphere?: ",
#             "How many bones are in the human body?: ",
#             "Which planet in the solar system is the hottest?: ")

#options = (("A. 116 ", "B. 117", "C. 118", "D. 119"),
#           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
#           ("A. 206", "B. 207", "C. 208", "D. 209"),
#           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

#answers = ("C", "D", "A", "A", "B")
#guesses = []
#score = 0
#question_num = 0

#for question in questions:
#    print("----------------------")
#    print(question)
#    for option in options [question_num]:
#        print(option)

#    guess = input("Enter (A, B, C, or D): ").upper()
#    guesses.append(guess)
#    if guess == answers[question_num]:
#        score += 1
#        print("Correct!")
#    else:
#        print("Incorrect!")
#        print(f"{answers[question_num]} is the correct answer")
#    question_num += 1

#print("----------------------")
#print("        RESULTS       ")
#print("----------------------")

#print("answers: ", end="")
#for answer in answers:
#    print(answer, end=" ")
#print()

#print("guesses: ", end="")
#for guess in guesses:
#    print(guess, end=" ")
#print()

#score = int(score / len(questions) * 100)
#print(f"Your score is: {score}%")

# -------- Dictionaries --------
# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

#capitals = {"USA": "Washington D.C.",
#            "India": "New Delhi",
#            "China": "Beijing",
#            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))

# -------- Methods: --------

# -------- Get method --------

#print(capitals.get("Japan")) # -------- To get one of the values from the dictionary you would use .get to get the key --------

#if capitals.get("Russia"):
#    print("That capital exists")
#else:
#    print("That capital does not exist")

# -------- Update method --------

#capitals.update({"Germany": "Berlin"}) # -------- using the .update method you can insert a new key value pair or update an existing key value pair --------
#capitals.update({"USA": "Detroit"})

#print(capitals)

# -------- Pop method --------

#capitals.pop("China") # -------- To remove a key value pair you can use .pop --------
#print(capitals)

# -------- Pop item method --------

#capitals.popitem() # -------- To remove the latest key value pair use .popitem --------
#print(capitals)

# -------- Clear method --------

#capitals.clear() # To clear the dictionary completely use .clear --------
#print(capitals)

# -------- Keys method ---------

#keys = capitals.keys() # -------- To get all the keys within the dictionary but not the values use the .keys method --------
#print(keys)

#for key in capitals.keys(): # -------- The keys method can be used in a for loop to iterate over the keys in the dictionary --------
#    print(key)

# -------- Values method ---------

#values = capitals.values()# -------- To get all the values within the dictionary use the .values method --------
#print(values)

#for value in capitals.values():# -------- To iterate and print over every value within your dictionary use a for loop --------
#    print(value)

# -------- Items method --------
# -------- .items returns a dictionary object which resembles a 2D list of tuples
#for key, value in capitals.items(): # -------- This iterates over every key value pair within the dictionary --------
#    print(f"{key}: {value}")

# -------- Dictionary Exercise: Concession stand program --------

#menu = {"pizza": 3.00, # -------- This is your library --------
#        "nachos": 4.50,
#        "popcorn": 6.00,
#        "fries": 2.50,
#        "chips": 1.00,
#        "pretzel": 3.50,
#        "soda": 3.00,
#        "lemonade": 4.25}
#cart = [] # -------- This is a list collection --------
#total = 0

#print("-------- MENU --------")
#for key, value in menu.items():
#    print(f"{key:10}: ${value:.2f}")
#print("----------------------")

#while True:
#    food = input("Select an item (q to quit): ").lower()
#    if food == "q":
#        break
#    elif menu.get(food) is not None:
#        cart.append(food)

#print("----------YOUR ORDER ------------")
#for food in cart:
#    total += menu.get(food)
#    print(food, end=" ")

#print()
#print(f"Total cost: ${total:.2f}")

# -------- Exercise: Number guessing program --------

#import random

#low = 1
#high = 100
#options = ("rock", "paper", "scissors")
#cards = ["2","3","4","5","6","7","8","9","10", "J", "Q", "K", "A"]

#number = random.randint(1,100) # -------- This will choose a random integer from 1-100 --------
#number =random.random() #  -------- This will choose a random floating point number from 0-1 --------
#option = random.choice(options) # -------- This will choose a random option from the list of preset choices --------
#random.shuffle(cards) # -------- This will shuffle the order of the items within the set --------

#print(number)
#print(option)
#print(cards)

# -------- Exercise: Number guessing game --------

#import random

#lowest_num = 1
#highest_num = 100
#answer = random.randint(lowest_num, highest_num)
#guesses = 0
#is_running = True

#print("Python Number Guessing Game")
#print(f"Select a number between {lowest_num} and {highest_num}")

#while is_running:

#    guess = input("Enter your guess: ")

#    if guess.isdigit():
#        guess = int(guess)
#        guesses += 1

#        if guess < lowest_num or guess > highest_num:
#            print(f"That number is out of range")
#            print(f"Please select a number between {lowest_num} and {highest_num}")
#        elif guess < answer:
#            print("Too low! Try again!")
#        elif guess > answer:
#            print("Too high! Try again!")
#        else:
#            print(f"CORRECT! The answer was {answer}")
#            print(f"Number of guesses: {guesses}")
#            is_running = False
#    else:
#        print("Invalid guess")
#        print(f"Please select a number between {lowest_num} and {highest_num}")

# -------- Exercise: Rock, paper, scissors game --------

#import random

#options = ("rock", "paper", "scissors")
#running = True

#while running:

#    player = None
#    computer = random.choice(options)

#    while player not in options:
#        player = input("Enter a choice (rock, paper, scissors): ")

#    print(f"Player: {player}")
#    print(f"Computer: {computer}")

#    if player == computer:
#        print("It's a tie!")
#    elif player == "rock" and computer == "scissors":
#        print("You win!")
#    elif player == "paper" and computer == "rock":
#        print("You win!")
#    elif player == "scissors" and computer == "paper":
#        print("You win!")
#    else:
#        print("You lose!")

#    play_again = input("Play again? (y/n): ").lower()
#    if not play_again == "y":
#        running = False

#    if not input("Play again? (y/n): ").lower() == "y": # -------- You can escape the while loop without using the variable play_again. This just makes for cleaner code with fewer variables --------
#        running = False

#print("Thanks for playing!")

# -------- Exercise: Dice roller program --------

#import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

#"┌---------┐"
#"│         │"
#"│         │"
#"│         │"
#"└---------┘"

#dice_art = {
#    1:("┌---------┐",
#       "│         │",
#       "│    ●    │",
#       "│         │",
#       "└---------┘"),
#    2:("┌---------┐",
#       "│  ●      │",
#       "│         │",
#       "│      ●  │",
#       "└---------┘"),
#    3:("┌---------┐",
#       "│  ●      │",
#       "│    ●    │",
#       "│      ●  │",
#       "└---------┘"),
#    4:("┌---------┐",
#       "│ ●     ● │",
#       "│         │",
#       "│ ●     ● │",
#       "└---------┘"),
#    5:("┌---------┐",
#       "│ ●     ● │",
#       "│    ●    │",
#       "│ ●     ● │",
#       "└---------┘"),
#    6:("┌---------┐",
#       "│ ●     ● │",
#       "│ ●     ● │",
#       "│ ●     ● │",
#       "└---------┘")

#}

#dice = []
#total = 0
#num_of_dice = int(input("How many dice?: "))

#for die in range(num_of_dice):
#    dice.append(random.randint(1,6))

#for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)

#for line in range(5):# -------- This nested loop will make it so the dice art shows horizontally --------
#    for die in dice:
#        print(dice_art.get(die)[line], end="")
#    print()


#for die in dice:
#    total += die
#print(f"total: {total}")

# -------- Functions --------
# function = A block of reusable code
#            place () after the function name to invoke it

#def happy_birthday(): # -------- To define a function use def then type the function name and add parenthesis and a colon --------
#    print("Happy birthday to you!") # -------- Be sure to indent any code that belongs to the function --------
#    print("You are old!") # -------- Be sure to indent any code that belongs to the function --------
#    print("Happy birthday to you!") # -------- Be sure to indent any code that belongs to the function --------
#    print() # -------- Be sure to indent any code that belongs to the function --------

#happy_birthday() # -------- To invoke the function type the function name and add a set of parenthesis. When you invoke the function you will execute the code once --------
#happy_birthday() # -------- If you need to invoke the function more than once, repeat the function.
#happy_birthday() # -------- If you need to invoke the function more than once, repeat the function.

# -------- With functions you are able to send a data directly to a function. using arguments you can send a values or variables directly to a function

#def happy_birthday(name): # -------- Notice how the parameter "name" matches below --------
#    print(f"Happy birthday to {name}!")
#    print("You are old!")
#    print(f"Happy birthday to {name}!")
#    print()

#happy_birthday("Emile") # -------- Place any data within the set of parenthesis. Any data you send a function are known as arguments, but you need a matching set of parameters that are in order --------

# -------- When you invoke a function you can send more than one argument --------

#def happy_birthday(name, age): # -------- The position of the parameters does matter and the parameters must match --------
#    print(f"Happy birthday to {name}!")
#    print(f"You are {age} years old!")
#    print(f"Happy birthday to {name}!")
#    print()

#happy_birthday("Emile", 20) # -------- The position of the arguments does matter --------
#happy_birthday("Steve", 30)
#happy_birthday("Joe", 40)

#def display_invoice(username, amount, due_date):
#    print(f"Hello {username}")
#    print(f"Your bill of ${amount:.2f} is due: {due_date}")

#display_invoice("Emile", 42.50, "01/01")

# -------- Return Statements --------
# return = statement used to end a function
#          and send a result back to the caller

#def add (x, y):
#    z = x + y
#    return z # -------- This will return "3" because x(1) plus y(2) =3. Z is the end result of the function so it will return the result --------

#def subtract (x, y):
#    z = x - y
#    return z # -------- This will return "-1" because x(1) minus y(2) =3. Z is the end result of the function so it will return the result --------

#def multiply (x, y):
#    z = x * y
#    return z # -------- This will return "2" because x(1) times y(2) =3. Z is the end result of the function so it will return the result --------

#def divide (x, y):
#    z = x / y
#    return z # -------- This will return "0.5" because x(1) divided y(2) =3. Z is the end result of the function so it will return the result --------

#print(add(1, 2))
#print(subtract(1, 2))
#print(multiply(1, 2))
#print(divide(1, 2))

#def create_name(first, last):
#    first = first.capitalize()
#    last = last.capitalize()
#    return first + " " + last

#full_name = create_name("emile", "cayer")

#print(full_name)

# -------- Default Arguments --------
# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary # -------- These are the types of arguments. We just used positional previously, now we are going to go over default --------

#def net_price(list_price, discount=0, tax=0.05): # -------- The default is set within the parameter(s) here. The default discount is 0 and the default tax is 0.05
#    return list_price * (1-discount) * (1 + tax)                                 #This function can also accept up to 2 additional arguments --------

#print(net_price(500))
#print(net_price(500, 0.1)) # -------- If you're passing in an argument for the discount the function will use whatever is passed in rather than the default --------
#print(net_price(500, 0.1, 0)) # -------- If you're passing in an argument for the discount and the tax the function will use the passed through argument rather than the default --------

# -------- Exercise: Count Up Timer --------

#import time

#def count(end, start=0): # -------- Non-default arguments should follow default arguments so if you use any default arguments you'll want to be sure that their after any positional arguments  --------
#    for x in range(start,end+1):
#        print(x)
#        time.sleep(1)
#    print("DONE!")

#count(10) # -------- Non-default arguments should follow default arguments so if you use any default arguments you'll want to be sure that their after any positional arguments  --------

#import time

#def count(end, start=0):
#    for x in range(start, end + 1):
#        print(x)
#        time.sleep(1)
#    print("DONE!")


#count(30, 15)

# -------- Keyword Arguments --------
#          helps with readability
#          order of arguments doesn't matter
#          1. positional 2. default 3. KEYWORD 4. arbitrary

#def hello(greeting, title, first, last):
#    print(f"{greeting} {title}{first} {last}")

#hello("Hello", "Mr.","Emile", "Cayer") # -------- This is a positional argument --------

#hello("Hello", last="Cayer", first="Emile", title="Mr.",) # -------- This is a keyword argument. The order does not matter as long as the parameters match --------
                                                                  # -------- If mixing positional and keyword arguments, positional must come before keyword arguments --------

#for x in range(1,11):
#    print(x, end=" ") # -------- "end" is a keyword argument found within the print function --------

#print("1","2","3","4","5", sep="-") # -------- can use the "sep" keyword argument to separate each of the strings with a given character --------

# -------- Exercise: Function to create a phone number --------

#def get_phone(country_code, area, first, last):
#    return f"{country_code}-{area}-{first}-{last}"

#phone_num = get_phone(country_code="1", area="123", first="456", last="7890")
#print(phone_num)

# -------- Arbitrary Arguments ( a varying amount of arguments) --------
# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional 2. default. 3. keyword 4. ARBITRARY

# -------- *args --------

#def add(a, b):
#    return a + b

#print(add(1, 2, 3)) # -------- This will give an error because the add function only takes 2 positional arguments --------

#def add(*args):
#    total = 0
#    for arg in args:
#        total += arg
#    return total

#print(add(1,2,3,4,5))

#def add(*nums): # -------- The name of the operator is not as important as using the unpacking operator (*) so instead of args you can use something like nums --------
#    total = 0
#    for num in nums:
#        total += num
#    return total

#print(add(1,2,3,4,5))

#def display_name(*args):
#    for arg in args:
#        print(arg, end=" ")

#display_name("Mr.", "Emile", "E", "Cayer", "III")

# -------- **kwargs --------

#def print_address(**kwargs):
#    for value in kwargs.values(): # -------- To list the values use the .values method --------
#        print(value)

#print_address(street="1234 Fake St.", city="Detroit", state="MI", zip="54321")

#def print_address(**kwargs):
#    for key in kwargs.keys(): # -------- To list the keys use the .keys method --------
#        print(key)

#print_address(street="1234 Fake St.", city="Detroit", state="MI", zip="54321")

#def print_address(**kwargs):
#    for key, value in kwargs.items(): # -------- To list both the keys and the values use the .items method --------
#        print(f"{key}: {value}")

#print_address(street="1234 Fake St.", city="Detroit", state="MI", zip="54321")

# -------- Exercise: Print a shipping label --------

#def shipping_label(*args, **kwargs): # -------- This function is designed to accept both args and kwargs. However, args needs to come before kwargs --------
#    for arg in args:
#        print(arg, end=" ")
#    print()
#    for value in kwargs.values():
#        print(value, end=" ")

#shipping_label("Mr.", "Emile", "Cayer", "III", # -------- These are arbitrary positional arguments --------
#               street="123 Fake St.", # -------- These are arbitrary keyword arguments --------
#               apt="100",
#               city="Detroit",
#               state="MI",
#               zip_code="54321")

#def shipping_label(*args, **kwargs):
#    for arg in args:
#        print(arg, end=" ")
#    print()

#    print(f"{kwargs.get('street')} {kwargs.get('apt')}") # -------- Use single quotes so that python doesn't get confused on where the f-string ends --------
#    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip_code')}")

#shipping_label("Mr.", "Emile", "Cayer", "III",
#               street="123 Fake St.",
#               apt="#100",
#               city="Detroit",
#               state="MI",
#               zip_code="54321")

#def shipping_label(*args, **kwargs):
#    for arg in args:
#        print(arg, end=" ")
#    print()

#    print(f"{kwargs.get('street')} {kwargs.get('apt')}") # -------- if this has a parameter that doesn't have anything, it will display "None" --------
#    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip_code')}")

#shipping_label("Mr.", "Emile", "Cayer", "III",
#               street="123 Fake St.",
#               city="Detroit",
#               state="MI",
#               zip_code="54321")

#def shipping_label(*args, **kwargs):
#    for arg in args:
#        print(arg, end=" ")
#    print()

#    if "apt" in kwargs:
#        print(f"{kwargs.get('street')} {kwargs.get('apt')}") # -------- You can use an if else statement to make sure "None" does not get printed if there is no apt parameter --------
#    else:
#        print(f"{kwargs.get('street')}")
              
#    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip_code')}")

#shipping_label("Mr.", "Emile", "Cayer", "III",
#               street="123 Fake St.",
#               pobox="PO box #1001"
#               city="Detroit",
#               state="MI",
#               zip_code="54321")

#def shipping_label(*args, **kwargs):
#    for arg in args:
#        print(arg, end=" ")
#    print()

#    if "apt" in kwargs:
#        print(f"{kwargs.get('street')} {kwargs.get('apt)')}")
#    elif "pobox" in kwargs: # -------- You can use an elif statement if a PO box is being used instead of an apt # --------
#        print(f"{kwargs.get('street')}")
#        print(f"{kwargs.get('pobox')}")
#    else:
#        print(f"{kwargs.get('street')}")

#    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

#shipping_label("Mr.", "Emile", "Cayer",
#               street="123 Fake St.",
#               pobox="PO box #1001",
#               city="Detroit",
#               state="MI",
#               zip="54321")

# -------- Iterables --------
# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

#numbers = [1, 2, 3, 4, 5] # -------- This is a list, lists are considered iterable. This can be used in a for loop --------

#for number in numbers:
#    print(number)

#for number in reversed(numbers): # -------- using reversed, this will give you the list of numbers backwards --------
#    print(number)

#for number in numbers:
#    print(number, end=" ") # -------- by using end and then a space, this places the list of numbers on a horizontal output, all on the same line --------

#numbers = (1,2,3,4,5) # -------- This is a tuple, tuples are also iterable --------

#for number in numbers:
#    print(number)

#fruits = {"apple", "orange", "banana", "coconut"} # -------- This is a set, sets are not reversible --------

#for fruit in fruits:
#    print(fruit)

#name = "Emile Cayer" # -------- This is a string --------

#for character in name:
#    print(character, end=" ")

#my_dictionary = {"A": 1, "B": 2, "C": 3} # -------- This is a dictionary --------

#for key in my_dictionary: # -------- This will print the keys from the dictionary --------
#    print(key)

#my_dictionary = {"A": 1, "B": 2, "C": 3}

#for value in my_dictionary.values(): # --------- This will print the values from the dictionary --------
#    print(value)

#my_dictionary = {"A": 1, "B": 2, "C": 3}

#for key, value in my_dictionary.items(): # -------- This will print both the keys and the values from the dictionary --------
#    print(key, value)

#my_dictionary = {"A": 1, "B": 2, "C": 3}

#for key, value in my_dictionary.items():
#    print(f"{key} = {value}") # -------- You can reformat the output however you want. This uses an f-string --------

# -------- Membership Operators --------
# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

#word = "APPLE" # -------- This is a string --------

#letter = input("Guess a letter in the secret word: ")
#if letter in word: # -------- The in membership operator will test to see if a value or a variable (letter) is found within a sequence (word). If it is, it returns true, if not it returns false --------
#    print(f"There is a {letter}")
#else:
#    print(f"{letter} was not found")

#word = "APPLE"

#letter = input("Guess a letter in the secret word: ")
#if letter not in word: # -------- The not in membership operator is the inverse of the in membership operator --------
#    print(f"{letter} was not found")
#else:
#    print(f"There is a {letter}")

#students = {"Emile", "Joe", "Sarah"} # -------- This is a set --------

#student = input("Enter the name of a student: ")

#if student in students:
#    print(f"{student} is a student")
#else:
#    print(f"{student} is not a student")

#students = {"Emile", "Joe", "Sarah"}

#student = input("Enter the name of a student: ")

#if student not in students: # -------- Sets can also be inverse --------
#    print(f"{student} is not a student")
#else:
#    print(f"{student} is a student")

#grades = {"Emile": "A", # -------- This is a dictionary --------
#          "Joe": "B",
#          "Sarah": "C",
#          "Kevin": "D"}

#student = input("Enter the name of a student: ")

#if student in grades:
#    print(f"{student}'s grade is {grades[student]}") # -------- You can pull keys and values using the in membership operator ---------
#else:
#    print(f"{student} was not found")

#email = "myemail@gmail.com" # -------- This is a string --------

#if "@" in email and "." in email: # -------- You can check numerous conditions using the in membership operator--------
#    print("Valid email")
#else:
#    print("Invalid email")

# -------- List Comprehension --------
# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]


#doubles = [] # -------- This is a traditional loop --------
#for x in range(1, 11):
#    doubles.append(x * 2)
#print(doubles)

#doubles = [expression for value in iterable]

#doubles = [x * 2 for x in range(1,11)] # -------- This is a list comprehension. "for every _ (x) in _ (range) do _ (*2)" --------
#print(doubles)

#triples = [y * 3 for y in range(1,11)]
#print(triples)

#squares = [z**2 for z in range(1,11)]
#print(squares)

#fruits = ["apple", "orange", "banana", "coconut"] # -------- This is a string --------
#fruits = [fruit.upper() for fruit in fruits] # -------- Using .upper will make fruits uppercase --------
#print(fruits)

#fruits =[fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]] # -------- The previous code can be formatted like this as well --------
#print(fruits)

#fruits = ["apple", "orange", "banana", "coconut"]
#fruit_chars = [fruit[0] for fruit in fruits] # -------- This will take the first letter (0) of each string and put it into a new list (fruit_chars) --------
#print(fruit_chars)

#numbers = [1, -2, 3, -4, 5, -6, 8, -7]
#positive_nums = [num for num in numbers if num >= 0] # -------- This is a condition. Use the if statement to check a condition --------
#negative_nums = [num for num in numbers if num < 0]
#even_nums = [num for num in numbers if num % 2 == 0]
#odd_nums = [num for num in numbers if num % 2 == 1]
#print(positive_nums)
#print(negative_nums)
#print(even_nums)
#print(odd_nums)

#grades = [85, 42, 79, 90, 56, 61, 30]
#passing_grades = [grade for grade in grades if grade >= 60]

#print(passing_grades)

# -------- Match-Case Statements --------
# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

#def day_of_week(day):
#    if day == 1:
#        return "It is Sunday"
#    elif day == 2:
#        return "It is Monday"
#    elif day == 3:
#        return "It is Tuesday"
#    elif day == 4:
#        return "It is Wednesday"
#    elif day == 5:
#        return "It is Thursday"
#    elif day == 6:
#        return "It is Friday"
#    elif day == 7:
#        return "It is Saturday"
#    else:
#        return "Not a valid day"

#print(day_of_week(1))

# -------- This is a match-case statement. An alternative to using numerous 'elif' statements --------

#def day_of_week(day):
#    match day: # -------- use match and then the corresponding case (day) and then add cases --------
#        case 1: # -------- The cases must be put into the "block" for the match case (indent properly) --------
#            return "It is Sunday"
#        case 2:
#            return "It is Monday"
#        case 3:
#            return "It is Tuesday"
#        case 4:
#            return "It is Wednesday"
#        case 5:
#            return "It is Thursday"
#        case 6:
#            return "It is Friday"
#        case 7:
#            return "It is Saturday"
#        case _: # -------- an _ in a match-case statement is called a wild card. This case functions as the else statement --------
#            return "Not a valid day"

#print(day_of_week(1))

#def is_weekend(day):
#    match day:
#        case "Sunday": # -------- You can use strings as the match for the case --------
#            return True # -------- You can return the function as a boolean (True or False) --------
#        case "Monday":
#            return False
#        case "Tuesday":
#            return False
#        case "Wednesday":
#            return False
#        case "Thursday":
#            return False
#        case "Friday":
#            return False
#        case 'Saturday':
#            return True
#        case _:
#            return False

#print(is_weekend("Saturday"))

#def is_weekend(day):
#    match day:
#        case "Saturday" | "Sunday": # -------- You can use the '|' logical operator. using '|' = or. in this case "Saturday" or (|) "Sunday" --------
#            return True
#        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#            return False
#        case _:
#            return False

#print(is_weekend("Saturday"))

# -------- Modules --------
# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

#print(help("modules")) # -------- Use this to see a list of all of the modules found within the standard Python library --------
#print(help("math"))

#import math # -------- To import a module use import and then the name of the module. You will then have access to everything found within that module including variables and functions --------
#math.pi # -------- Use the module name and then . variable or function name to access the variables and functions of the module --------
#print(math.pi)

#import math as m # -------- Another way you can import a module is by using the 'as' and adding a custom name/an "alias" --------
#print(m.pi)

#from math import pi # -------- You can also use from to import a specific variable/function from the module. However, this can lead to name conflicts --------
#print(pi)

# -------- Creating a module --------

# -------- To create a module follow these steps: --------
# 1. Right click project folder
# 2. Go to "new" -> Python file
# 3. Insert name of file
# 4. Click Python file

#import my_module

#result = my_module.pi
#result = my_module.square(3)
#result = my_module.cube(3)
#result = my_module.circumference(3)
#result = my_module.area(3)

#print(result)

# -------- Variable Scope & Scope Resolution --------
# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
# scope will always go from Local -> Enclosed -> Global -> Built-in

#def func1(): # -------- This is a function --------
#    a = 1 # -------- Variables declared within a function have a local scope --------
#    print(a) # -------- a is the variable. Variable a is local to function 1 --------
#def func2():
#    b = 2
#    print(b) # --------- b is the variable. Variable b is local to function 2 --------

#func1() # -------- This is how to invoke a function --------
#func2() # -------- This is how to invoke a function --------

# -------- Local scope ---------

#def func1():
#    a = 1
#    print(b) # -------- Functions can not see inside other functions. This will return an error because 'b' is not defined inside of function 1 --------
#def func2():
#    b = 2
#    print(a) # -------- Functions can not see inside other functions. This will return an error because 'a' is not defined inside of function 2 --------

#func1()
#func2()

#def func1():
#    x = 1

#    def func2():
#        x = 2 # -------- This is a local version of x. It is local within function 2 ---------
#        print(x) # -------- Within function 2 if you were to print 'x' it would print the local version which is 2 --------
#    func2()

#func1()

# -------- Enclosed scope --------

#def func1():
#    x = 1 # -------- This is an enclosed version of x. It is 'enclosed' within function 1

#    def func2():
#        print(x) # -------- If you were to remove the 'x = 2' from function 2 then the function would then print '1' which would be using the enclosed function instead of local because x is outside of function 2 --------
#    func2()

#func1()

# -------- Glocal scope --------

#def func1():
#    print(x)

#def func2():
#    print(x)

#x = 3 # -------- This is the global version of x. It is outside of being a local or enclosed version (it is outside any functions) --------

#func1()
#func2()

# -------- Built-in scope --------

#from math import e # -------- This is the built-in version of e  --------

#def func1():
#    print(e) # -------- '3' would be printed because the global version comes before the built-in version --------

#e = 3 # -------- This is the global version of e. Variables can share the same name as long as they are in a different scope --------

#func1()

# -------- if_name_ == '_main_' -------- (this is a module)
# if _name_ == _main_: (this script can be imported OR run standalone)
#                      Functions and classes in this module can be reused without the main block of code executing
# Good practice (code is modular, helps readability, leaves no global variables, avoid unintended execution)

#   ex. library = Import library for functionality
#                 When running library directly, display a help page

def main():
    # Your program goes here

if __name__ == "__main__":
    main()

# -------- This is where I delete the main.py script --------
