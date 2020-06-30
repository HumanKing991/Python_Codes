class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def Traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def insert_start(self,new):
        new.next = self.head
        self.head = new

    def insert_end(self,new):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def insert_random(self, new, position):
        temp = self.head
        while temp.value != position:
            temp = temp.next
        new.next = temp.next
        temp.next = new
            
        
        
        
        
