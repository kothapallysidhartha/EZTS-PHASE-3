class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(" -> ".join(nodes))

# Example usage:
llist = LinkedList()
llist.insert_at_end("7")
llist.insert_at_end(8)
llist.insert_at_end(5)
llist.insert_at_end(6)
llist.insert_at_end(9)
#llist.insert_at_beginning(0)
#llist.insert_at_end("akil")
llist.display()  # Output: 0 -> 1 -> 2
llist.delete_node(0)
llist.display()  # Output: 0 -> 2
