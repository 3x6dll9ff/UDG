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
        
        reversed_string = []
        while not self.is_empty():
            reversed_string.append(self.pop())
        
        return ' '.join(reversed_string)

# Пример использования
stack = Stack()
sentence = "Ovo je primer recenici"
print(stack.reverse_sentence(sentence))


