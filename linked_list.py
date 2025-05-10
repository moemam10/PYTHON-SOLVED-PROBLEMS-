
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def insertFirst(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def InsertAtPos(self, data, pos):
        node = Node(data)
        if pos == 0 or self.head is None:
            self.insertFirst(data)
        else:
            counter = 0
            current = self.head
            while counter != pos - 1:
                current = current.next
                counter += 1
            node.next = current.next
            current.next = node

    def FindBefLas(self):
        if self.head is None:
            print("empty")
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            return current.data

    def connect(self, lst2):
        if self.head is None:
            self.head = lst2.head
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = lst2.head

    def delete(self, data):
        if self.head is None:
            print("empty")
        elif self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                current = current.next
            print("item is not exist")

    def display(self):
        if self.head is None:
            print("IS EMPTY")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next
            print("none")

lst = Linkedlist()
lst.append(10)
lst.append(20)
lst.append(30)
lst.append(40)
lst.delete(10)
lst.display()
