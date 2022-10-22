#Stack implementation through SLL
from SinglyLinkedList import Node

class Stack:
    def __init__(self, head = None):
        self.head = head

    #Push
    def push(self, new_stack):
        #If stack is empty
        if self.head is None:
            self.head = Node(new_stack)

        #If stack has a element
        else: 
            new_node = Node(new_stack)
            new_node.next = self.head
            self.head = new_node

    #Pop
    def pop(self):
        #If stack is empty
        if self.head is None:
            return None
        
        #If stack has at least one element
        else:
            popped_elem = self.head.val
            curr = self.head
            self.head = self.head.next
            del(curr)
            return popped_elem

    def populate(self, ran):
        i = 0
        while(i<ran):
            self.push(i)
            i = i+1

    def print_stack(self):
        curr = self.head
        while(curr is not None):
            print(curr.val)
            curr = curr.next


def main():
    print('\n\n\n\n')
    s = Stack()
    s.populate(10)
    s.print_stack()
    
if __name__ == "__main__":
    main()
