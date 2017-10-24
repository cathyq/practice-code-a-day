# Given the root node of a binary tree, is it also a binary search tree?
# Problem from Cracking the Coding Interview 


'''Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

def check_binary_search_tree_(root):
    inOrder(root)
    
    #return (len(tree) == len(set(tree))) and (tree == sorted(tree))
    if len(tree) != len(set(tree)):
        return False
    else:
        if tree == sorted(tree):
            return True
        else:
            return False
       
    
tree = []        
def inOrder(root): 
    if root is not None:
        inOrder(root.left)
        tree.append(root.data)
        inOrder(root.right)