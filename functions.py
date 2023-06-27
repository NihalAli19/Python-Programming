a = 9
b = 8
c = 5
d = 6

# User-defined functions
def calculateGMEAN(a, b):
    gmean = (a * b) / (a + b)
    print(gmean)

def greaterNumber(a, b):
    if a > b:
        print("->", a, "is greater then", b)
    else:
        print("->", a, "is lesser then", b)

def factorial(a):     # will write body later, so use pass keyword
    pass

calculateGMEAN(a, b)
calculateGMEAN(c, d)
greaterNumber(a, b)
greaterNumber(c, d)