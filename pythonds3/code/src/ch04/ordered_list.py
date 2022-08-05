from src.ch04.node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count = count + 1
            current = current.next

        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next

        return False

    def add(self, item):
        """Add a new node"""
        current = self.head
        previous = None
        temp = Node(item)

        while current is not None and current.data < item:
            previous = current
            current = current.next

        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("{} is not in the list".format(item))

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
