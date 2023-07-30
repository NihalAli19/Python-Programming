# Dictionaries are ordered collection of data items. They store multiple items in a single variable.
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

# dic = {
#    "Key": "Value"
#    Key: Value
#  }
dic = {
    "Nihal": "Human being",
    "Mouse": "Object"
}

print(dic["Nihal"])

marks = {
    "Basim": 95,
    "Ali": 96,
    "Ovaiz": 99,
    "Zain": 85,
    "John": 100,
}

print(marks["Basim"])
print(marks["Ali"])
print(marks["Zain"])
print(dic)
print(marks)

# print(marks['Ali2'])      -> raises error in the program
# print(marks.get('Ali2'))  -> prints None and executes the rest of the program lines

print("Hello!")

# to access dictionary keys use: dict_name.keys()
print(marks.keys())
# to access dictionary values use: dict_name.values()
print(marks.values())

# to iterate dictionary to get the values of corresponding to the keys
for key in marks.keys():
    print(marks[key])

# Using f-string
for key in marks.keys():
    print(f"The value corresponding to the KEY \"{key}\" is {marks[key]}")

print("\n")

# We can print all the key-value pairs using items() method
print(marks.items())

print("\n")

for key, value in marks.items():
   # instead this: print(f"The value corresponding to the KEY \"{key}\" is {marks[key]}")
   print(f"The value corresponding to the KEY \"{key}\" is {value}")

# dictionary can be used to store:
# marks of students
# performance of employees
# employee IDs with employee names
# items of MRP in a retail/grocery shop

# Helpful in storing things in DATABASE
