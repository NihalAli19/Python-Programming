# Emulating do-while loop using break and continue statements
i = int(input("Enter any number: "))

while (i <= 10):
    print("Hello World,", i)
    i = i - 1
    if (i == 0):
        break

i = int(input("Enter any number: "))
# Another way using while (True)
while True:
    print("Hello World,", i)
    i = i - 1
    if (i == 0):
        break