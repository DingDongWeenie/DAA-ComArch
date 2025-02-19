class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    def __repr__(self):
        return str(self.data)


class circlylist:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def insert_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            new_node.next = self.head
            cur.next = new_node
            self.head = new_node

    def insert_at(self, data, pos):
        if pos <= 0 or not self.head:
            self.insert_beginning(data)
            return
        cur = self.head
        index = 0
        while index < pos - 1 and cur.next != self.head:
            cur = cur.next
            index += 1
        new_node = Node(data, cur.next)
        cur.next = new_node

    def search(self, key):
        if not self.head:
            return False
        cur = self.head
        while True:
            if cur.data == key:
                return True
            cur = cur.next
            if cur == self.head:
                break
        return False

    def __str__(self):
        if not self.head:
            return "null"
        nodes = []
        cur = self.head
        while True:
            nodes.append(str(cur.data))
            cur = cur.next
            if cur == self.head:
                break
        return " -> ".join(nodes) + " -> head"


if __name__ == "__main__":
    cll = circlylist()
    cll.insert_end(30)
    cll.insert_end(40)
    cll.insert_beginning(10)
    cll.insert_at(20, 2)
    print(cll)
    print(cll.search(10))