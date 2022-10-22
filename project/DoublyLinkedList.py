#Doubly Linked List
#Node
class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev



class DLL:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


    #Insert a Node in the list at last position
    def insert(self, new_val):
        new_node = Node(new_val)

        #If empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        #If DLL has at least one element
        if self.head is not None:
            curr = self.head
            if curr.next is None:
                new_node.prev = curr
                curr.next = new_node
                self.tail = new_node
                return

            while(curr.next is not None):
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            self.tail = new_node
            return

    #Populate the list with a range
    def populate(self, ran):
        i = 0
        while(i<ran):
            self.insert(i)
            i+=1

    #Print the list
    def print_list(self):
        curr = self.head
        while(curr is not None):
            print(curr.val)
            curr = curr.next
    
    #Print list backwards
    def print_list_backwards(self):
        curr = self.tail
        while(curr is not None):
            print(curr.val)
            curr = curr.prev

    #Remove a given element from the list
    def remove(self, elem):
        #If it's first elem in list
        if self.head.val is elem:

            #If it's the only elem in list
            if self.tail.val is elem:
                self.head = None
                self.tail = None
                return

            #If there are more elements in the list
            if self.tail.val is not elem:
                curr = self.head
                self.head = self.head.next
                self.head.prev = None
                del(curr)
                return


       #If list has more than one elem
        trav1 = self.head
        trav2 = trav1.next

        while(trav2.val is not elem):
            trav1 = trav1.next
            trav2 = trav2.next
            if trav2.next is None and trav2.val is not elem:
                print('Val not found: '+str(elem))
                return


        #If element is last in list
        if trav2 is self.tail:
            trav1.next = None
            trav2.prev = None
            self.tail = trav1
            del(trav2)
            return

        #If middle of list
        temp = trav2
        trav2 = trav2.next
        trav1.next = trav2
        trav2.prev = trav1
        del(temp)
        return
    
def main():
    i = DLL()
    i.populate(10)
    i.print_list()
    i.remove(0)
    i.remove(5)
    i.remove(9)
    i.remove(11)
    print('\n\n\nAfter deletions')
    i.print_list()
    print('\n\n\n')
    i.print_list_backwards()

if __name__ == "__main__":
    main()
