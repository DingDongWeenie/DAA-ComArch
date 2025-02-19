# Data Structures Implementations

This repo contains various fundamental data structures in Python. 
The following data structures are included:

1. **Linked Lists**:
   - Doubly Linked List
   - Singly Linked List
   - Circular Linked List
2. **Stacks**
3. **Queues**
4. **Trees**
5. **Graphs**
6. **Heaps**

---





## 1. Singly Linked List
The Singly Linked List is also created in its own class. This list stores references to the next node only. It contains:

- The `insert_end` method, which adds data to the end of the list.
- The `insert_beginning` method, which inserts data at the start of the list.
- The `insert_at` method, which inserts at a given position.
- The `search` method, which looks for a value.
- The `__str__` method, which displays all nodes in the list.

The simplicity of singly linked lists makes them easy to work with.

- [SinglyList Asciinema](https://asciinema.org/a/XnPv5RothJG6UW8gP80BVEgYo)

### Quick Code Snippet:
```python
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

    def __str__(self):
        nodes = []
        cur = self.head
        while cur:
            nodes.append(str(cur.data))
            cur = cur.next
        return " -> ".join(nodes) + " -> null"
```


## 2. Doubly Linked List
The Doubly Linked List is created in a separate class for encapsulation and easy use. A doubly linked list allows each node to store references to the next and previous nodes. This means you can traverse the list both forwards and backwards.

- The `insert_end` method adds data to the end of the list.
- The `insert_beginning` method inserts data at the start.
- The `insert_at` method inserts data at a specified position.
- The `search` method looks for a specific value in the list.
- The `__str__` method displays all the elements in the list.

This allows flexibility and easy traversal of the list.

- [DoublyList Asciinema](//asciinema.org/a/vV8qPC0ez6Fho7Z0PQ7XW4omz)

### Quick Code Snippet:
```python
class Node:
    def __init__(self, data, next_=None, prev=None):
        self.data = data
        self.next = next_
        self.prev = prev

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

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " <-> ".join(nodes) + " <-> null"

dll = doublylist()
dll.insert_end(30)
dll.insert_end(40)
print(dll)
```

CirclyList
The Circular Linked List is similar to a singly linked list, but its last node points back to the first node, creating a loop:

- The `insert_end` method adds elements to the end of the circular list.
- The `insert_beginning` method adds elements at the start.
- The `insert_at` method inserts elements at a specific position.
- The `search` method checks if a value exists in the list.
- The `__str__` method displays all elements, looping back to the head.

Circular linked lists are useful for looping scenarios.

- [CirclyList Asciinema](https://asciinema.org/a/lpJWtT0zq2ugrubVJvszkVgd7)

### Quick Code Snippet:
```python
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
```
Graphs

https://asciinema.org/a/hp9YdRqrk1JOQKvYVMGqMtLxY

Heaps

https://asciinema.org/a/K3adywAuQtfnRrWKqMR5cqppY

Queues

https://asciinema.org/a/Kj82pKqFojhjIOEAkx5RyRNBw

Stacks

https://asciinema.org/a/jijcU98TrKEUfUBbncpFar1Sa

Trees

https://asciinema.org/a/9nAs3jaz4JhcqkdVLBmgVlGrP
