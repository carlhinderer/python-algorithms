from .single_node import SingleNode

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        node = SingleNode(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        previous = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                self.count -= 1
                return
            previous = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False

    def clear(self):
        self.tail = None
        self.head = None
        self.count = 0