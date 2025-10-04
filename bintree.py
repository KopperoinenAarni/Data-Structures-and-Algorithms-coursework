
# openDSA examples were used in help for most of the basic structure :) - thanks for the good material
# the slideshow examples of recursion really helped me in better understanding these concepts!

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.mirrored = False # put a status on tree if its mirrored or not

    # Inserts a new key to the BST
    def insert(self, key):
        self.root = self.__inserthelp(self.root, key)

    def __inserthelp(self, node, key):  
        if node == None:
            return Node(key) # if node is empty set it to be the key

        if self.mirrored == False: 
            if node.key > key: # check node and go left or right depending the size of it
                node.left = self.__inserthelp(node.left, key)
            elif node.key < key:
                node.right = self.__inserthelp(node.right, key)

        elif self.mirrored == True:
            if node.key < key: # check node and go left or right depending the size of it
                node.left = self.__inserthelp(node.left, key)
            elif node.key > key:
                node.right = self.__inserthelp(node.right, key)
        return node
    

    # Check if a key is in the BST
    def search(self, key):
        return self._searchhelp(self.root, key)
    
    def _searchhelp(self, node, key):
        if node == None:
            return False
        
        if self.mirrored == False:
            if node.key > key:  # check node and go left or right depending the size of it
                return self._searchhelp(node.left, key)
            elif node.key < key:
                return self._searchhelp(node.right, key)
            else: 
                return True
            
        elif self.mirrored == True:
            if node.key < key:  # if mirrored then do inverse in checking
                return self._searchhelp(node.left, key)
            elif node.key > key:
                return self._searchhelp(node.right, key)
            else: 
                return True



        
    # Removes a key from the BST
    def remove(self, key):
        self.root = self.__removehelp(self.root, key)

    def __removehelp(self, node, key):
        if node == None:
            return None
        
        if self.mirrored == False:
            if node.key > key:  # check node and go left or right depending the size of it
                node.left = self.__removehelp(node.left, key)
            elif node.key < key:
                node.right = self.__removehelp(node.right, key)
            else:
                if node.left == None: # if no left node, return right node
                    return node.right 
                elif node.right == None: # if not right node then return left node
                    return node.left
                else: 
                        node.key = self.__getmax(node.left) # if we have left and right node then get max from left side and substitute it into the removed nodes place
                        node.left = self.__removemax(node.left) # remove the max node from left side that was just substituted
            return node
        
        elif self.mirrored == True: # if tree is mirrored the do inverse operations because everything is on different side
            if node.key < key:  # if mirrored then do inverse in checking
                node.left = self.__removehelp(node.left, key)
            elif node.key > key:
                node.right = self.__removehelp(node.right, key)
            else:
                if node.left == None: # if no left node, return right node
                    return node.right 
                elif node.right == None: # if not right node then return left node
                    return node.left
                else: # use max from right subtree in mirrored tree
                    node.key = self.__getmax(node.right)
                    node.right = self.__removemax(node.right)
            return node

    # Finds the greatest key value from the BST
    def __getmax(self, node):
        if self.mirrored == False:
            if node.right == None:
                return node.key
            else: 
                return self.__getmax(node.right) 
        elif self.mirrored == True: # max value is on left side when mirrored
            if node.left == None:
                return node.key
            else:
                return self.__getmax(node.left)
        
        # Removes the greatest key value from the BST
    def __removemax(self, node):
        if self.mirrored == False: # if tree is not mirrored, then remove max value from right side, if is mirrored then max val is on left side
            if node.right == None: 
                return node.left
            node.right = self.__removemax(node.right)
            return node
        elif self.mirrored == True:
            if node.left == None: 
                return node.left
            node.left = self.__removemax(node.left)
            return node


        # prints the BST in preorder traversal
    def preorder(self):
        self.__preorderhelp(self.root)
        print()

    def __preorderhelp(self, node):
        if node != None: # if node is not none then print it, iterate recursively for each node make a call for each left and right node
            print(node.key, end=" ")
            self.__preorderhelp(node.left)
            self.__preorderhelp(node.right)
    
    def postorder(self):
        self.__postorderhelp(self.root)
        print()

    def __postorderhelp(self, node):
        if node != None: 
            self.__postorderhelp(node.left)
            self.__postorderhelp(node.right)
            print(node.key, end=" ") # we get postorder when putting print in end instead of start compared to preorder


    def inorder(self):
        self.__inorderhelp(self.root)
        print()

    def __inorderhelp(self, node):
        if node != None: 
            self.__inorderhelp(node.left)
            print(node.key, end=" ") # we get inorder when putting print in the middle. when I got this the naming made so much more sense 
            self.__inorderhelp(node.right)


    def breadthfirst(self):
        self.__breadthfirsthelp(self.root)
        print()

    def __breadthfirsthelp(self, node):
        if node != None:
            queue = [node]  # start from root node 
            while queue: 
                cur_node = queue.pop(0)  # remove first element from queue
                print(cur_node.key, end=" ")
                if cur_node.left != None:   # at each step add left and right to queue list
                    queue.append(cur_node.left)
                if cur_node.right != None:
                    queue.append(cur_node.right)
    

    def mirror(self):
        self.root = self.__mirrorhelp(self.root)
        if self.mirrored == True: # Swith the mirror status 
            self.mirrored = False
        elif self.mirrored == False: # always flip mirroring to different statuts than currently each run 
            self.mirrored = True 

    def __mirrorhelp(self, node):
        if node == None: 
            return None
        node.left, node.right = self.__mirrorhelp(node.right), self.__mirrorhelp(node.left) # swap each value from side to side 
        return node
    
if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)

    Tree.preorder()
    Tree.mirror()
    Tree.preorder()

    Tree.insert(8)
    Tree.remove(3)
    print(Tree.search(2))
    Tree.preorder()
    Tree.mirror()
    Tree.preorder()

