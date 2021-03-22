class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    # basic functions
    def traverse(self):
        if self.head is None:
            print("Empty")
            return
        cnode = self.head
        res = ""
        while cnode:
            res += str(cnode.data) + " > "
            cnode = cnode.next
        print(res)
        return

    def searching(self, ele):
        if self.head is None:
            print("Empty")
            return
        index = 0
        cnode = self.head
        while cnode:
            if cnode.data == ele:
                print(f"{ele} found at {index}")
                return
            cnode = cnode.next
            index += 1
        else:
            print(f"{ele} is not present in the list")
            return

    # reference functions
    def ref_to_last_node(self):
        if self.head is None:
            print("empty")
            return
        cnode = self.head
        while cnode.next:
            cnode = cnode.next
        print(f"Last node is {cnode.data}")
        return cnode

    def ref_to_second_last(self):
        if self.head is None:
            print("Empty")
            return
        cnode = self.head
        while cnode.next.next:
            cnode = cnode.next
        print("Second last node is ", cnode.data)
        return cnode

    def ref_to_node_data(self, ele):
        if self.head is None:
            print("empty")
            return
        cnode = self.head
        index = 0
        while cnode:
            if cnode.data == ele:
                break
            index += 1
            cnode = cnode.next
        else:
            print(f"{ele} not found")
            return
        print(f"Ref found for {ele} at index {index}")
        return

    def ref_to_predNode(self, ele):
        if self.head is None:
            print("Empty")
            return
        cnode = self.head
        if cnode.data == ele:
            print("Node present at 0th index")
            return None
        while cnode.next:
            if cnode.next.data == ele:
                print(f"Predecessor of {ele} is {cnode.data}")
                return cnode
            cnode = cnode.next
        else:
            print(f"{ele} is not present in the list")
        return

    def ref_to_node_pos(self, pos):
        if self.head is None:
            print("Empty")
            return
        cnode = self.head
        index = 0
        while cnode and index <= pos:
            if index == pos:
                print(f"{cnode.data}")
                return cnode
            index += 1
            cnode = cnode.next
        else:
            print(f"Index {pos} > len of list")

    # insertion functions

    def insert_at_start(self, data):
        if self.head is None:
            self.head = Node(data)
            return self.head

        cnode = self.head
        new_node = Node(data, cnode)
        self.head = new_node
        return self.head

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return self.head
        cnode = self.head
        while cnode.next:
            cnode = cnode.next
        cnode.next = Node(data)
        return

    def insert_after_pos(self, pos, data):
        if self.head is None and pos == 0:
            self.head = Node(data)
            return self.head
        elif pos < 0:
            print("-ve index")
            return
        cnode = self.head
        index = 0
        while cnode and index <= pos:
            if index == pos:
                new_node = Node(data)
                new_node.next = cnode.next
                cnode.next = new_node
                return
            cnode = cnode.next
            index += 1
        else:
            print(f"{pos} excedded the total length")
            return

    def insert_before_pos(self, pos, data):
        if self.head is None and pos == 0:
            self.insert_at_start(data)
            return
        cnode = self.head
        index = 0
        while cnode and index < pos:
            if index == pos - 1:
                new_node = Node(data)
                new_node.next = cnode.next
                cnode.next = new_node
                return
            cnode = cnode.next
            index += 1
        else:
            print(f"{pos} excedded the total length")
            return

    # deletion functions
    def delete_first_node(self):
        if self.head is None:
            print("Empty")
            return
        self.head = self.head.next
        return

    def delete_last_node(self):
        if self.head is None:
            print("Empty list")
            return
        cnode = self.head
        while cnode.next.next:
            cnode = cnode.next
        cnode.next = None
        return

    def delete_this_node(self, ele):
        if self.head is None:
            print("Empty")
            return
        cnode = self.head

        if cnode.data == ele and cnode.next is None:
            self.delete_first_node()
            return

        while cnode.next.next:
            if cnode.next.data == ele:
                cnode.next = cnode.next.next
            cnode = cnode.next
        else:
            if cnode.next.data == ele:
                cnode.next = None
                return
            else:
                print(f"{ele} is not present in the list")
                return


l = Linkedlist()
l.insert_at_start(10)
l.insert_at_start(30)
l.insert_at_start(50)
l.insert_at_start(60)
l.insert_at_start(70)
# l.traverse()
# l.searching(50)
# l.ref_to_last_node()
# l.ref_to_second_last()
# l.ref_to_node_data(50)
# l.ref_to_predNode(50)
# l.ref_to_node_pos(4)
# l.traverse()
l.insert_at_end(50)
l.insert_at_end(450)
# l.traverse()
l.insert_after_pos(1, 0)
# l.traverse()
l.insert_before_pos(8, 99)
l.delete_first_node()
l.delete_last_node()
l.traverse()
l.delete_this_node(10)
l.traverse()
