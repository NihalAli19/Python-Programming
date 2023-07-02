# Four types of arguments:
# 1) Default arguments
# 2) Keyword arguments
# 3) Variable length arguments
# 4) Required arguments

# 1) Default arguments:
def average(a = 9, b = 1):
    print("The average is:", (a+b)/2)

average()       # would use the given values
average(1, 5)   # would ignore the given values
average(5)      # used as a = 5
average(b = 5)

# Another example:
def nameCompletion(fname, mname = "WookiePlays", lname = "Ali"):
    print("Hello, ", fname, mname, lname)

nameCompletion("Nihal")
nameCompletion("Nihal", "Sadruddin")
nameCompletion("Nihal", "Sadruddin", "Ali")

# 2) Keyword arguments:
# can change the order of the arguments

average(b = 9, a = 21)

# 3) Variable length arguments:
def average(*numbers): # tuple/list of numbers
    print(type(numbers))  # takes it as tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum / len(numbers))

# average(5 , 6)
# average(5 , 6, 10)
average(5 , 6, 10, 11)

# 4) Required arguments:
# Arguments are necessary to be given, else the default values will be taken into the function.

def average(a, b = 1):
    print("The average is:", (a+b)/2)

average(a = 21)    #  b is optional, but a needs to be provided
average(a = 21, b = 6)

def name(**name):  #  name as dictionary
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "GOAT", lname = "Ali", fname="Sadruddin")

# Using return statement

def average(a = 9, b = 1):
    # print("The average is:", (a+b)/2)
    return (a+b)/2

avg = average()
print(avg)

# 2 return statements, then first one is considered
def average(a = 9, b = 1):
    # print("The average is:", (a+b)/2)
    return 10
    return (a+b)/2

avg = average()
print(avg)