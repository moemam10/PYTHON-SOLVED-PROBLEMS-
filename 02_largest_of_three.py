
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"{num1}>{num2}>{num3}")
    else:
        print(f"{num1}>{num3}>{num2}")
elif num2 > num3 and num2 > num1:
    if num1 > num3:
        print(f"{num2}>{num1}>{num3}")
    else:
        print(f"{num2}>{num3}>{num1}")
elif num3 > num2 and num3 > num1:
    if num1 > num2:
        print(f"{num3}>{num1}>{num2}")
    else:
        print(f"{num3}>{num2}>{num1}")
