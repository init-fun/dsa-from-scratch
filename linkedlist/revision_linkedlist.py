class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    # assuming the list is not empty
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        while cnode:
            print(f"{cnode.data} > ", end="")
            cnode = cnode.next
        print()
        return

    def search(self, ele):
        if self.head is None:
            return None
        cnode = self.head
        index = 0
        while cnode:
            if cnode.data == ele:
                print(f"{ele} found at {index}")
                return
            cnode = cnode.next
            index += 1
        else:
            print(f"{ele} is not present in the list")
            return

    def ref_to_last_node(self):
        if self.head is None:
            return None
        cnode = self.head
        while cnode.next:
            cnode = cnode.next
        print(f"End node is {cnode.data}")
        return

    def ref_to_second_last_node(self):
        if self.head is None:
            return None
        cnode = self.head
        if cnode.next is None:
            return None

        while cnode.next.next:
            cnode = cnode.next
        print(f"Second last node is {cnode.data}")
        return

    def ref_to_this_node_data(self, ele):
        if self.head is None:
            return None
        cnode = self.head
        index = 0
        while cnode:
            if cnode.data == ele:
                print(f"{ele} is present at {index}")
                return
            cnode = cnode.next
            index += 1

        else:
            print(f"{ele} is not present in the list")
            return

    def ref_to_pred_node(self, ele):
        if self.head is None:
            return None
        cnode = self.head
        if cnode.data == ele:
            print(f"pred of {ele} is {None}")
            return
        prev_node = None
        while cnode:
            if cnode.data == ele:
                print(f"pred node of {ele} is {prev_node.data}")
                return
            prev_node = cnode
            cnode = cnode.next
        else:
            print(f"{ele} is not present in the list")
            return

    def ref_to_node_at_pos(self, pos):
        if self.head is None:
            return None
        cnode = self.head
        index = 0
        while cnode and index <= pos:
            if pos == index:
                print(f"At {pos} -> {cnode.data}")
                return
            cnode = cnode.next
            index += 1
        else:
            print(f"{pos} is out of range")
            return

    def insert_at_start(self, ele):
        if self.head is None:
            self.head = Node(ele)
            return self.head
        cnode = self.head
        new_node = Node(ele, cnode)
        self.head = new_node
        return self.head

    def insert_at_end(self, ele):
        if self.head is None:
            self.head = Node(ele)
            return self.head
        cnode = self.head
        while cnode.next:
            cnode = cnode.next
        cnode.next = Node(ele)
        return

    def insert_before_this(self, target_node, data):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        # first node
        if cnode.data == target_node and cnode.next is None:
            self.insert_at_start(data)
            return
        while cnode.next:
            if cnode.next.data == target_node:
                new_node = Node(data, cnode.next)
                cnode = new_node
                return
            cnode = cnode.next
        else:
            print(f"{target_node} is not present in the list")
            return


myLinkedlist = Linkedlist()
myLinkedlist.insert_at_start(90)
myLinkedlist.insert_at_start(100)
myLinkedlist.insert_at_start(42)
myLinkedlist.insert_at_start(99)
myLinkedlist.insert_at_start(54)
myLinkedlist.insert_at_start(60)
# myLinkedlist.traverse()
# myLinkedlist.search(42)

# myLinkedlist.ref_to_last_node()
# myLinkedlist.ref_to_second_last_node()
# myLinkedlist.ref_to_this_node_data(42)
# myLinkedlist.ref_to_pred_node(90)
# myLinkedlist.ref_to_node_at_pos(0)
# myLinkedlist.ref_to_node_at_pos(3)
# myLinkedlist.ref_to_node_at_pos(5)
# myLinkedlist.ref_to_node_at_pos(6)

myLinkedlist.insert_at_end(236)
myLinkedlist.insert_at_end(456)
myLinkedlist.insert_at_end(746)
myLinkedlist.traverse()
myLinkedlist.insert_before_this(456, 4564)
myLinkedlist.traverse()
