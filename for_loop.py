name = 'Nihal'

for i in name:
    print(i, end=" ")
    if (i == "i"):
        print("Hello this is second letter")

colors = ["Red", "Green", "Blue", "Violet", "Yellow"]
for i in colors:
    print(i)        # prints the whole name of a colour; element of the list
    for nestedColor in i:
        print(nestedColor)      # prints letters of the colour

# range()

for i in range(5):
    print(i)

for i in range(2,5):
    print(i)

# range(start, stop, step)

print("range(start, stop, step)")
for i in range(3, 20, 2):
    print(i)