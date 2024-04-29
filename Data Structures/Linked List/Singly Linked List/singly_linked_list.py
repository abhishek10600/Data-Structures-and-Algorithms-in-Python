class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def insert_after(self, data, value):
        temp = self.head
        while temp is not None:
            if temp.data == value:
                break
            temp = temp.next
        if temp is None:
            print("Node not found in linked list")
        else:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node

    def insert_before(self, data, value):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == value:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.data != value:
            ptr = temp
            temp = temp.next
            if temp is None:
                print("Node is not found in linked list.")
                break
        if temp is not None:
            new_node = Node(data)
            new_node.next = ptr.next
            ptr.next = new_node

    def delete_head(self):
        if self.head is None:
            print("Linked list is empty. Cannot delete the head of an empty linked list.")
        else:
            temp = self.head
            self.head = self.head.next
            temp = None

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty.")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            ptr = temp.next
            while ptr.next is not None:
                temp = temp.next
                ptr = ptr.next
            temp.next = None

    def delete_node(self, value):
        if self.head is None:
            print("Cannot delete. Linked list is empty.")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.data != value:
            ptr = temp
            temp = temp.next
            if temp is None:
                print("Node is not present in node.")
                break
        else:
            ptr.next = temp.next
            temp = None

    def print_linkedlist(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next


ll = LinkedList()

# ll.insert_head(6)
# ll.insert_head(7)
# ll.insert_head(8)
# ll.insert_end(1)
# ll.insert_end(2)
# ll.insert_end(3)
# ll.insert_end(4)
# ll.insert_end(5)

# ll.insert_end(1)
# ll.insert_end(2)
# ll.insert_end(3)
# ll.insert_end(4)
# ll.insert_end(5)

# ll.print_linkedlist()

# ll.insert_after(6, 3)

# ll.print_linkedlist()

# ll.insert_after(6, 9)


# ll.insert_end(1)
# ll.insert_end(2)
# ll.insert_end(3)
# ll.insert_end(4)

# ll.print_linkedlist()

# ll.insert_before(6, 3)

# ll.print_linkedlist()


# ll.insert_end(1)
# ll.insert_end(2)
# ll.insert_end(3)
# ll.insert_end(4)
# ll.insert_end(5)

# ll.print_linkedlist()

# ll.delete_head()

# ll.print_linkedlist()

# ll.insert_end(1)
# ll.insert_end(2)
# ll.insert_end(3)
# ll.insert_end(4)
# ll.insert_end(5)

# ll.print_linkedlist()

# ll.delete_end()

# ll.print_linkedlist()

ll.insert_end(1)
ll.insert_end(2)
ll.insert_end(3)
ll.insert_end(4)

ll.print_linkedlist()

ll.delete_node(9)

# ll.print_linkedlist()
