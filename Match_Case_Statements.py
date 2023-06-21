# Match-Case Statements are similar to the switch-case statements
# Python 3.10 onwards support match-case Statements
# No break statements required, only the case which match will run
# if-else can be used.
x = 5
# x is the variable to match
match x:
    #if x is 0
    case 0:
        print("X is zero!")
        # case with if-condition
    case 5:
        print("X is 5")
        # Empty case with if-condition
    case _ if x != 90:
        print("X is not 90")
    case _ if x != 80:
        print("X is not 80")
    case _ if x != 70:
        print("X is not 70")

        # default case will only be match if the above case were not matched
        # ,so it is basically just an else:
