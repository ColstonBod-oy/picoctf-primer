print("Input the number of iterations:")
number_iterations = int(input())

for i in range(number_iterations):

    if i < 5:
        print("The following number is less than 5")
    else:
        print("The following number is greater than or equal to 5")

    print(i)
