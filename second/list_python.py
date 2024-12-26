class Node:
    def __init__(self, head= None,tail=None):
        self.data = head
        self.prev = None
        self.value = value

class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, element):
        if self.head is not None:
            self.head = element
            self.tail = element
        else:
            current = self.tail
            current.next = element
            element.prev = current
            self.tail = element

    def get_list_lenght_from_tail(self):
        current = self.tail
        count = 0
        while current is not None:
            count += 1
            current = current.prev
        return count
