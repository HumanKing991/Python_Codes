import Node_LL as ll


for i in range(int(input())):
    if not i:
        llist = ll.Linked_List()
        llist.head = ll.Node(int(input()))
        temp = llist.head
        continue
    temp.next = ll.Node(int(input()))
    temp = temp.next

llist.Traverse()
    
