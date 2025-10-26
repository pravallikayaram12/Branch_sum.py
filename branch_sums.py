#The sum of values along every path from the root to each leaf. 
#It uses recursion to walk the tree, keeping a running total for the current path and appending the total when it reaches a leaf. 
#The results are collected leftmost branch → rightmost branch.

# Step 1: Define the Binary Tree Node
from collections import deque

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSumsBFS(startNode):
    if startNode is None:
        return []

    sum = []
    nodes_to_visit = deque([(startNode, startNode.value)])  # queue holds (node, running sum)

    while nodes_to_visit:
        n, total = nodes_to_visit.popleft()

        # If leaf node, record running sum
        if n.left is None and n.right is None:
            sum.append(total)

        if n.left is not None:
            nodes_to_visit.append((n.left, total + n.left.value))

        if n.right is not None:
            nodes_to_visit.append((n.right, total + n.right.value))

    return sum

if __name__ == "__main__":
    startNode = BinaryTree(1)
    startNode.left = BinaryTree(2)
    startNode.right = BinaryTree(4)
    startNode.left.left = BinaryTree(6)
    startNode.left.right = BinaryTree(7)
    startNode.right.left = BinaryTree(9)
    startNode.right.right = BinaryTree(10)
    startNode.left.left.left = BinaryTree(11)
    startNode.left.left.right = BinaryTree(13)

    print("Branch sums (BFS):", branchSumsBFS(startNode))

