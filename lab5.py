# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:48:06 2019

@author: Eng
"""

class Node:
    def __init__(self, key, value, next = None, prev = None):
        self.item = value;
        self.next = next;
        self.prev = prev
        self.key = key

class LRUcache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.head = None
        self.tail = None

    def remove(self, node):
        if self.head is None and self.tail is None:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
          self.head = self.head.next  
        elif node == self.tail:
            self.tail = self.tail.prev
        else: #middle
            previous_node = node.prev
            next_node = node.next
            previous_node.next = next_node
            next_node.prev = previous_node
    
    def add (self, node):
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.dict[node.key] = node
        
        
    def printing(self):
        temp = self.head
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
        print()

    def get(self, key):
        if key not in self.dict:
            return -1
        else:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.item

    def put(self, key, value):
        if key in self.dict:
            self.remove(self.dict[key])
        new_node = Node(key, value)
        self.add(new_node)
        self.dict[key] = new_node
        if len(self.dict) > self.capacity:
            del self.dict[self.head.key]
            self.head = self.head.next
       
        
        

if __name__ == '__main__':
    
    cache = LRUcache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.printing()
    print(cache.get(1))       #// returns 1
    cache.put(3, 3)
    cache.printing()    #// evicts key 2
    print(cache.get(2))      #// returns -1 (not found)
    cache.put(4, 4)
    #// evicts key 1
    cache.printing()
    print(cache.get(1))       #// returns -1 (not found)
    print(cache.get(3))       #// returns 3
    print(cache.get(4)) #evicts key 1

    
 