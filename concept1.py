import Node_LL as m

def list_manipulation(llist):
    temp = llist.next.next
    temp.next.next.next = temp
    llist.next = temp.next
    print(llist.next.next.next.next.value)


llist = m.Linked_List()
llist.head = m.Node('a')
second = m.Node('b')
third = m.Node('c')
fourth = m.Node('d')
fifth = m.Node('e')
sixth = m.Node('f')
llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
list_manipulation(llist.head)
    
