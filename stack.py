from numpy import random

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, data):
        self.stack.append(data)
        self.size += 1

    def pop(self):
        
        if self.size > 0:
            n = self.stack[-1]
            self.stack = self.stack[:-1]
            self.size -= 1 
            return n

        return None

    def peek(self):
        if self.size > 0:
            return self.stack[-1]

        return None

    def isEmpty(self):
        return len(self.stack) == 0

    def get_size(self):
        return self.size

    def __str__(self):
        return ", ".join(map(str, self.stack[::-1]))

st = Stack()

st.push(5)
st.push(10)
st.push(15)
print(st.pop())

print(st.peek())
print(st.isEmpty())
print(st.get_size())
print(st)

