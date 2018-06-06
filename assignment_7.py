# Q.1- Create a function to calculate the area of a sphere by taking radius from user.


def cal_area(r):
    pi = 3.14
    area = pi*r*r
    return area


radius = float(input("Enter the radius"))
print("Area of the circle = %.2f" % cal_area(radius))

# Q.2- Write a function “perfect()” that determines if parameter number is a perfect number.
# Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
# [An integer number is said to be “perfect number” if its factors, including 1(but not the number itself),
#  sum to the number. E.g., 6 is a perfect number because 6=1+2+3].


def perfect(n2):
    sum1 = 0
    for i1 in range(1, n2):
        if n2 % i1 == 0:
            sum1 = sum1 + i1
    if sum1 == n2:
        return True
    else:
        return False


for i in range(1, 1001):
    if perfect(i):
        print(i)


# Q.3- Print multiplication table of 12 using recursion.


def times_tables(n1, t=1):
    if t == 13:
        return
    print(str(n1) + " x " + str(t) + " = " + str(n1*t))
    times_tables(n1, t+1)


times_tables(12)


# Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def power(a, b):
    if b == 1:
        return a
    if b != 1:
        return a*power(a, b-1)


base_new = int(input("Enter base: "))
exp_new = int(input("Enter exponential value: "))
print("Result:", power(base_new, exp_new))

# Q.5- Write a function to find factorial of a number but also store the factorials calculated in a dictionary


def factorial(n1, d1):
    if n1 in d1:
        return d1[n1]
    else:
        p = n1*factorial(n1-1, d1)
        d1[n1] = p
        return p


d = {1: 1}
n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n, d))
print(d)




