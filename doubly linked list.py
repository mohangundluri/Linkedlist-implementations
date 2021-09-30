"""Implementation of 'Doubly linked list'."""


class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None
        self.nref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        """printing data present in every node in forward direction 'Forward Traversal' """
        if self.head is None:
            print("Doubly linked list is empty, cant perform forward traversal")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ")
                n = n.nref

    def print_linked_list_reverse(self):
        """printing data present in every node in backward direction 'Backward Traversal' """
        if self.head is None:
            print("Doubly linked list is empty, cant perform reverse traversal")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, end=" ")
                n = n.pref

    def insert_when_empty(self, data):
        """Adding element to doubly linked list when doubly linked list is empty"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            print("Linked list is not empty")

    def add_begin(self, data):
        """Adding element to doubly linked list at start"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self, data):
        """Adding element to doubly linked list at end"""
        new_data = Node(data)
        n = self.head

        if self.head is None:
            self.head = new_data
        else:
            while n.nref is not None:
                n = n.nref

        n.nref = new_data
        new_data.pref = n

    def add_before(self, data, x):
        new_node = Node(data)
        if self.head is None:
            print(f"Linked list is empty and the {x} is not present in linked list")
        elif self.head == x:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                if n.nref == x:
                    break
                n = n.nref

            if n.nref is None:
                print(f"{x} is not present in linked list")
            else:
                new_node.nref = n.nref
                n.nref = new_node
                new_node.pref = n
                n.nref.pref = new_node



ll = LinkedList()

ll.add_begin(10)
ll.add_before(15, 10)
ll.print_linked_list_reverse()
print("\n")
ll.print_linked_list()