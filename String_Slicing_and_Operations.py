names = "Ovaiz,Nihal"
print("Length of String names:", len(names))
print(names[0:5])

fruit = "Mango"
print("Fruit is", fruit, "which has", len(fruit), "letters")
print(fruit[0:4])
print(fruit[:4])  # automatically adds 0 there.
print(fruit[1:4])

# makes it equal to length [len(fruit)]
print(fruit[:])
# or
print(fruit[:5])

print(fruit[0:len(fruit)-3])

print(fruit[-1:len(fruit)-3])  # Nothing is printed
# Python compiler reads it as, 4:2

print(fruit[-3:-1])
# 2:4

# Quick Quiz
nm = "Preppy"
print(nm[-4:-2])
# 3:5   Successful Quiz :)