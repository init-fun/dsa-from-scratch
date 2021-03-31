class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        cnode = self.head
        while cnode:
            print(f"{cnode.data} > ", end="")
            cnode = cnode.next
        print()

    def search(self, data):
        if self.head is None:
            print("List is empty")
            return
        cnode = self.head
        index = 0
        while cnode:
            if cnode.data == data:
                print(f"{data} found at {index}")
                return
            cnode = cnode.next
        else:
            print(f"{data} is not in the list")

    def insert_at_start(self, new_data):
        if self.head is None:  # no node is present in the list
            self.head = Node(new_data)
            return
        cnode = self.head
        new_node = Node(new_data)
        new_node.next = cnode
        cnode.prev = new_node
        self.head = new_node
        return

    def insert_at_end(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        cnode = self.head
        while cnode.next:
            cnode = cnode.next

        new_node = Node(new_data)

        new_node.prev = cnode
        cnode.next = new_node
        return

    def insert_after_the_node(self, data, new_data):
        if self.head is None:
            print("List is empty")
            return

        cnode = self.head
        while cnode:
            if cnode.data == data:
                break
            cnode = cnode.next

        if cnode is None:
            print(f"{data} is not in the list")
            return
        else:
            # we have the ref the node after which we have to insert the new node

            new_node = Node(new_data)
            new_node.prev = cnode
            new_node.next = cnode.next
            if cnode.next:
                cnode.next.prev = new_node
            cnode.next = new_node

    def insert_before_the_node(self, data, new_data):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:  # only one node
            new_node = Node(new_data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        # get the ref to the node before which we need to insert a new node
        cnode = self.head
        while cnode:
            if cnode.data == data:
                break
            cnode = cnode.next

        if cnode is None:
            print(f"{data} is not present in the list")
            return
        else:
            new_node = Node(new_data)

            new_node.prev = cnode.prev
            new_node.next = cnode

            cnode.prev.next = new_node
            cnode.prev = new_node

        return

    def delete_first_node(self):
        if self.head is None:
            print("Node is empty")
            return

        self.head = self.head.next
        self.head.prev = None

    def delete_only_node(self):
        self.head = None
        return

    def delete_last_node(self):
        if self.head is None:
            print("List is empty")
            return
        # only one node
        if self.head.next is None:
            self.head = None
            return

        # more than one node
        cnode = self.head
        while cnode.next:
            cnode = cnode.next
        cnode.prev.next = None
        return
