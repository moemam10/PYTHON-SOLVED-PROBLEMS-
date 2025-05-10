
class Stack:
    def __init__(self):
        self.items = [0]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack is Not Allowed")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack is Not Allowed")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.size())
print(my_stack.is_empty())
