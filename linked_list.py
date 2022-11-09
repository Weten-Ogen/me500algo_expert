class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

class LinkedList:
    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new(self, new_data):




