#Q.1- Take an input year from user and decide whether it is a leap year or not.

# To get year (integer input) from the user
year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))


#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
length=int(input("Enter the length"))
breadth=int(input("Enter the breadth"))
if length == breadth:
    print("Dimensions are of square")
else:
    print("Dimensions are of rectangle")


# Q.3- Take the input age of 3 people and determine oldest and youngest among them.

age_x = int(input("Enter the age of the first person"))
age_y = int(input("Enter the age of the second person"))
age_z = int(input("Enter the age of the third person"))

if age_x > age_y and age_x > age_z:
    print("age_x is the oldest")

elif age_y > age_x and age_y > age_z:
    print("age_y is the oldest")

elif age_z > age_x and age_z > age_y:
    print("age_z is the oldest")

elif age_x < age_y and age_x < age_z:
    print("age_x is younget")

elif age_y < age_x and age_y < age_z:
    print( "age_y is youngest")


elif age_z < age_x and age_z < age_y:
    print("age_z is youngest")

else:
    print( "All are equal")

#Q4 .4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.

# 1. if employee is female, then she will work only in urban areas.
# 2. if employee is a male and age is in between 20 to 40 then he may work in anywhere
# 3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# 4. And any other input of age should print "ERROR".

age = int(input("Enter the age"))

print("Enter SEX either ('M' or 'F')")
sex = input()

print("Enter STATUS  either ('Y' or 'N')")
status = input()
if sex == 'F' or (sex == 'M' and age >= 40 and age <= 60):
    print("will work only in urban areas")
elif sex == 'M' and (age >= 20 and age <= 40):
    print("He will work anywhere")
else:
    print("ERROR")


# Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity Suppose, one unit will cost 100.
# Judge and print total cost for user.

print("Enter quantity")
quantity = int(input())
if quantity * 100 > 1000:
    print("Cost is", ((quantity * 100) - (.1 * quantity * 100)))
else:
    print("Cost is", quantity * 100)


