import operator

# Create a dictionary containing all possible operators
operatorList = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# Loop through every possible integer value of a
for a in range(-10000, 10000):
    # b is given = 1
    b = 1
    #Create a list for all outputs of incorrect functions
    results = []
    # Loop through every possible operator in the first line
    for x in operatorList:
        operator1 = operatorList.get(x)
        # Loop through every possible operator in the second line
        for y in operatorList:
            operator2 = operatorList.get(y)
            # Calculate the first and second lines of the function with the chosen operators
            line1 = float(operator1(a, b))
            line2 = float(operator2(line1, 2))
            # Check if the calculation was the intended correct function
            # if true, assign it to a different var, if false, assign it to the incorrect outputs list
            if x == '-' and y == '*':
                expectedAnswer = line2
            else:
                results.append(line2)
        
    # Check if the expected answer appears in the incorrect results list (if true, the test case is invalid)    
    if expectedAnswer not in results:
       pass
    else:
        print(f"A = {a}, B = {b} is invalid")
        print(f"{expectedAnswer} in {results}")
        
                