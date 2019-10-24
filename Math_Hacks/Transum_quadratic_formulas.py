# Transum Quadratic Formula Solver
# Solves quadratic patterns and generates a rule for them
# Designed for:
# https://www.transum.org/Maths/Activity/Quadratic_Sequences/Default.asp?Level=3
import math
mainLoop = True

print("Quadratic Formula Solver for Transum")
print("Daniel Pavela © 2019")
print("\n-------------------------\n")

while mainLoop is True:
    print("Please input the values for the nth term from 1 to 4")
    inputLoop = True
    while inputLoop is True:
        try:
            firstTerm = float(input("First Term: "))
            secondTerm = float(input("Second Term: "))
            thirdTerm = float(input("Third Term: "))
            fourthTerm = float(input("Fourth Term: "))
            inputLoop = False
        except ValueError:
            print("\nPlease only use digits when inputting the term!\nDecimals are accepted\n")
    # y = a * x**2 + b * x + c
    # finalAnswer = {aValue} * x**2 + {bValue} * x + {cValue}

    # Find the first and second row of differences:
    row11 = secondTerm - firstTerm
    row12 = thirdTerm - secondTerm
    row13 = fourthTerm - thirdTerm
    # ---
    row21 = row12 - row11
    row22 = row13 - row12
    # Calculate the A value
    aValue = row21 / math.factorial(2)

    # Find the C value
    row10 = row11 - row21
    cValue = firstTerm - row10

    # Find the B Value
    # When x = 1,
    xValue = 1
    bValue = 0
    currentAnswer = (aValue * xValue**2) + (bValue * xValue) + cValue
    bValue = firstTerm - currentAnswer
    DisplayBValue = 0
    DisplayCValue = 0

    if cValue > 0:
        DisplayCValue = "+ {cValue}".format(cValue=cValue)
    else:
        DisplayCValue = "- {cValue}".format(cValue=cValue)

    if bValue > 0:
        DisplayBValue = "+ {bValue}".format(bValue=bValue)
    else:
        DisplayBValue = "- {bValue}".format(bValue=bValue)

    print("The quadratic formula for this pattern is:")
    print("y = {aValue}x² {bValue}x {cValue}".format(aValue=aValue, bValue=DisplayBValue, cValue=DisplayCValue))
    print("With A being", aValue)
    print("With B being", bValue)
    print("With C being", cValue)

    input("\nPress enter to calculate again \n")
    print("\n\n\n")
