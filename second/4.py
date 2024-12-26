class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def prepend(self, new_element):
        if self.head == None:
            self.head = new_element
        new_element.next = self.head
        self.head = new_element

    def append(self, new_element):
        current = self.head
        if self.head == current:
         while current.next:
            current = current.next
         current.next = new_element
        else:
            self.head = new_element

    def print_list(self):
        current = self.head
        if self.head:
            while current.next:
                print(current.value)
                current = current.next
            print(current.value)
        else:
            print(current.value)

    def delete_first_element(self):
        current = self.head
        self.head = self.head.next
        current.next = None

    def delete_last_element(self):
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def find_element_by_index(self, index):
        current = self.head
        for i in range(index):
            if current:
                current = current.next
                print(current.value)
            else:
                return None
        return current.value
    
    def get_list_lenght(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return print(f"count of list : {count}")



node1 = Node(4)
node2 = Node(5)
node3 = Node(12)
node4 = Node(7)

ll = LinkedList(node1)
ll.prepend(node2)
ll.prepend(node3)
ll.prepend(node4)

ll.delete_last_element()
ll.find_element_by_index(2)
ll.get_list_lenght()
ll.print_list()
