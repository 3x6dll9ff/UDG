class Node:
    def __init__(self, data=None, next=None):
        self.__data = data
        self.__next = next

    # GETTER_DATA
    @property
    def data(self):
        return self.__data

    # SETTER_DATA
    @data.setter
    def data(self, data):
        self.__data = data

    # GETTER_NEXT\
    @property
    def next(self):
        return self.__next

    # SETTER_NEXT
    @next.setter
    def next(self, next):
        self.__next = next


class LinkedList:
    def __init__(self, head=None):
        self.__head = head

    # GETTER_HEAD
    @property
    def head(self):
        return self.__head

    # SETTER_HEAD
    @head.setter
    def head(self, head):
        self.__head = head

    def append(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = new_node
        else:
            current = self.__head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.__head  # Новый элемент становится "головой"
        self.__head = new_node

    # встроенный геттер по индексу
    def __getitem__(self, index):
        current = self.__head
        for i in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None:
            raise IndexError("Index out of range")
        return current.data

    def get_length(self):
        current = self.__head
        count = 0  # Начинаем с нуля, так как список может быть пустым
        while current is not None:
            current = current.next
            count += 1
        return count

    def __len__(self):
        return self.get_length()  # Опираемся на метод get_length

    def remove_last_item(self):
        if self.__head is None:
            return  # Список пуст, нечего удалять

        if self.__head.next is None:
            self.__head = None  # В списке только один элемент
            return

        current = self.__head
        while current.next.next is not None:  # Находим предпоследний элемент
            current = current.next
        current.next = None  # Удаляем последний элемент

    def remove_first_item(self):
        if self.__head is not None:
            self.__head = self.__head.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.append(2)
    llist.append(3)
    llist.append(4)
    print(llist[1])  # Ожидаемый вывод: 3
