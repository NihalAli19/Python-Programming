# While loop is in Python, but there is no do-while loop in it
i = 0
while (i <= 3):
    print(i)
    i = i + 1

print("Loop ended!")

Userinput = int(input("Enter your age: "))
while (Userinput <= 18):
    print(Userinput)
    Userinput = int(input("Enter your age: "))

NoOfAttendees = int(input("Enter the number of attendees: "))

while (NoOfAttendees >= 5):
    count = NoOfAttendees
    while (count > 0):
        name = input("Enter name:")
        count = count - 1
    NoOfAttendees = NoOfAttendees - 1
else:
    print("I am inside else!")

count = 5
# count = -1
while (count > 0):
    print(count)
    count = count - 1
else:
    print("I am inside else!")