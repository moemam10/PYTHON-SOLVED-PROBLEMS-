
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value

    def display(self):
        current = self.top
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack contents:")
stack.display()
print("Top element:", stack.peek())
print("Popped:", stack.pop())
print("Stack after pop:")
stack.display()
