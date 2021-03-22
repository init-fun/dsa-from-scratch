class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("No node")
            return
        cnode = self.head
        while cnode:
            print(f"{cnode.data} ->")
            cnode = cnode.next

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

    def search(self, data):
        if self.head is None:
            print("List is empty/ Not found")
            return
        cnode = self.head
        index = 0
        while cnode:
            if cnode.data == data:
                print(f"Element {data} found at index {index}")
                break
            cnode = cnode.next
            index += 1

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
                print(f"found at index {index}")
                return
            cnode = cnode.next
            index += 1
        else:
            print("Not present in the list")

    def ref_to_predescessor(self, pred_of_this):
        if self.head is None:
            print("No node is present in the list")
            return
        cnode = self.head
        while cnode.next is not None:
            if cnode.next.data == pred_of_this:
                print(cnode.data)
                return
            cnode = cnode.next
        else:
            print("No pred for this node. returning none")
            return None

    def ref_to_particular_pos(self, pos=None, data=None):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        index = 0
        while cnode is not None and index <= pos:
            if index == pos or cnode.data == data:
                print(f"found at index {index}")
                return
            cnode = cnode.next
            index += 1
        else:
            print(f"{pos} related error.")
            return

    def insert_at_begining(self, data):
        self.head = Node(data, self.head)

    def insert_after_this(self, old_node, data):
        if self.head is None:
            print("No node")
            return
        cnode = self.head
        while cnode.next:
            if cnode.data == old_node:
                new_node = Node(data)
                new_node.next = cnode.next
                cnode.next = new_node
                return
            cnode = cnode.next
        else:
            print("Node is not present in the list")
            return

    def insert_before_this(self, old_node, data):
        if self.head is None:
            print("No node")
            return
        cnode = self.head
        prev_node = None
        if cnode.data == old_node:
            new_node = Node(data)
            new_node.next = cnode
            cnode = new_node
            return
        while cnode is not None:
            if cnode.data == old_node:
                new_node = Node(data)
                new_node.next = cnode
                prev_node.next = new_node
                return
            prev_node = cnode
            cnode = cnode.next
        else:
            print(f"Didn't found {old_node} in the list")
            return

    def insert_at_pos(self, pos, data):
        if pos == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        cnode = self.head
        index = 0
        while cnode is not None and index < pos - 1:
            cnode = cnode.next
            index += 1

        if cnode is None:
            print("you can only insert node at pos ", pos)
        else:
            new_node = Node(data)
            new_node.next = cnode.next
            cnode.next = new_node
            return

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        cnode = self.head
        while cnode.next:
            cnode = cnode.next
        cnode.next = Node(data, None)
        return

    def insert_in_empty_list(self, data):
        self.head = Node(data=new_data)
        return self.head

    def del_from_begining(self):
        if self.head is None:
            print("No node")
            return
        elif self.head.next is None:
            print("Deleting the only node")
            self.head = None
            return
        else:
            self.head = self.head.next
            return self.head

    def del_last_node(self):
        if self.head is None:
            print("zero node")
            return
        elif self.head.next is None:
            self.head = None
            return
        else:
            cnode = self.head
            while cnode.next:
                cnode = cnode.next
            cnode = None
            return


# working methods
# myLinkedList = LinkedList()
# myLinkedList.insert_at_begining(10)
# myLinkedList.insert_at_begining(4)
# myLinkedList.insert_at_end(170)
# myLinkedList.search(10)
# myLinkedList.del_from_begining()
# myLinkedList.ref_to_last_node()
# myLinkedList.ref_to_second_last()
# myLinkedList.ref_to_a_specific_node(5)
# myLinkedList.ref_to_predescessor(7)
# myLinkedList.ref_to_particular_pos(5)

# print("-------------------")
# myLinkedList.display()
# print("-------------------")

# a new list
myLinkedList = LinkedList()
myLinkedList.insert_at_end(0)
myLinkedList.insert_at_end(1)
myLinkedList.insert_at_end(2)
myLinkedList.insert_at_end(3)
myLinkedList.insert_at_end(4)
myLinkedList.insert_at_end(5)
myLinkedList.insert_at_end(6)
myLinkedList.insert_at_end(7)

myLinkedList.insert_after_this(4, 44)
# myLinkedList.display()
myLinkedList.insert_before_this(4, 33)
# myLinkedList.display()
myLinkedList.insert_at_pos(2, 5)
# myLinkedList.display()
print("-------------------")
myLinkedList.display()
print("-------------------")
myLinkedList.del_from_begining()
myLinkedList.display()
myLinkedList.del_last_node()
myLinkedList.display()