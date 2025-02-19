class Node:
    def __init__(self, data, next_=None, prev=None):
        self.data = data
        self.next = next_
        self.prev = prev

    def __repr__(self):
        return str(self.data)


class doublylist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at(self, data, pos):
        if pos <= 0 or not self.head:
            self.insert_beginning(data)
            return

        current = self.head
        index = 0
        while current and index < pos:
            current = current.next
            index += 1

        if not current:
            self.insert_end(data)
        else:
            new_node = Node(data, next_=current, prev=current.prev)
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node
            if new_node.prev is None:
                self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " <-> ".join(nodes) + " <-> null"


if __name__ == "__main__":
    dll = doublylist()
    dll.insert_end(30)
    dll.insert_end(40)
    dll.insert_beginning(10)
    dll.insert_at(20, 2)
    print(dll)
    print(dll.search(10))