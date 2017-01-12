#Complete the preOrder function in your editor below, which has  parameter: a pointer to the root of a binary tree. It must print the values in the tree's preorder traversal as a single line of space-separated values.

#Input Format

#Our hidden tester code passes the root node of a binary tree to your preOrder function.

#Output Format

#Print the tree's preorder traversal as a single line of space-separated values.


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    #Write your code here
    current = []
    all_nodes = [root.data]
    addNode(root, current)
    
    while current:
        new_node = current.pop()
        all_nodes.append(new_node.data)
        if new_node.left:
            addNode(new_node, current)
        elif new_node.right:
            addNode(new_node, current)
            
    for i in all_nodes:
        print i,


def addNode(node, currentlst):
    if node.right:
        currentlst.append(node.right)
    if node.left:
        currentlst.append(node.left)
    return