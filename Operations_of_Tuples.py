countries =  ("Pakistan", "Spain", "India", "England", "Scotland")
temp = list(countries) # tuple to list
temp.append("Russia")    # using the list method to manipulate the tuple indirectly
temp.pop(3)  # removes item on the given index
temp[2] = "Canada"
countries = tuple(temp)    # converting the list back into tuple; this is called indirect tuple changing
print(countries)

totalCountries = countries.count("Pakistan")
print("Pakistan occurs:",totalCountries,"times")

index = countries.index("Canada")
print("Canada is at:",index,"index")

# tuple.index(element, start, end)
# occurrences = countries.index("Russia", 2, 4)
# print(occurrences)

length = len(countries)
print("Length of this tuple is:",length)