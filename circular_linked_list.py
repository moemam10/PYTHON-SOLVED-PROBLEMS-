
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node
            node.next = self.head

    def display(self):
        if self.head is None:
            print("IS EMPTY")
        else:
            current = self.head
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current == self.head:
                    break
            print("Head")

lst = CircularLinkedlist()
lst.append(10)
lst.append(20)
lst.append(30)
lst.append(40)
lst.display()
