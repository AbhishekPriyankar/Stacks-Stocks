class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a node at the beginning of a
    # circular linked list
    def append(self, data):
        new_node = Node(data)
        temp = self.head

        new_node.next = self.head

        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = new_node

        else:
            new_node.next = new_node

        self.head = new_node

    def printList(self):
        temp = self.head
        if self.head is not None:
            while True:
                print (temp.data)
                temp = temp.next
                if temp == self.head:
                    break

circularList = CircularLinkedList()

circularList.append(10)
circularList.append(12)
circularList.append(21)
circularList.append(33)

print("Contents of a Circular Linked List")
circularList.printList()
