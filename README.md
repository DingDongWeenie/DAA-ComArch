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
The Singly Linked List stores items where each one points only to the next item.

- The `insert_end` method adds an item to the end of the list.
- The `insert_beginning` method adds an item at the start.
- The `insert_at` method inserts an item at a specific position.
- The `search` method looks for an item.
- The `__str__` method displays all items from start to end.

### Example Use:
This is ideal for scenarios like navigating through a to-do list or any single-direction task list.
### Asciinema:
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






---
## 2. Doubly Linked List
The Doubly Linked List that I wrote stores items that are connected to both their previous and next items, making it easy to move in both directions. 

- The `insert_end` method adds an item to the end of the list.
- The `insert_beginning` method adds an item at the start.
- The `insert_at` method inserts at a specific position.
- The `search` method looks for an item.
- The `__str__` method displays all the items.

### Example Use:
This is useful for things like undo/redo functions or navigating a playlist where you can go both forward and backward.
### Asciinema:
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






---
## 3. Circular Linked List
The Circular Linked List is similar to a singly linked list, but the last item connects back to the first item, forming a loop.

- The `insert_end` method adds an item to the end.
- The `insert_beginning` method adds an item at the start.
- The `insert_at` method inserts an item at a specific position.
- The `search` method checks if an item is in the list.
- The `__str__` method displays all the items in the loop.

### Example Use:
This is useful for things like round-robin scheduling or board games where turns rotate in a circle.
### Asciinema:
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






---
## 4. Graphs
The Graph I wrote represents connections between items (nodes).

- The `add_node` method adds new nodes.
- The `add_edge` method connects two nodes.
- The `__str__` method shows all the nodes and their connections.

### Example Use:
Graphs are great for representing social networks, maps, or recommendation systems.
### Asciinema:
- [Graphs Asciinema](https://asciinema.org/a/hp9YdRqrk1JOQKvYVMGqMtLxY)

### Quick Code Snippet:
```python
class Graphs:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)

    def __str__(self):
        return "\n".join(f"{node}: {neighbors}" for node, neighbors in self.adj_list.items())

```






---
## 5. Heaps
I implemented a Min Heap, where the smallest item is always at the top.

- The `push` and `insert` methods add items while keeping the heap sorted.
- The `pop` method removes and returns the smallest item.
- The `peek` method shows the smallest item without removing it.
- The `__str__` method displays all the items.

### Example Use:
Heaps are useful for priority queues or for finding the smallest elements in a set of data.
### Asciinema:
- [Heaps Asciinema](https://asciinema.org/a/K3adywAuQtfnRrWKqMR5cqppY)

### Quick Code Snippet:
```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self._heapify_down(0)
        return item

    def __str__(self):
        return "Heap: " + ", ".join(map(str, self.heap))
```





---
## 6. Queues
The Queue follows the "first in, first out" (FIFO) rule. The first item added is the first one removed.

- The `enqueue` method adds an item to the queue.
- The `dequeue` method removes and returns the first item.
- The `is_empty` method checks if the queue is empty.
- The `__str__` method displays all the items.

### Example Use:
Queues are great for customer service lines or managing tasks in order of arrival.
### Asciinema:
- [Queues Asciinema](https://asciinema.org/a/Kj82pKqFojhjIOEAkx5RyRNBw)

### Quick Code Snippet:
```python
class Queues:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def __str__(self):
        return "Queue: " + " -> ".join(map(str, self.items))

```





---
## 7. Stacks
The Stack follows the "last in, first out" (LIFO) rule. The last item added is the first one removed.

- The `push` method adds an item to the stack.
- The `pop` method removes and returns the last item.
- The `peek` method shows the last item without removing it.
- The `is_empty` method checks if the stack is empty.
- The `__str__` method displays all the items.

### Example Use:
Stacks are perfect for browser history (going back to the last page) or undo features in apps.
### Asciinema:
- [Stacks Asciinema](https://asciinema.org/a/jijcU98TrKEUfUBbncpFar1Sa)

### Quick Code Snippet:
```python
class Stacks:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def __str__(self):
        return "Stack: " + " -> ".join(map(str, self.items))
```





---
## 8. Trees
The Tree I wrote is a binary search tree (BST), where each item has left and right children.

- The `insert` method adds items to the tree. Smaller items go to the left, and larger items go to the right.
- The `in_order` method shows all items in sorted order.
- The `__str__` method displays the tree in order.

### Example Use:
Trees are useful for organizing data in file systems or for search engines to quickly find information.
### Asciinema:
- [Graphs Asciinema](https://asciinema.org/a/9nAs3jaz4JhcqkdVLBmgVlGrP)

### Quick Code Snippet:
```python
class Trees:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = TreeNode(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = TreeNode(data)
```
