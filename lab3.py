import os
black = 'BLACK'
red = 'RED'

class Node:
    def __init__(self, item=None, left=None, right=None, parent=None, color=red):
        self.item = item
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 1
        self.color = color

class RBTree:
    def __init__(self, root=None):
        self.root = root
        self.height = -1
        self.balance = 0
    def __contains__(self,k):
        return self.search(k)
    
    def search(self,k):
        return self._search(k,self.root)
    
    def BSTInsert(self, Node = None):
         if self.root is None:
           self.root = Node
           Node.left = None
           Node.right = None
         else:
           curr = self.root
           while curr is not None: 
             if Node.item < curr.item:
                if curr.left is None:
                  curr.left = Node
                  curr = None
                else:
                  curr = curr.left
             else:
                if curr.right is None:
                  curr.right = Node
                  curr = None
                else:
                  curr = curr.right       
           Node.left = None
           Node.right = None
    def RBTreeInsert(self, Node = None):
        self.BSTInsert(Node)
        Node.color = red
        self.RBTreeBalance(Node)
        
    def print_tree(self):
        self._print_tree(self.root)
        
    def _print_tree(self, node):
        if node is None:
            return
        
        self._print_tree(node.left)
        print(node.item)
        self._print_tree(node.right)
        
    def RBTreeBalance(self, Node):
        if Node.parent is None:
            Node.color = black
            return
        if Node.parent.color is black:
            return
        parent = Node.parent
        grandparent = self.RBTreeGetGrandparent(Node)
        uncle = self.RBTreeGetUncle(Node)
        if uncle is not None and uncle.color is red:
             parent.color = uncle.color = black
             grandparent.color = red
             self.RBTreeBalance(grandparent)
             return
          
        if Node is parent.right and parent is grandparent.left:
            self.RBTreeRotateLeft(parent)
            Node = parent
            parent = Node.parent
             
        elif Node is parent.left and parent is grandparent.right:
             self.RBTreeRotateRight(parent)
             Node = parent
             parent = Node.parent
             
        parent.color = black
        grandparent.color = red
        if Node is parent.left:
            self.RBTreeRotateRight(grandparent)
        else:
            self.RBTreeRotateLeft(grandparent)

    def RBTreeGetGrandparent(self,Node = None):
        if Node.parent is None:
            return None
        return Node.parent.parent

    def RBTreeGetUncle(self,Node = None):
        grandparent = None
        if Node.parent is not None:
            grandparent = Node.parent.parent
        if grandparent is None:
            return None
        if grandparent.left is Node.parent:
            return grandparent.right
        else:
            return grandparent.left
    
    def RBTreeRotateRight(self, Node = None):
        leftRightChild = Node.left.right
        if Node.parent is None:
            self.RBTreeReplaceChild(Node.parent, Node, Node.left)
        else:
            self.root = Node.left
            self.root.parent = None
            
        self.RBTreeSetChild(Node.left, "right", Node)
        self.RBTreeSetChild(Node, "left", leftRightChild)
    
    def RBTreeRotateLeft(self, Node = None):
        RightLeftChild = Node.right.left
        if Node.parent is None:
            self.RBTreeReplaceChild(Node.parent, Node, Node.right)
        else:
            self.root = Node.right
            self.root.parent = None
            
        self.RBTreeSetChild(Node.right, "left", Node)
        self.RBTreeSetChild(Node, "right", RightLeftChild)
    def RBTreeSetChild(self, parent, whichChild, child):
        if whichChild is not "left" and whichChild is not "right":
            return False

        if whichChild is "left":
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent
        return True
    
    def RBTreeReplaceChild(self, parent1, currentChild, newChild):
        if parent1.left is currentChild:
            return self.RBTreeSetChild(parent1, "left", newChild)
        elif parent1.right == currentChild:
            return self.RBTreeSetChild(parent1, "right", newChild)
        return False
    
    def _search(self, k, Node):
            if Node is None:
                return False
            if Node.item == k:
                return True
            if k > Node.item:
                return self._search(k,Node.right)
            return self._search(k, Node.left)

class AVLTree:
    
    def __init__(self, root=None):
        self.root = root
        self.height = -1
        self.balance = 0
    
    def __contains__(self,k):
        return self.search(k)
    
    def search(self,k):
        return self._search(k,self.root)
    
    def AVLTreeInsert(self, Node = None):
        if self.root is None:
          self.root = Node
          Node.parent = None
          return
      
        curr =self.root
        while curr is not None:
          if Node.item < curr.item:
             if curr.left is None:
                curr.left = Node
                Node.parent = curr
                curr = None
             else:
                curr = curr.left
          else:
              if curr.right is None:
                  curr.right = Node
                  Node.parent = curr
                  curr = None
              else:
                  curr = curr.right
             
        Node = Node.parent
        while Node is not None:
            self.AVLTreeRebalance(Node)
            Node = Node.parent

    def AVLTreeRebalance(self, Node = None):
        self.AVLTreeUpdateHeight(Node)        
        if self.AVLTreeGetBalance(Node) == -2:
            if self.AVLTreeGetBalance(Node.right) == 1:
                self.AVLTreeRotateRight(Node.right)
                return self.AVLTreeRotateLeft(Node)
            elif self.AVLTreeGetBalance(Node) == 2:
                if self.AVLTreeGetBalance(Node.left) == -1:
                    self.AVLTreeRotateLeft(Node.left)
                return self.AVLTreeRotateRight(Node)   
        return Node
    
    def AVLTreeRotateRight(self, Node = None):
       leftRightChild = Node.left.right
       if Node.parent is not None:
          self.AVLTreeReplaceChild(Node.parent, Node, Node.left)
       else:
           self.root = Node.left
           self.root.parent  = None
       self.AVLTreeSetChild(Node.left, "right", Node)
       self.AVLTreeSetChild(Node, "left", leftRightChild)
       
    def AVLTreeRotateLeft(self, Node = None):
       RightLeftChild = Node.right.left
       if Node.parent is not None:
          self.AVLTreeReplaceChild(Node.parent, Node, Node.right)
       else:
           self.root = Node.right
           self.root.parent  = None
       self.AVLTreeSetChild(Node.right, "left", Node)
       self.AVLTreeSetChild(Node, "right", RightLeftChild)
    
    def AVLTreeUpdateHeight(self, Node = None):
        left_height = -1
        if Node.left is not None:
            left_height = Node.left.height
        right_height = -1
        if Node.right is not None:
            right_height = Node.right.height
        Node.height = max(left_height, right_height) + 1
    
    def AVLTreeSetChild(self, parent1, whichChild, child):
        if whichChild != "left" and whichChild != "right":
           return False
        if whichChild == "left":
           parent1.left = child
        else:
           parent1.right = child
        if child is not None:
           child.parent = parent1
        self.AVLTreeUpdateHeight(parent1)
        return True
    
    def AVLTreeReplaceChild(self,parent1, currentChild, newChild):
       if parent1.left == currentChild:
          return self.AVLTreeSetChild(parent1, "left", newChild)
       elif parent1.right == currentChild:
          return self.AVLTreeSetChild(parent1, "right", newChild)
       return False
    
    def AVLTreeGetBalance(self, Node=None):
       left_Height = -1
       if Node.left is not None:
          left_Height = Node.left.height
       right_Height = -1
       if Node.right is not None:
          right_Height = Node.right.height
       return left_Height - right_Height
   
    def _search(self, k, Node):
        if Node is None:
            return False
        if Node.item == k:
            return True
        if k > Node.item:
            return self._search(k,Node.right)
        return self._search(k, Node.left)
    
def read_file(file):
    answer = input("do you want to use Red and black Binary Tree (RB) or AVL Binary Tree(AVL)")
    if answer == '0':
        english_words = RBTree()
    elif answer == '1':
        english_words = AVLTree()
    os.chdir(r'C:/Users/Eng/Documents/CS/2302/lab3')
    with open(file) as f:
        for i in f:
            if answer == '0':
                temp = Node(i.strip())
                english_words.RBTreeInsert(temp)
                
            elif answer == '1':
                temp = Node(i.strip())
                english_words.AVLTreeInsert(temp)
                #print(i)
    print("Done")
    return english_words

def print_anagrams(word, english_words, prefix=""):
   if len(word) <= 1:
       str = prefix + word

       if str in english_words:
           print(prefix + word)
   else:
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur
           
           if cur not in before: # Check if permutations of cur have not been generated.
               print_anagrams(before + after, english_words , prefix + cur)

def main():
    tree = read_file("example.txt")
    #tree.print_tree()
    #print_anagrams("bca", tree)
    print_anagrams("oio",tree)

if __name__ == "__main__":
    main()