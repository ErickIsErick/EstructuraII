from Node import Node

class LinkedList: 
    def __init__(self): 
        self.head = None 

    def insert_at_beginning(self, data):
       new_node = Node(data) # { data: 40, next: null } -> { data: 20, next: null }
       new_node.next = self.head # { data: 40, next: null} -> { data: 20, next: null}
       self.head = new_node 
       # { data: 60, next: { data: 40, next: { data: 20, next: { data: 100, next: null}}}}



    def mostrar(self):
        actual = self.head
        while actual:
            print(actual.data, end=" -> ")
            actual = actual.next
        print("None")

    def revertir(self):
        prev = None
        current = self.head
        print(current)
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def del_matching_nodes(self, key):
        actual = self.head
        if self.head.data == key:
            self.head = self.head.next
            return
            
        actual = self.head
        while actual:
            if actual.data == key:
                break
            previous = actual
            actual = actual.next
        if actual is None:
            print('Deletion Error: Key not found.') 
        else:
            previous.next = actual.next

    def maxElement(self):
        count = 0
        current = self.head
        while current:
            if current.data > count:
                count = current.data
            current = current.next
        return count