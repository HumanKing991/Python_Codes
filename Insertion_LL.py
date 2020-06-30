import Node_LL as m




for i in range(int(input())):
    if not i:
        llist = m.Linked_List()
        llist.head = m.Node(int(input()))
        temp = llist.head
        continue
    temp.next = m.Node(int(input()))
    temp = temp.next
    


new = m.Node(100)
llist.insert_start(new)
new1 = m.Node(200)
llist.insert_end(new1)
new2 = m.Node(300)
llist.insert_random(new2, 3)
llist.Traverse()
