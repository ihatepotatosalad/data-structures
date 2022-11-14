class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]


a = Stack()

a.push(5)
a.push(4)
a.push(3)
a.push(2)
print(a.peek())

print(a.stack)
