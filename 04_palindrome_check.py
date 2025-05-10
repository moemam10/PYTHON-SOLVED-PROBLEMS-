
num = int(input("Enter a number: "))
rev = num
n = 0
while num > 0:
    digit = num % 10
    n = n * 10 + digit
    num //= 10
if rev == n:
    print("Yes")
else:
    print("No")
