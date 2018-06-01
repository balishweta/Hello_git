
# Q.7 Q.3- Count the number of occurrence of each letter in word "MISSISSIPPI".
#  Store count of every letter with the letter in a dictionary.

word = "MISSISSIPPI"

for i in range(len(word)):
    print("Count of " + word[i]+"is" + str(word.count(word[i])))


my_dict1 = dict()
for i in range(len(word)):
    key = word[i]
    value = str(word.count(word[i]))
    my_dict1[key] = value
print(my_dict1)