# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:48:06 2019

@author: Eng
"""

class Node:
    def __init__(self, item, next = None, prev = None, key = None):
        self.item = item;
        self.next = next;
        self.prev = prev
        self.key = key


class DoublyLinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail


    def insertAtStart(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next
            self.tail.next = None


    def remove(self, value):
        
        if self.head.item == value:
            self.head = self.head.next
            self.head.prev = None
            return self.head
        elif self.tail.item == value:
            self.tail = self.tail.prev
            self.tail.next = None
            return self.tail
        else:
            temp = self.head.next
            while temp.next is not None:
                if temp.item == value:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return temp
                else:
                    temp = temp.next
    def printDouble(self):
        temp = self.head
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
            
class LRUcache:
    def __init__(self, capacity):
        self.capacity =capacity
        self.dict = {}
        self.size = 0

    def set_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.current_size += 1
    
    def get(self, key):
        if key not in self.dict:
            return -1
        else:
            return self.dict[key]
    
    def put(self, key, value):
        if key in self.dict:
            node = self.dict[key]
            node.item = value
            
        else:
            new_node = Node(key, value)
            if self.size == self.capacity:
                del self.dict[self.tail.key]
                self.remove(self.tail)
            self.set_head(new_node)
            self.hash_map[key] = new_node
        

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insertAtStart(1)
    dll.insertAtStart(2)
    dll.insertAtEnd(3)
    dll.insertAtStart(4)
    dll.printDouble()
    dll.remove(2)
    print()
    dll.printDouble()
 