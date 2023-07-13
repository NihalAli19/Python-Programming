l = [1, 3, 9, 6]
print(l)
l.append(7)
print("Append:",l)

l.sort()
print("Sort:",l)

l.sort(reverse=True)
print("Reverse sort:",l)

l.reverse()
print("Reverse:",l)

# this methods returns the i ndex of the first occurrence ofo the list item.
print("Index:",l.index(3))

print("Count:",l.count(2))

m = l
m[0] = 0    # changes l elements as well as m is also a reference of l
print(l)

l = [1, 3, 9, 6]
# therefore, use copy method to avoid it
m = l.copy()
print("Copy list:",m)

l.insert(1,899)
print("Insert:",l)

m =  [900, 1000, 1100]
l.extend(m)
print("Extended List:",l)

# making new list using the two lists without changing the original lists
l = [1, 3, 9, 6]
k = l + m
print(k)