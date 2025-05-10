
def sumsquares(n):
    total = 0
    for i in range(1, n):
        total += i * i
    return total

n = int(input("Enter a number: "))
res = sumsquares(n)
print(res)
