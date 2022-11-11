class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def add_at_beginning(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node


    def append_at_location(self, data, index):
        if index > self.size:
            raise 'Index is greater than list size.'

        node = Node(data)
        pos = 0

        current = self.head

        while pos < index:
            current = current.next
            pos += 1

        node.next = current.next
        current.next = node

        self.size += 1




if __name__ == '__main__':
    # Create a list
    l = SinglyLinkedList()
    l.append('a')
    l.append('b')
    l.append('c')

    # Traverse the list
    current = l.head
    while current:
        print(current.data)
        current = current.next

    # Append at location
    l.append_at_location('new', 0)

    # Traverse the list
    current = l.head
    while current:
        print(current.data)
        current = current.next