# 1.  Take 10 integers from user and print it on screen.

for i in range(0, 10):
    num = int(input('Enter a number:'))
    print(num)

# 2.  Write an infinite loop.An infinite loop never ends. Condition is always true.

i = 1
while i >= 1:
    print("hello")
    i = i + 1

# 3. Create a list of integer elements by user input. Make a new list which will store
#  square of elements of previous list.
list1 = []
n = int(input("Enter the number of the elements "))
for i in range(n):
    i = int(input("Enter the element"))
    list1.append(i)
print(list1)

list2 = []
for i in list1:
    list2.append(i**2)
print(list2)

# 4. From a list containing ints, strings and floats, make three lists to store them separately

list1 = [1, 4, 6, "hello", "Bye", 3.0, 5.0, 3]
list_int = []
list_string = []
list_float = []
for x in list1:

    if type(x) is int:
        list_int.append(x)
    elif type(x) is str:
        list_string.append(x)
    else:
        list_float.append(x)
print("List of integers", list_int)
print("List of float", list_float)
print("List of strings", list_string)

# 5. Using range(1,101), make a list containing only prime numbers.


for num in range(1, 101):

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
                print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


# 6. Print the following patterns:
# *
# **
# ***
# ****

x = 1
while x <= 4:
    print("*" * x)
    x = x+1

# 7. Create a user defined dictionary and get keys corresponding to the value using for loop.
n = int(input("Enter the number of the inputs"))
d = {}
for i in range(n):
    text = input().split()
    d[text[0]] = text[1]
print(d)

for t in d:
    print(t, d[t])


# 8. Take inputs from user to make a list.
# Again take one input from user and search it in the list and delete that element,
#  if found. Iterate over list using for loop.

list1 = []
n = int(input("Enter the number of the elements "))
for i in range(n):
    i = int(input("Enter the element"))
    list1.append(i)
print(list1)

search_item = int(input("Enter the number to be searched"))

for i in list1:
    if i == search_item:
        list1.remove(i)
print(list1)


