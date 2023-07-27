s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

print(s1.union(s2))
print(s1, s2)

s1.update(s2)
print(s1, s2)

print(s1.intersection(s2))

# Symmetric Difference = (A union B) - (A intersection B)
# prints values which are not similar to both the sets.
print(s1.symmetric_difference(s2))

# difference() and difference_update()
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7, 9}
print(s1.difference(s2)) # returns a new set, without the unwanted items
s1.difference_update(s2)
print("Difference: ",s1)  # method removes the items that exist in both sets.

A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}

print('A before (A - B) =', A)

A.difference_update(B)

print('A after (A - B) = ', A)

# Checks if items in a given set is present in the other set. Returns false if items are present else, return True.
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7, 9}
print(s1.isdisjoint(s2))

# Checks if all the items of a particular set are present in the original set. Returns True if all the items are present, else it returns False.
s1 = {1, 2, 5, 6}
s2 = {1, 2, 5, 3, 6, 7, 9}

print(s2.issuperset(s1))
s1.add(45)
print(s1)

# remove or discard an element from the set
s1.remove(45) # gives error if not found and the rest of the lines would not work. Used when you want to throw error.
print(s1)

s1.discard(6)
print(s1)

random = s1.pop()
print(random)

del s1
print("s1 deleted")

# Clears set not deletes
s1 = {1, 2, 5, 6}
s2 = {1, 2, 5, 3, 6, 7, 9}
s1.clear()
print(s1)

if 2 in s2:
    print("Present!")
else:
    print("Absent!")