# 1. What is TimeTuple?

#Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −
                #Index 	Field 	Values
                #0 	4-digit year 	2008
                #1 	Month 	1 to 12
                #2 	Day 	1 to 31
                #3 	Hour 	0 to 23
                #4 	Minute 	0 to 59
                #5 	Second 	0 to 61 (60 or 61 are leap-seconds)
                #6 	Day of Week 	0 to 6 (0 is Monday)
                #7 	Day of year 	1 to 366 (Julian day)
                #8 	Daylight savings 	-1, 0, 1, -1 means library determines DST


# 2. Write a program to get formatted time.

import time

t = time.localtime()

print(time.asctime(t))

# 24 hour format
print(time.strftime("%H:%M:%S"))

# 12 hour format
print(time.strftime("%I:%M:%S"))

# dd/mm/yyyy format
print(time.strftime("%d/%m/%Y"))

# 3. Extract month from the time

import datetime
d = datetime.date.today()
print(d)
print("Month is" + str(d.month))

# 4. Extract day from the time.

import datetime
d = datetime.date.today()
print(d)
print("Day is" + str(d.day))

# 5. Extract date (ex : 11 in 11/01/2021) from the time.

import datetime
now = datetime.datetime.now()
print(now.strftime("%d/%m/%Y"))
print("Current date :")
print(now.strftime("%d"))

# 6. Write a program to print time using localtime method.

import time
t = time.localtime()
print(t)

# 7.Find the factorial of a number input by user using math package functions.
import math
num = int(input("Enter the number whose factorial is to be found"))
print("The factorial is " + str(math.factorial(num)))

# 8. Find the GCD of a number input by user using math package functions.
import math
num1 = int(input("Enter the number whose GCD is to be found"))
num2 = int(input("Enter the number whose GCD is to be found"))
print("The GCD is " + str(math.gcd(num1, num2)))

# 9. Use OS package and do the following tasks:
    # 1. Get current working directory.
    # 2.c

import os

print(os.getcwd())
print(os.environ)