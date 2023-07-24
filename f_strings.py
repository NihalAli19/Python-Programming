#  used to do string formatting
letter = "Hey, My name is {1} and I am from {0}"
country = "Pakistan"
name = "Nihal"

print(letter.format(name,country))
print(letter.format(country, name))

# to avoid this we can do the numbering inside the curly brackets {}
letter = "Hey, My name is {1} and I am from {0}"
country = "Pakistan"
name = "Nihal"

print(letter.format(country, name))


# THE USAGE OF f-strings
# we can use the name of the variables directly
print(f"Hey, My name is {name} and I am from {country}")

#  using format:
priceText = "For only $ {price:.2f} !"   # takes only 2 decimal places
print(priceText.format(price=49.09999999999999))

# using f-string
price = 1205.6666666666
priceText = f"For only $ {price:.2f} !"
print(priceText)

print("\nGetting a number as a string using f-string:")
print(f"{2*30}")
print(type(f"{2*30}"))

print("To print the f-strings as they are written we need to using double curly brackets such as {{}}")
print(f"Hey, My name is {{name}} and I am from {{country}}")