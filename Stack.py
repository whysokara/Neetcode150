class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item. Raise error if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def __getitem__(self, index):
        """Allow stack[index] access."""
        return self.items[index]

    def __len__(self):
        """Support len(stack)."""
        return len(self.items)

    def __repr__(self):
        """Return string representation of the stack."""
        return f"Stack({self.items})"


s = Stack()
s.push(10)
s.push(20)
s.push(30)

# print(s)          # Stack([10, 20, 30])
# print(s.items)    # as list [10, 20, 30]
# print(s.pop())   # 30
# print(s.peek())  # 20
# print(s[0])      # 10
# print(len(s))    # 2


# for i in s.items:
#     print(i)

# for item in reversed(s.items):
#     print(s.item[::,-1])

print(list(reversed(s.items))) 