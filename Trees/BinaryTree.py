## Binary tree with four nodes (2,3,4,5)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

## Initializing and allocate memory for tree nodes
firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)

## connect binary tree nodes

firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode