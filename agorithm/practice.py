# converting strigs to list

# first converter
# String to List of Strings

string1 = "Benjamin kamena is a progrmammer"

print(string1)
print(type(string1))
print(string1.split())

# second converter
# String to List of Characters

print(string1)
print(type(string1))
print(list(string1))

# third converter
# List of Strings to List of Lists

print(string1)
string2 = string1.split()
list = list(map(list, string2))
print(list)

# fourth converter
# CSV to List

string2 = "Benjamin, kamena, is, a, progrmammer"
print(string2)
print(type(string2))
print(string2.split(','))

# fifth converter
#A string consisting of Integers to List of integers

string3 = "1 2 3 4 5 6 7 8 9"
print(string3)
print(type(string3))
list1 = list(string3.split())
list2 = list(map(int, list1))
print(list2)



