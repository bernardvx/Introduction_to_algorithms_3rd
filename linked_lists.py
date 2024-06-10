class Node:
#Basic attributes of a node of a singly linked list
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_list:


    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node  = Node(data) 
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def delete(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return
        
        prev.next = temp.next
        temp = None


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next

        print('None')



singly_linked = Linked_list()

singly_linked.insert_at_begining(5)
singly_linked.insert_at_begining(4)
singly_linked.insert_at_end(3)
singly_linked.insert_at_begining(2)
singly_linked.insert_at_end(1)

singly_linked.print_list()
singly_linked.delete(3)

singly_linked.print_list()