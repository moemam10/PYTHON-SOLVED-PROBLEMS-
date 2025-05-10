
def is_even(k):
    return k % 2 == 0

n = int(input("Enter a number: "))
print("Even" if is_even(n) else "Not Even")
