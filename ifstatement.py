num =int(input("enter number"))
num2=int(input("enter to check odd or even"))
if num>=0:
    print("the number is positive")
else:
    print("the number is negative")
    if num2 % 2 == 0:
        print(f"the {num2} is even")
    else:
        print(f"the {num2} is odd")