import Node_LL as m

llist = m.Linked_List()
llist.head = m.Node(1)
second = m.Node(2)
third = m.Node(3)
fourth = m.Node(4)
fifth = m.Node(5)
llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

new = m.Node(100)
llist.insert_start(new)
llist.Traverse()

