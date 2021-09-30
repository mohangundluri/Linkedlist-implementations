""""Implementation of 'Singly linked list'."""


class Node:
    """creating node class"""
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        """Linked list traversal
        printing all node data"""
        n = self.head
        if n is None:
            print("Linked list is empty")
        else:
            while n is not None:
                print(n.data, end=" ")
                n = n.ref

    def add_begin(self, data):
        """adding element start of the linked list"""
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        """adding element end of the linked list"""
        new_node = Node(data)
        n = self.head
        if n is None:
            self.head = new_node
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        """adding element after the given node"""
        new_node = Node(data)
        n = self.head

        while n is not None:
            if n.data == x:
                break
            n = n.ref

        if n is None:
            print(f"{x} is not present in linked list")
        else:
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        """adding element before the given node"""
        new_node = Node(data)
        n = self.head
        if n is None:
            print(f"{x} is not present in the linked list")
        elif n.data == x:
            new_node.ref = n
            self.head = new_node
        else:
            while n is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            new_node.ref = n.ref
            n.ref = new_node

    def delete_begin(self):
        """Deleting first element of the linked list"""
        if self.head is None:
            print("linked list is empty to delete")
        else:
            self.head = self.head.ref

    def delete_end(self):
        """"Deleting end element of the linked list"""
        n = self.head
        if n is None:
            print("linked list is empty, we cant delete element at end")
        else:
            while n is not None:
                if n.ref.ref is None:
                    break
                n = n.ref
            n.ref = None

    def delete_node(self, x):
        """removing particular node in the given linked list"""
        if self.head is None:
            print("linked list is empty , we cant perform delete operation")
            return

        if x == self.head.data:
            self.head = self.head.ref
            return

        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref

        if n.ref is None:
            print(f"element {x} is not present")
        else:
            n.ref = n.ref.ref


ll = LinkedList()
ll.print_linked_list()