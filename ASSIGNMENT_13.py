# 1.Name and handle the exception occured in the following program:

# ZeroDivisionError: division by zero
try:
    a = 3
    if a < 4:
        a = a/(a-3)
except ZeroDivisionError:
    print("Division by zero is not allowed")

# 2. Name and handle the exception occurred in the following program:

# The error is IndexError: list index out of range
try:
    l = [1,2,3]
    print(l[3])
except IndexError:
    print("Accesing element that doesnot exist")

# 3. What will be the output of the following code:

try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
    raise

# output

# An exception
# Traceback (most recent call last):
#  File "ASSIGNMENT_13.py", line 25, in <module>
#  raise NameError("Hi there")
# NameError: Hi there

# 4. What will be the output of the following code:


def AbyB(a, b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
	    print("a/b result in 0")
    else:
	    print(c)


AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


# output

-5.0
a/b result in 0

# 5. Write a program to show and handle following exceptions:
# 1. Import Error
# 2. Value Error
# 3. Index Error

# import error
import sys
import gw_utility.Book


def main():
    try:
        print(sys.version)
    except ImportError as error:
        # Output expected ImportErrors.
        print(error.__class__.__name__ + ": " + error.message)
    except Exception as exception:
        # Output unexpected Exceptions.
        print(exception, False)
        print(exception.__class__.__name__ + ": " + exception.message)


# value error

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer!")


# index error
try:
    l = [1,2,3]
    print(l[3])
except IndexError:
    print("Accesing element that doesnot exist")


# 6. Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
#  The code must keep taking input till the user enters the appropriate age number(less than 18).

class Error(Exception):
   """Base class for other exceptions"""
   pass

class AgeTooSmallError(Error):
   """Raised when the input age is too small"""
   pass

while True:
    try:
        age = int(input("Please enter the age : "))
        if age < 18:
            raise AgeTooSmallError
        else:
            break
    except AgeTooSmallError:
        print("Not  valid age! Age too be greater than 18 ...")
print("Great, you successfully entered age!")