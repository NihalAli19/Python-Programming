print("** Calculator **")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print("You can perform the following operations using this calculator:\n")

print("1) Addition\n2) Subtraction\n3) Division\n4) Multiplication\n5) Modulus\n6) Exponential\n7) Floor Division")
choice = int(input("Which operation do you want to perform: "))

if choice == 1:
    print("Answer:", (a + b))
elif choice == 2:
    print("Answer:", (a - b))
elif choice == 3:
    print("Answer:", (a / b))
elif choice == 4:
    print("Answer:", (a * b))
elif choice == 5:
    print("Answer:", (a % b))
elif choice == 6:
    print("Answer:", (a ** b))
elif choice == 7:
    print("Answer:", (a // b))
else:
    print("Incorrect choice!")
