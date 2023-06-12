name = "Nihal"
friend = 'Ovaiz'  # strings can be quoted between double or single quotes

print("Hello,", name)

#  We can use triple double or single quote to write a string in multiple lines,
#  because Python look for end of line when quote in double or single quote normally

chat = '''
Nihal: Hello!
Ovaiz: How are you?
Nihal: I am fine. What about you?
Ovaiz: I am great! Let's start with the coding :)'''

print("\nChat between two friends:\n", chat)

# Strings in Python is "like" Array of Characters
print("Printing first character of the name:", name[0])
print("Printing second character of the name:", name[1])

print("\nUsing for loop\n")
for character in name:     # stores letters of name in character and it is printed one by one.
    print(character)