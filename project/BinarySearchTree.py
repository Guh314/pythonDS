#!usr/bin/env python3

import random

#Binary Search Tree 
class BST:

    #Node
    class BSTNode:
        def __init__(self,val=None, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
        
        def get_val(self):
            return self.val
        
        def set_val(self, new_val):
            self.val = new_val
        
        def get_right(self):
            return self.right

        def get_left(self):
            return self.left
        
        def set_left(self, new_left):
            self.left = new_left

        def set_right(self, new_right):
            self.right = new_right

        def has_child(self):
            if self.get_right() != None or self.get_left() != None:
                return True
            return False

        def get_right_most(self):
            def __get_right_most(root):
                if root.get_right():
                    __get_right_most(root.get_right())
                return root
            new_root = __get_right_most(self.left)
            return new_root


        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self.val

            if self.right != None:
                for elem in self.right:
                    yield elem

    def __init__(self):
        self.root = None

    
    #Inserting elements in a BST
    def insert(self, elem):
        
        #Recursive Function to insert elements
        def __insert(root, elem):
            if root == None:                                        #First case, root = None
                return BST.BSTNode(elem) 
            if elem < root.get_val():                               #Second case, elem < root.get_val()
                root.set_left(__insert(root.get_left(), elem))
            if elem > root.get_val():                               #Third case, elem > root.get_val()
                root.set_right(__insert(root.get_right(), elem))
            return root                                             #Fourth case, elem == root.get_val()

        #The __insert function call
        self.root = __insert(self.root, elem)

    def delete(self, elem):

        #Search a element in the Tree and return it's subtree or None if it's not there
        def __search(root, elem):        
            print(root)
            if root:
                if root.get_val() == elem: return root
                if elem < root.get_val(): return __search(root.get_left(), elem)
                if elem > root.get_val(): return __search(root.get_right(), elem)
            return None

        #The Deletion function
        def __delete(root, elem):
            if root:
                if not root.has_child():
                    return root.set_val(None)
                if root.get_left is not None and root.get_right() is None:
                    return root.get_left()
                if root.get_left is None and root.get_right() is not None:
                    return root.get_right()
                root.set_val(root.get_right_most())
                return __delete(root.get_left(), root.get_val())
            return None

        sub_tree_to_delete_elem = __search(self.root, elem)
        if sub_tree_to_delete_elem:
            return __delete(sub_tree_to_delete_elem, elem)
                

    #Preorder reading of the tree
    def preorder(self):

        #Recursive function to do the reading
        def __preorder(root):
            if root == None: return                                 #Only has one case, if node is None
            print(root.get_val())
            __preorder(root.get_left())
            __preorder(root.get_right())
        __preorder(self.root)
    
    #Inorder reading of tree
    def inorder(self):
        def __inorder(root):
            if root == None: return
            __inorder(root.get_left())
            print(root.get_val())
            __inorder(root.get_right())
        __inorder(self.root)

    #Postorder reading of tree
    def postorder(self):
        def __postorder(root):
            if root == None: return
            __postorder(root.get_left())
            __postorder(root.get_right())
            print(root.get_val())
        __postorder(self.root)

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:   
            return [].__iter__()


def random_list(num):
    lst = []
    for i in range(num):
        lst.append(random.randint(0, 10))
    return lst

def print_tree(Tree):
    for x in Tree:
        print(x)

def main():
    Tree = BST()
    lst = random_list(10)
    
    Tree.insert(50)
    
    Tree.insert(40)

    Tree.insert(60)

    Tree.insert(30)

    Tree.insert(45)
    
    Tree.insert(55)
    
    Tree.insert(65)

    #print("\n\n")
    #print("Preorder:")
    #Tree.preorder()

    #print("\n\n")
    #print("Inorder:")
    #Tree.inorder()
    
    #print("\n\n")
    #print("Postorder:")
    #Tree.postorder()
    print_tree(Tree)
    Tree.delete(30)
    print_tree(Tree)
    Tree.delete(60)
    print_tree(Tree)
    #print("\n\n")

if __name__ == "__main__":
    main()
