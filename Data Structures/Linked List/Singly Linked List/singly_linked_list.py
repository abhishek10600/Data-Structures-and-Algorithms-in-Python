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

    def print_linkedlist(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next


ll1 = LinkedList()
ll1.insert_head(1)
ll1.insert_head(2)
ll1.insert_head(3)
ll1.insert_head(4)
ll1.insert_head(5)

ll2 = LinkedList()

ll1.print_linkedlist()
ll2.print_linkedlist()
