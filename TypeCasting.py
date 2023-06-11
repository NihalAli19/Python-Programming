a = "7"
b = "8"
c = "6"

print(a+b+c)  # prints String by concatenating them as python take it as string

print(int(a) + int(b) + int(c))  # type-casts the string into valid integer as there is an integer stored as string

a = "Nihal7"
# print(int(a)) gives error as it is not a valid integer string.

# implicit type-casting

a = 7
b = 8.6
print(a + b)  # prints sum in float to prevent data loss
