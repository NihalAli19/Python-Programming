a = "Nihal !!!!!!!! Ovaiz"
print(len(a))
print(a.upper())  # String are immutable and this method makes a new string. It does not changes the string
print(a.lower())  # Similarly, new string is made and returned.
print("Striping \"!\" from string", a.rstrip("!"))
print(a.replace("Nihal", "Ovaiz"))
print(a.split(" "))

heading = "headIng"
print(heading.capitalize())   # Capitalizes first character of the String, but converts the rest of the string to lower case

str = "Welcome to Coderz Den on YouTube!"
print("Length of str without centering it:", len(str))
print(str.center(50))
print("Length of str after centering it:", len(str.center(50)))

print("Counting the number of times \'Nihal\' is used in the String:", a.count("Nihal"))
print(str.endswith("!"))

str = "Welcome to Coderz Den on YouTube!"   # can override a variable in Python Programming
print(str.endswith("to", 4, 10))  # Checking for a value in-between the string by providing start and end index positions.

# find() returns -1 if String is not found for which we are searching for, else prints the index value of the String searched

str = "Hello Guys Let's learn Python5"
print(str.find("is"))

print(str.index("Guys"))  # Checks for exception of "substring not found"

str = "HelloGuysLetslearnPython"
print("Is alpha numeric:", str.isalnum())

str = "HelloGuysLetslearnPython786"
print("Is alpha:", str.isalpha())

print("Is it lower: ", str.islower())
print("Is printable: ", str.isprintable())  # \n is not printable

str = "Hello Guys Lets learn Python 786"
print("Have spaces: ", str.isspace())
str = " "
print("Have spaces: ", str.isspace())

str = "Hello Guys Lets Learn Python786"
print("Is title:", str.istitle())  # return true if the first letter of each word is capitalized

print("Is upper:", str.isupper())

print("Start with: ", str.startswith("Hello"))

print("Swap:", str.swapcase())