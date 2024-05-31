class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(" -> ".join(nodes))

    def detect_and_remove_cycle(self):
        if not self.head or not self.head.next:
            return

        slow = self.head
        fast = self.head

        # Detect cycle using Floyd's Cycle Detection Algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # If no cycle is found
        if slow != fast:
            return

        # Find the start of the cycle
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Remove the cycle
        while fast.next != slow:
            fast = fast.next
        fast.next = None

def main():
    llist = LinkedList()
    
    while True:
        print("\nOptions:")
        print("1. Insert at end")
        print("2. Display list")
        print("3. Create cycle for testing")
        print("4. Detect and remove cycle")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter data to insert: "))
            llist.insert_at_end(data)
        elif choice == 2:
            llist.display()
        elif choice == 3:
            pos = int(input("Enter position to link the last node to (0-based index): "))
            current = llist.head
            cycle_node = None
            index = 0
            while current.next:
                if index == pos:
                    cycle_node = current
                current = current.next
                index += 1
            current.next = cycle_node
        elif choice == 4:
            llist.detect_and_remove_cycle()
            print("Cycle detected and removed if it existed.")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
