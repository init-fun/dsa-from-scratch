class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("Empty")
            return
        cnode = self.head
        while cnode:
            print(f"{cnode.data} >", end=" ")
            cnode = cnode.next
        print()
        return

    def insert_at_start(self, data):
        if self.head is None:
            self.head = Node(data)
            return self.head
        cnode = self.head
        new_node = Node(data, cnode)
        self.head = new_node
        return self.head

    def reverse(self):
        prev_node = None
        cnode = self.head
        while cnode:
            next_node = cnode.next
            cnode.next = prev_node
            prev_node = cnode
            cnode = next_node
        self.head = prev_node

    def bubble_sort(self):
        if self.head is None or self.head.next is None:
            return self.head

        end_node = None
        while self.head.next is not end_node:
            cnode = self.head
            while cnode.next is not end_node:
                next_node = cnode.next
                if cnode.data > next_node.data:
                    # swap the data
                    cnode.data, next_node.data = next_node.data, cnode.data

                cnode = cnode.next
            end_node = cnode

    def merge_them(self, second_list):
        new_list = Linkedlist()
        new_list.head = self.merge2in1(self.head, second_list.head)
        return new_list

    def merge2in1(self, first, second):
        if first.data <= second.data:
            new_node = Node(first.data)
            first = first.next
        else:
            new_node = Node(second.data)
            second = second.next

        third_list = new_node

        while first and second:
            if first.data <= second.data:
                third_list.next = Node(first.data)
                first = first.next
            else:
                third_list.next = Node(second.data)
                second = second.next
            third_list = third_list.next

        while first:
            third_list.next = Node(first.data)
            first = first.next
            third_list = third_list.next

        while second:
            third_list = Node(second.data)
            second = second.next
            third_list = third_list.next

        return new_node

    def merge_by_swapping_links(self, second_list):
        new_list = Linkedlist()
        new_list.head = self.swap_links(self.head, second_list.head)
        return new_list

    def swap_links(self, first, second):
        if first.data <= second.data:
            ptr = first
            first = first.next
        else:
            ptr = second
            second = second.next

        third_list = ptr

        while first and second:
            if first.data <= second.data:
                third_list.next = first
                third_list = third_list.next
                first = first.next

            else:
                third_list.next = second
                third_list = third_list.next
                second = second.next

        if first:
            third_list.next = first
        else:
            third_list.next = second

        return ptr


myLinkedlist1 = Linkedlist()
myLinkedlist1.insert_at_start(60)
myLinkedlist1.insert_at_start(545)
myLinkedlist1.insert_at_start(22)
myLinkedlist1.insert_at_start(435)
# myLinkedlist1.traverse()


myLinkedlist2 = Linkedlist()
myLinkedlist2.insert_at_start(40)
myLinkedlist2.insert_at_start(55)
myLinkedlist2.insert_at_start(23)
myLinkedlist2.insert_at_start(5)
myLinkedlist2.reverse()
# myLinkedlist2.traverse()

myLinkedlist1.bubble_sort()
myLinkedlist2.bubble_sort()
print("Befor megeing")
myLinkedlist2.traverse()
myLinkedlist1.traverse()
print("after merging")
# tmp = myLinkedlist1.merge_them(myLinkedlist2)
tmp = myLinkedlist1.merge_by_swapping_links(myLinkedlist2)
tmp.traverse()