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
ll.insert_end(1)
ll.insert_end(2)
ll.insert_end(3)
ll.insert_end(4)
ll.insert_end(5)


ll.print_linkedlist()
