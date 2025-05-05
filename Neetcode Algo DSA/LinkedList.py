# defining a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# setting up constructor with just a head
class LinkedList:
    def __init__(self):
        self.head = None # initially the list is empty     

# traversing 
    def traverse(self):
        current = self.head # start from head
        while current:
            print(current.data, end=" -> ")
            current = current.next # move to the next node
        print("None")

# insert at beginning

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Step 5: Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Step 6: Delete a node by value
    def delete(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.next
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print(f"{data} not found in the list.")
            return

        prev.next = current.next

    # Step 7: Search for a value
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
