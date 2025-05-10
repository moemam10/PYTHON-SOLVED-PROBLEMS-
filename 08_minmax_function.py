
def minmax(lst):
    smallest = lst[0]
    largest = lst[0]
    for i in lst:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    return (smallest, largest)

arr = input("Enter numbers separated by spaces: ")
numbers = [int(num) for num in arr.split()]
result = minmax(numbers)
print(result)
