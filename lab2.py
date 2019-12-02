class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_last(self, item):

        if self.head is None:  
            self.head = Node(item, self.head)
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next

        curr.next = Node(item)

    def add_first(self, item):
        self.head = Node(item, self.head)

    def add(self, index, item):
        if index == 0:
            self.head = Node(item, self.head)
            return

        if index < 0: 
            return

        curr = self.head
        for i in range(index - 1):  
            if curr is None:
                return

            curr = curr.next

        if curr is not None:
            curr.next = Node(item, curr.next)
    
    def print_list(self):
        current = self.head
        
        while current is not None:
            print(current.item)
            current = current.next
            
    def contains(self, item):
        return self.index_of(item) != -1

    def index_of(self, item):
        curr = self.head
        i = 0
        while curr is not None:
            if curr.item == item:
                return i
            i += 1
            curr = curr.next
        return -1

    def get(self, index):
        if index < 0:
            return None

        curr = self.head

        for i in range(index): 
            if curr is None:
                return None

            curr = curr.next

        return None if curr is None else curr.item

    def get_first(self):
        if self.head is None:
            return 
        else:
            return self.head.item

    def get_last(self):
        if self.head is None:
            return None

        curr = self.head
        while curr.next is not None:
            curr = curr.next

        return curr.item
    

    def remove_same(self, index):
        if index < 0:  # Don't do anything if index is invalid
            return

        if index == 0:  # Handling special case - when the item to remove is the head
            self.remove_first()
            return

        curr = self.head

        for i in range(index - 1): 
            if curr is None:
                return

            curr = curr.next

        if curr is not None and curr.next is not None:
            curr.next = curr.next.next

    def remove_first(self):
        if self.head is not None:
            self.head = self.head.next

    def remove_last(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return

        curr = self.head

        while curr.next.next is not None:
            curr = curr.next

        curr.next = None
    def remove(self, index):
        if index < 0:
            return

        if index == 0: 
            self.remove_first()
            return

        curr = self.head

        for i in range(index - 1):
            if curr is None:
                return

            curr = curr.next

        if curr is not None and curr.next is not None:
            curr.next = curr.next.next
            
            
    def size(self):
        curr = self.head

        length = 0
        while curr is not None:
            length += 1
            curr = curr.next

        return length

    def is_empty(self):
        return self.head is None

    def biggest(self):
        curr = self.head
        biggest = 0
        while curr is not None:
            if biggest < int(curr.item):
                biggest = int(curr.item)
            curr = curr.next
        return biggest
    
    def repeated(self):
        curr = self.head 
        if curr.next is None :
            return 
        while curr.next is not None: 
            if curr.item == curr.next.item:
                curr.next = curr.next.next
            curr = curr.next
    
    def bubblesort(self):
       counter  = 0 
       start = self.head
       first = self.head
       second = first.next
       while first.next is not None :
           if second is None :
               if counter == 0 :
                   
                   return 
           counter = 0
           if int(first.item) > int(second.item) :
               temp = second.item
               second.item = first.item
               first.item = temp
               counter += 1 
           if counter != 0: 
               first = start
               second = first.next
           else : 
               first = second
               second = first.next
    
    def solution1(self):
        curr = second = self.head
        while curr is not None:
            while second.next is not None:   
                if second.next.item == curr.item:
                    second.next = second.next.next
                else:
                    second = second.next
            curr = second = curr.next
    
    def solution2 (self): 
        self.bubblesort()
        self.repeated()
    
    def solution3(self):
        self.head = mergesort(self.head)
        self.repeated()
        
    def solution4(self):
        bool_array = [False] * (self.biggest()+1)
        curr = self.head
        while curr is not None:
            if bool_array[int(curr.item)] == True:
                self.remove(self.index_of(int(curr.item)))
            else:     
                bool_array[int(curr.item)] = True
            curr = curr.next
        return 
    
def mergesort(head):
    if head is None or head.next is None:
        return head
    l1, l2 = divide(head)
    l1 = mergesort(l1)
    l2 = mergesort(l2)
    head = merge(l1, l2)
    return head

def merge(l1, l2):
    temp = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if int(l1.item) <= int(l2.item):
        temp = l1
        temp.next = merge(l1.next, l2)
    else:
        temp = l2
        temp.next = merge(l1, l2.next)
    return temp
        
def divide(head):
    moving = head                     
    initial = head
    if moving is not None:
        initial = initial.next            
    while initial is not None:
        initial = initial.next            
        if initial is not None:
            initial = initial.next
            moving = moving.next
    mid = moving.next
    moving.next = None
    return head, mid
            



def read(LL):
    
    file = open("vivendi.txt", 'r') 
    file2 = open("activision.txt", 'r') 

    for i in file.read().split('\n'):
        LL.add_last(i)
        print(i)
    for i in file2.read().split ('\n'):
        LL.add_last(i)
        print(i)

def main():
    LL = LinkedList()
    read(LL)
    LL.solution1
    #LL.solution2()
    LL.print_list()
    LL.solution3()
    LL.print_list()
    LL.solution4()



if __name__ == "__main__":
    main()