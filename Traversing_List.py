import Node_LL as ll


llist = ll.Linked_List()
llist.head = ll.Node(1)
second = ll.Node(2)
third = ll.Node(33)
fourth = ll.Node(23)
llist.head.next = second
second.next = third
third.next = fourth

llist.Traverse()
    
