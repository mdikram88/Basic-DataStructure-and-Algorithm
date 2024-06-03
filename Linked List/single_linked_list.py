from numpy import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    
    def get_head(self):
        return self.head

    
    def get_tail(self):
        if self.is_empty():
            return 
            
        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        return last_node

    
    def is_empty(self):
        return self.head == None
    
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last_node = self.get_tail()
        last_node.next = new_node

    
    def insert(self, data, index):
        
        if self.is_empty():
            self.append(data)
            return

        
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        i = 0
        cur_node = self.head
        
        while i < index - 1 and cur_node.next:
            cur_node = cur_node.next
            i += 1
            
        new_node.next = cur_node.next
        cur_node.next = new_node


    def delete_head(self):
        if self.is_empty():
            return 

        self.head = self.head.next


    def delete_tail(self):
        if self.is_empty():
            return

        i = 0
        cur_node = self.head

        while cur_node.next.next:
            cur_node = cur_node.next

        cur_node.next = None

    
    def delete_at(self, index):
        if self.is_empty():
            raise IndexError

        if index == 0:
            return self.delete_head()
        
        i = 0
        cur_node = self.head

        while i < index - 1 and cur_node.next.next:
            cur_node = cur_node.next
            i += 1

        if i != index - 1:
            raise IndexError

        cur_node.next = cur_node.next.next
        

    def transverse_from(self, index):
        i = 0
        
        cur = self.head
        
        while i < index and cur.next:
            cur = cur.next
            i += 1

        if i != index:
            raise IndexError
            

        return self.__str__(cur)

    def transverse_till(self, index):
        i = 0

        cur = self.head

        while i < index and cur.next:
            cur = cur.next
            i += 1

        if i != index:
            raise IndexError

        return self.__str__(self.head, end=index)
    
            
    def __str__(self, cur_node=None, end=None):
        if self.is_empty():
            return ""

        if not cur_node:
            cur_node = self.head

        i = 0
        st = ""
        while cur_node.next:
            st += str(cur_node.data) + "->"
            cur_node = cur_node.next
            i += 1
            
            if end and i == end:
                break

        st += str(cur_node.data)
        return st


lt = LinkedList()
lt.append(1)
lt.append(2)
lt.append(3)
lt.append(4)

print(lt.transverse_from(2))
# num = int(input("Enter the size of Linked List you want: "))

# for ele in random.randint(1, 100, size=num):
#     lt.append(ele)


print(lt)