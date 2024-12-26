class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0
    
    def show_orders(self):
        if not self.is_empty():
            print("Order")
            for order in self.items:
                print(order)
        else:
            print("No orders in the queue.")
    def is_empty(self):
        return len(self.items) == 0
    

bank_queue = Queue()
bank_queue.enqueue("Client A")
bank_queue.enqueue("Client B")
bank_queue.enqueue("Client C")

print(bank_queue.dequeue())  
print(bank_queue.dequeue())  

