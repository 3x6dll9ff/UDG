class OrderNode:
    def __init__(self, name: str = None, name_dishes: str = None, time: int = None, priority: int = None):
        self.order = {
            "name": name,
            "name_dishes": name_dishes,
            "time": time,
            "priority": priority
        }
        self.next = None
        self.prev = None


class DoubleListOrder:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    # Добавление заказа в начало списка
    def add_order_to_start(self, order: OrderNode):
        if self.head is None:  # Если список пуст, инициализируем head и tail
            self.head = order
            self.tail = order
        else:
            order.next = self.head  # Устанавливаем next для нового узла
            self.head.prev = order  # Устанавливаем prev для текущего head
            self.head = order       # Новый узел становится головой списка
    
    def add_order_to_end(self, order: OrderNode):
        if self.tail is None:  # Если список пуст, инициализируем head и tail
            self.head = order
            self.tail = order
        else:
            current = self.tail  # Устанавливаем prev для нового узла
            current.next = order  # Устанавливаем next для текущего tail
            current.prev = current       # Новый узел становится хвостом списка
            self.tail = order       # Новый узел становится хвостом списка

    def delete_by_name(self, name):
        if self.head is None:
            return 'None'
        else:
            if self.head.order['name'].lower() == name.lower():
                current = self.head
                self.head = self.head.next
                self.head.prev = None
                current.next = None
            else:
                current = self.head
                prev = None
                while current is None:
                    if current.order['name'].lower() == name.lower():
                        prev.next = current.next
                        current.next.prev = prev
                        current.next = None
                        current.prev = None
                    prev = current
                    current = current.next
                    

    def sort_by_priority(self):
        priority1 = []
        priority2 = []
        current = self.head
        while current is not None:
            if current.order['priority'] == 1:
                priority1.append(current)
            else:
                priority2.append(current)
            current = current.next
        print('Orders with lower priority: \n' + '\n'.join([str(order.order) for order in priority1]))
        print("")
        print('Orders with highest priority: \n' + '\n'.join([str(order.order) for order in priority2]))


    #broj narudzbi nakon zadatog vremena
    def number_order_time(self, entered_time):
        if self.head is None:
            return '0'
        count = 0
        current = self.head

        while current:
            if current.order['time'] > entered_time:
                count += 1
            current = current.next
        return print('Number Order Time : ' + str(count + 1))

    def remove_last_element(self):
        if self.head is None:
            return '0'
        else:
            current = self.tail
            current.prev.next = None
            self.tail = current.prev
            current.prev = None



    def print_list(self):
        if self.head is None:
            print("List je prazna!")
        else:
            current = self.head
            while current is not None:
                print(current.order)
                current = current.next
                
    

# Создаём заказы
order1 = OrderNode('Marko Prkovic', 'Pizza', 600, 1)
order2 = OrderNode('Anna Pekovic', 'Hamburger', 300, 2)
order3 = OrderNode('Vasily Markovic', 'Pasta', 320, 1)
order4 = OrderNode('Ivan Ivanovic', 'Pizza', 140, 1)
order5 = OrderNode('Valentina Misebic', 'Pizza', 600, 2)
order6 = OrderNode('Oleg Ponovic', 'Pizza', 720, 1)

# Добавляем заказы в двусвязный список
double_list_order = DoubleListOrder()
double_list_order.add_order_to_start(order1)
double_list_order.add_order_to_start(order2)
double_list_order.add_order_to_start(order3)
double_list_order.add_order_to_start(order4)
double_list_order.add_order_to_start(order5)
double_list_order.add_order_to_end(order6)
double_list_order.print_list()
print('')
double_list_order.delete_by_name('Valentina Misebic')

# Печать списка

double_list_order.sort_by_priority()
double_list_order.number_order_time(300)
