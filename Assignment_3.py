#  ASSIGNMENT-3 DATA TYPES
#
# Q.1- Create a list with user defined inputs.
list_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
print(list_days)

# Second way---if inputs are required from the user
a = []
n1 = int(input("Enter number of elements:"))
for i in range(1, n1+1):
    b = int(input("Enter element:"))
    a.append(b)
    print(a)

# Q.2- Add the following list to above created list:
# [‘google’,’apple’,’facebook’,’microsoft’,’tesla’]

list_company = ['google', 'apple', 'facebook', 'microsoft', 'tesla']
list_days.extend(list_company)

print(list_days)

# Q.3- Count the number of time an object occurs in a list.

my_list = ['google', 'apple', 'facebook', 'microsoft', 'tesla', 'google', 'tesla', 'google', 'tesla', 'facebook']
my_list.count('google')
my_list.count('apple')
my_list.count('facebook')
my_list.count('microsoft')
my_list.count('tesla')

# Q.4- create a list with numbers and sort it in ascending order.

my_number_list = [23, 12, 33, 44, 57, 34, 10]
my_number_list.sort()
my_number_list

# Q.5- Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge
# them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]

A = [34, 4, 67, 89]
A.sort()
B = [5, 55, 76, 12, 3, 4, 89]
B.sort()
C = A+B
C.sort()
print(C)

# Q.6-Implement a stack and queue using lists.
# stack implementation
stack = ["google", "apple", "facebook"]
print(stack)
stack.append("tesla")
print(stack)
stack.append("microsoft")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
# queue implementation
# adding the elements
queue = []
for i in range(0, 5):

    queue.append(i)
    print(queue)


# removing the elements
    while queue:
        j = queue.pop(0)
        print(queue)

