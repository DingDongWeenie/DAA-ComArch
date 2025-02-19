class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    def __repr__(self):
        return str(self.data)


class Singlylist:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_beginning(self, data):
        self.head = Node(data, self.head)

    def insert_at(self, data, pos):
        if pos == 0:
            self.insert_beginning(data)
            return
        cur = self.head
        for _ in range(pos - 1):
            if not cur:
                return  # Position out of bounds
            cur = cur.next
        if cur:
            cur.next = Node(data, cur.next)

    def search(self, key):
        cur = self.head
        while cur:
            if cur.data == key:
                return True
            cur = cur.next
        return False

    def __str__(self):
        nodes = []
        cur = self.head
        while cur:
            nodes.append(str(cur.data))
            cur = cur.next
        return " -> ".join(nodes) + " -> null"


if __name__ == "__main__":
    sll = Singlylist()
    sll.insert_end(30)
    sll.insert_end(40)
    sll.insert_beginning(10)
    sll.insert_at(20, 2)
    print(sll)
    print(sll.search(10))