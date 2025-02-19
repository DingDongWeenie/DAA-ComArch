class Queues:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return "Queue: " + " -> ".join(map(str, self.items))


if __name__ == "__main__":
    queue = Queues()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue)
    print("Dequeued:", queue.dequeue())
    print(queue)