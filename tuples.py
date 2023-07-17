#  Tuples are odered collection of data items. They store multiples items in a single variable. Tuples are unchangeable meaning we can not alter them after creation.

tup = (7, 8, 6)
#  tup[0] = 90  , tuples can not be changed
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])
print("Length: ",len(tup))
print(tup[-1])

if 8 in tup:
    print("Found!")
else:
    print("Sorry, not found!")

# tuple slicing

tup2 = tup[1:4]  # new tuple is created!
print(tup2)
print(tup2[0:])
print(tup2[:2])

#  string and tuples are immutable
#  lists are mutable