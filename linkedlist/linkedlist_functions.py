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

    def bubble_sort(self):
        if self.head is None:
            print("empty")
            return
        end_node = None
        while self.head.next is not end_node:
            cnode = self.head
            while cnode.next is not end_node:
                next_node = cnode.next
                if cnode.data > next_node.data:
                    cnode.data, next_node.data = next_node.data, cnode.data

                cnode = cnode.next

            end_node = cnode

    def reverse(self):
        if self.head is None or self.head.next is None:
            return self.head

        prev_node = None
        cnode = self.head
        while cnode:
            next_node = cnode.next
            cnode.next = prev_node
            prev_node = cnode
            cnode = next_node
        self.head = prev_node

    def merge_them(self, second_list):
        new_list = Linkedlist()
        new_list.head = self.merge_two_list(self.head, second_list.head)
        return new_list

    def merge_two_list(self, first, second):
        # compare the first node of both the lists and assign to the head of the third list
        if first.data <= second.data:
            new_node = Node(first.data)
            first = first.next
        else:
            new_node = Node(second.data)
            second = second.next

        third_list = new_node

        # go through both of the list
        while first and second:
            if first.data <= second.data:
                third_list.next = Node(first.data)
                first = first.next
            else:
                third_list.next = Node(second.data)
                second = second.next
            third_list = third_list.next

        # if first list still has some nodes
        while first:
            third_list.next = Node(first.data)
            first = first.next
            third_list = third_list.next

        while second:
            third_list.next = Node(second.data)
            second = second.next
            third_list = third_list.next

        return new_node

    # practice round
    def merge_them2(self, second_list):
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
            second = second.data
            third_list = third_list.next

        return new_node

    # end of practice
    def merge_by_swaping_links(self, second_list):
        new_list = Linkedlist()
        new_list.head = self.merge_by_links(self.head, second_list.head)
        return new_list

    def merge_by_links(self, first, second):
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

    def insert_cycle_at(self, data):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        cycle_ptr = None
        prev_node = None

        while cnode:
            if cnode.data == data:
                cycle_ptr = cnode
            prev_node = cnode
            cnode = cnode.next
        if cycle_ptr:
            prev_node.next = cycle_ptr
        else:
            return f"{data} is not present in the list"

    def has_cycle(self):
        if self.find_cycle():
            return True
        return False

    def find_cycle(self):
        if self.head is None or self.head.next is None:
            return None

        fptr = self.head
        sptr = self.head
        while fptr and sptr.next:
            if fptr == sptr:
                # print("Has cycle")
                return fptr
            fptr = fptr.next
            sptr = sptr.next.next
        else:
            # print("No cycle present")
            return None

    def remove_cycle(self):
        cyclic_node = self.find_cycle()
        if cyclic_node is None:
            print("No cycle")
            return
        print(f"Cycle detected at {cyclic_node.data}")

        fptr = cyclic_node
        sptr = cyclic_node

        len_cycle = 0

        while True:
            len_cycle += 1
            sptr = sptr.next
            if fptr == sptr:
                break
        print("Length of the cycle is ", len_cycle)

        len_rem_list = 0
        fptr = self.head
        while fptr is not sptr:
            len_rem_list += 1
            fptr = fptr.next
            sptr = sptr.next

        print("Node not in cycle", len_rem_list)
        total_node = len_cycle + len_rem_list
        print("Total nodes : ", total_node)

        fptr = self.head
        for i in range(len(total_node) - 1):
            fptr = fptr.next
        fptr.next = None


myLinkedlist = Linkedlist()
myLinkedlist.insert_at_start(60)
myLinkedlist.insert_at_start(545)
myLinkedlist.insert_at_start(22)
myLinkedlist.insert_at_start(435)
# myLinkedlist.insert_at_start(430)
# myLinkedlist.insert_at_start(103)
# myLinkedlist.traverse()
myLinkedlist.bubble_sort()
# myLinkedlist.traverse()
myLinkedlist.reverse()

# myLinkedlist.traverse()

myLinkedlist1 = Linkedlist()
myLinkedlist1.insert_at_start(60)
myLinkedlist1.insert_at_start(545)
myLinkedlist1.insert_at_start(22)
myLinkedlist1.insert_at_start(435)
myLinkedlist1.bubble_sort()


myLinkedlist2 = Linkedlist()
myLinkedlist2.insert_at_start(40)
myLinkedlist2.insert_at_start(55)
myLinkedlist2.insert_at_start(23)
myLinkedlist2.insert_at_start(5)
myLinkedlist2.bubble_sort()
print("two sorted list")
myLinkedlist1.traverse()
myLinkedlist2.traverse()
# print("after mergeing")

# print("by swapping data")
# new_list = myLinkedlist1.merge_them2(myLinkedlist2)


print("By swapping links")
new_list = myLinkedlist1.merge_by_swaping_links(myLinkedlist2)
new_list.traverse()