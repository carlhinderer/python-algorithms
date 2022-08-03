class Node:
    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        return self._data

    def set_data(self, node_data):
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        return self._next

    def set_next(self, node_next):
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        return str(self._data)


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

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
            current = current.next

        return False

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
