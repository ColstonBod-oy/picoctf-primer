num1 = 8

print("Input the number that will divide:")

try:
    num2 = int(input())
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Do not divide by zero, that is forbidden.")
except ValueError:
    print("Your input value must be an integer.")

print("The program keeps executing to do other stuff...")
