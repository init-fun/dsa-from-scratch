class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        res = ""
        while cnode:
            res += str(cnode.data) + "->"
            cnode = cnode.next
        print(res)

    def insert_at_begining(self, data):
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        cnode = self.head
        while cnode.next:
            cnode = cnode.next
        cnode.next = Node(data, None)
        return

    def search(self, data):
        if self.head is None:
            print("List is empty/ Not found")
            return
        cnode = self.head
        index = 0
        while cnode:
            if cnode.data == data:
                print(f"Found at index {index}")
                break
            cnode = cnode.next
            index += 1

    def insert_at_pos(self, data, pos):
        if self.head is None and pos == 1:
            self.head = Node(data, self.head)
            return

    def del_from_begining(self):
        if self.head is None:
            print("No node")
            return
        self.head = self.head.next
        return self.head

    def ref_to_last_node(self):
        if self.head is None:
            print("No node")
            return
        cnode = self.head
        while cnode.next is not None:
            cnode = cnode.next
        print(cnode.data)

    def ref_to_second_last(self):
        if self.head is None:
            print("No node")
            return
        cnode = self.head
        while cnode.next.next is not None:
            cnode = cnode.next
        print(cnode.data)

    def ref_to_a_specific_node(self, serach_this):
        if self.head is None:
            print("No node")
            return

        cnode = self.head
        index = 0
        while cnode is not None:
            if cnode.data == serach_this:
                print(f"found at {index}")
                break
            cnode = cnode.next
            index += 1
        else:
            print("Not present in the list")


myLinkedList = LinkedList()
# myLinkedList.display()
myLinkedList.insert_at_begining(10)
# myLinkedList.display()
myLinkedList.insert_at_begining(4)
# myLinkedList.display()
myLinkedList.insert_at_end(170)
myLinkedList.display()
myLinkedList.search(10)
myLinkedList.display()
myLinkedList.del_from_begining()
myLinkedList.ref_to_last_node()
myLinkedList.ref_to_second_last()
# recreating the list

myLinkedList.insert_at_begining(130)
# myLinkedList.display()
myLinkedList.insert_at_begining(44)
# myLinkedList.display()
myLinkedList.insert_at_end(15)

myLinkedList.display()
myLinkedList.ref_to_a_specific_node(18)