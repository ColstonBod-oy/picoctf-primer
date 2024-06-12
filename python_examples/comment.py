print("Input the number of iterations")

# We read user input and assign it to the variable number_iterations
number_iterations = int(input())

# We iterate according to the value input by the user
for i in range(number_iterations):
    if i < 5:
        # We only print this message when the value of i is less than 5
        print("The following number is less than 5")
    else:
        # We only print the value of i is greater than or equal to 5
        print("The following number is greater than or equal to 5")

    # We always print this
    print(i)
