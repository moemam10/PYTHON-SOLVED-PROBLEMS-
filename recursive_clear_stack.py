
def clear(stack):
    if not stack:
        return
    stack.pop()
    clear(stack)

s = [1, 2, 3, 4, 5]
clear(s)
print(s)
