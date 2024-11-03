from queue import Queue

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree_graph(tree_root, graph=None):
    if graph is None:
        graph = nx.Graph()
    graph.add_node(tree_root.value)
    if tree_root.left:
        graph.add_edge(tree_root.value, tree_root.left.value)
        build_tree_graph(tree_root.left, graph)
    if tree_root.right:
        graph.add_edge(tree_root.value, tree_root.right.value)
        build_tree_graph(tree_root.right, graph)
    return graph


def depth_first_traversal(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            yield visited[:]


def breadth_first_traversal(root):
    queue = Queue()
    queue.put(root)
    visited = []
    while not queue.empty():
        node = queue.get()
        if node not in visited:
            visited.append(node)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
            yield visited[:]


def generate_color_codes(base_color="#1f78b4", num_colors=8):
    base_color_rgb = tuple(int(base_color[i:i + 2], 16) for i in (1, 3, 5))
    step = tuple(c / (num_colors - 1) for c in base_color_rgb)
    color_codes = []
    for i in range(num_colors):
        new_color = "#{:02x}{:02x}{:02x}".format(*[int(base_color_rgb[j] - step[j] * i) for j in range(3)])
        color_codes.append(new_color)
    return color_codes


def visualize_traversal(root, traversal_func, colors_db):
    tree_graph = build_tree_graph(root)
    pos = nx.spring_layout(tree_graph)
    traversal_steps = list(traversal_func(root))

    for i, step in enumerate(traversal_steps):
        node_colors = ['gray' for _ in tree_graph.nodes()]
        for node in step:
            node_colors[list(tree_graph.nodes()).index(node.value)] = colors_db[min(i, len(colors_db) - 1)]
        plt.figure(figsize=(10, 8))
        nx.draw(tree_graph, pos, with_labels=True, node_color=node_colors, font_weight='bold', font_color='white',
                node_size=1000)
        plt.title(f"Step {i + 1}")
        plt.show()


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)

    colors = generate_color_codes(base_color="#1f78b4", num_colors=6)

    print("DFS Traversal Visualization:")
    visualize_traversal(root, depth_first_traversal, colors)

    print("BFS Traversal Visualization:")
    visualize_traversal(root, breadth_first_traversal, colors)
