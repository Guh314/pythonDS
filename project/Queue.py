#Queue
#Implementing with Singly Linked List
from SinglyLinkedList import Node

class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    #Enqueue
    def enqueue(self, val):
        new_node = Node(val)
        #If Queue is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node

       #If Queue has at least one element
        else:
            curr = self.tail
            curr.next = new_node
            self.tail = curr.next
            

    #Dequeue
    def dequeue(self):
        #If there's only one element in Queue
        if self.head is self.tail:
            q = self.head
            self.head = None
            self.tail = None
            return q

        #If there's more than one element in the Queue
        else:
            curr = self.head
            self.head = curr.next
            curr = None
            del(curr)

    #Populate Queue
    def populate(self, ran):
        i = 0
        while(i<ran):
            self.enqueue(i)
            i = i+1

    #Print Queue
    def print_queue(self):
        curr = self.head
        while(curr is not None):
            print(curr.val)
            curr = curr.next

def main():
    q = Queue()
    q.populate(20)
    q.print_queue()

    print("\n\n")

    q.dequeue()
    q.dequeue()
    q.dequeue()
    
    q.print_queue()

if __name__ == "__main__":
    main()
