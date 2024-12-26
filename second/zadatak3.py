
# a)
# class Sub:
#     def __init__(self, name, duration):
#         self.name = name
#         self.duration = duration
    
#     def enqueue(self, item):
#         self.items.append(item) 

#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)  
#         raise IndexError("Dequeue from empty queue") 

#     def front(self):
#         if not self.is_empty():
#             return self.items[0]  
#         raise IndexError("Front from empty queue")

#     def is_empty(self):
#         return len(self.items) == 0  

#     def size(self):
#         return len(self.items)  

#     def print_filter_by_duration(self, N):
#         for i in range(len(self.items)):
#             if i % 2 == 0 and self.items[i].duration > N:
#                 print(self.items[i].name)
        
    


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def is_empty(self):
        return len(self.items) == 0
    
    def reverse_sentence(self, sentence):
        words = sentence.split()
        for word in words:
            self.push(word)

# Пример использования
stack = Stack()
sentence = "matematika programiranje "
print(stack.reverse_sentence(sentence))


