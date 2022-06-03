
class Stack():
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else: return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def size(self):
        size = len(self.stack)
        return size