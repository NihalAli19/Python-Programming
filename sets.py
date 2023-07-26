# Sets are unordered collection of data items.
# They store multiple items  in a single variable.
# Set items are separated by commas and enclosed within curly brackets{}
# Sets are unchangeable, meaning you can not change items of the set once created.
# Sets do not contain duplicate items.

s = {2, 4, 2, 6}     # do not show repeated values
print(s)

s = {2, 4, 2, 6, 9}  # unordered collection
print(s)

information = {"Nihal", 19, True, 5.66, 786}
print(information)

# cannot be accessed using index numbers

set2 = {}   # it is not an empty set, but it is a dictionary
print(type(set2))

set1 = set()
print(type(set1))

for info in information:
    print(info)
