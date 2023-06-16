age = int(input("Enter your age: "))
print("Your age is:", age)

if (age >= 18):
    print("Eligible to vote!")
else:
    print("You cannot vote!")

# Highest Run Scorer

highest = 101
Your_Score = int(input("Your match score: "))
if (Your_Score > highest):
    highest = Your_Score
    print("The new High Score is:", highest)
else:
    print("High Score is still:", highest)