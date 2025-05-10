
def distinct(numbers):
    return len(numbers) == len(set(numbers))

arr = input("Enter numbers: ")
numbers = [int(num) for num in arr.split()]
print(distinct(numbers))
