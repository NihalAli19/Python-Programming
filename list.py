# List help in collecting things in one entity, store multiple thing under one name
# lists are ordered collection of data items
# they store multiple item in a single variable
# list items are separated by commas and enclose within square bracket
# lists are changeable, can be changed after creation
# tuple DONOT change

marks = [3, 5, 6]
print(marks)
print(type(marks))

print((marks[0])) # seems similar to arrays.
print((marks[1])) # seems similar to arrays.
print((marks[2])) # seems similar to arrays.

names = ["Nihal", "Ovaiz", "Preppy", "Brentz", "BuddyTech Services", 786, True]
print(names)

print(names[-3])  # len(name)-3

if "Nihal" in names:
 print("Found!")
else:
 print("No!")

# same data type should be given
if "786" in names:
 print("Found!")
else:
 print("No!")

if "Tech" in "BuddyTech Services":
 print("Found!")
else:
 print("No!")