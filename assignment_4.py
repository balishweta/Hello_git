# Q.1- Write a program to create a tuple with different data types and do the following operations.
# 1. Find the length of tuples
tuple1 = (0, 1, 2, 3, "apple", "orange", 2.4, 100)
print(len(tuple1))

# Q.2-Find largest and smallest elements of a tuples.
this_tuple = (4,3,2,32,1,55,6,77)
print('Largest element in the list =' + str(max(this_tuple)))
print('Smallest element in the list =' + str(min(this_tuple)))


# Q.3- Write a program to find the product of all elements of a tuple.

tuple2 = (1, 2, 3, 4)
prod = 1
for x1 in tuple2:
    prod = prod * x1
print(prod)

# Q.4  Create two set using user defined values.
# creating first set
a = set([])
n1 = int(input("Enter number of elements:"))
for i in range(1, n1+1):
    b = int(input("Enter element:"))
    a.add(b)
    print(a)

# creating second set
c = set([])
n1 = int(input("Enter number of elements:"))
for i in range(1, n1+1):
    b = int(input("Enter element:"))
    c.add(b)
    print(c)

# 1. Calculate difference between two sets
    # a and c are two sets
    print(a.difference(c))

# 2. Compare two sets.
    # ordering operators (<, <=, >, >=) comoare two sets to determine their superset or subset relationship
    set1 = set([(1, 1), (2, 1), (1, 2), (6, 6)])
    set2 = set([(2, 1), (1, 2)])
    set1
    set2

    print(set2 < set1)
    print(set2 <= set1)
    print(set1 <= set1)
    print(set1 < set1)

    # 3. Print the result of intersection of two sets
    # a and c are two sets
    print(a.intersection(c))

# Q.5 Create a dictionary to store name and marks of 10 students by user input.
my_dict1 = dict()
for i in range(1, 10+1):
        user_input = input("Enter key and value separated by commas (,): ")
        key, value = user_input.split(",")

        key = key.strip()
        value = value.strip()
        my_dict1[key] = value
print(my_dict1)

# Q.6 Sort the dictionary created in previous question according to marks

#import operator
import operator
sorted_d = sorted(my_dict1.items(), key=operator.itemgetter(0))
print('Original dictionary :',my_dict1)
print('Dictionary in ascending order by value : ',  sorted_d)