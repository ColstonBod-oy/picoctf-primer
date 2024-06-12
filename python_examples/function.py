def even_odd(x):
    if (x % 2 == 0):
        return True
    else:
        return False

print("Input a number:")
my_number = int(input())

if even_odd(my_number):
    print("The number is even")
else:
    print("The number is odd")
