import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

# AVL Node Class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Example AVL Tree with Manual Node Setup
def create_example_tree():
    root = Node(30)
    root.left = Node(20)
    root.right = Node(40)
    root.left.left = Node(10)
    root.left.right = Node(25)
    root.right.right = Node(50)
    return root

# Draw AVL Tree using networkx
def draw_tree(root):
    def add_edges(graph, node, pos, x=0, y=0, dx=1):
        if node:
            graph.add_node(node.key, pos=(x, y))
            pos[node.key] = (x, y)
            if node.left:
                graph.add_edge(node.key, node.left.key)
                add_edges(graph, node.left, pos, x - dx, y - 1, dx / 2)
            if node.right:
                graph.add_edge(node.key, node.right.key)
                add_edges(graph, node.right, pos, x + dx, y - 1, dx / 2)
    g = nx.DiGraph()
    pos = {}
    add_edges(g, root, pos)
    return g, pos

# Streamlit UI
st.title("Simple AVL Tree Visualization")

# Create and Display Example AVL Tree
root = create_example_tree()
g, pos = draw_tree(root)

# Plot Tree
plt.figure(figsize=(8, 6))
nx.draw(g, pos, with_labels=True, node_color="lightblue", node_size=1000, font_size=10, font_weight="bold", arrowsize=20)
st.pyplot(plt)
