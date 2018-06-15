#  Q.1- Write a Python program to read last n lines of a file


#my_file = open("C:\\Users\\PUNEET\\PycharmProjects\\PROJECT1\\a.txt")
#print(my_file)
#my_file_contents = my_file.read()

#print(my_file_contents)
def lastlines(f, n):
    with open(f) as file:
        print('last ', n, 'lines from file', f)
        for line in (file.readlines()[-n:]):
            print(line, end='')


name = input("enter the filename")
n = int(input('No of  lines to read '))

lastlines(name, n)






# Q.2- Write a Python program to count the frequency of words in a file.


name = input("enter the filename")
file = open(name)
data = file.read()
noofwords = len(data.split())
print("No of words in the file are " + str(noofwords))

# Q.3- Write a Python program to copy the contents of a file to another file.
infile = input("enter the filename")
outfile = input("enter the filename")
with open(infile) as f:
    with open(outfile, "w") as f1:
        for line in f:
            f1.write(line)

# Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.

with open('a.txt') as fh1, open('c.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):

        print(line1+line2)

# Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers
# and then store it to another file.

import random


def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res

num = 10
start = 20
end = 30
p = Rand(start, end, num)
print(p)


afile = open("Random.txt", "w")
for item in p:
        afile.write(str(item))
        afile.write("\n")
afile.close()


with open('Random.txt', 'r') as f:
    lines = f.readlines()
numbers = [int(e.strip()) for e in lines]
numbers.sort()
print(numbers)

afile1 = open("Newfile.txt", "w")
for number in numbers:
    afile1.write(str(number))
    afile1.write("\n")
afile1.close()

