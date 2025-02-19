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


if __name__ == "__main__":
    g = Graphs()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    print(g)