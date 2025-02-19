class Stacks:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return "Stack: " + " -> ".join(map(str, self.items))


if __name__ == "__main__":
    stack = Stacks()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)
    print("Popped:", stack.pop())
    print(stack)