#Singly Linked List
#Node

class SLL:

    class Node:
        def __init__(self, val=None, next=None):
            self.val = val
            self.next = next

        def get_val(self):
            return self.val
    
        def set_val(self, new_val):
            self.val = new_val

        def get_next(self):
            return self.next

        def set_next(self, new_next):
            self.next = new_next

        def has_next(self):
            if self.next: return True
            return False

        def get_last(self):
            def __get_last(head):
                if head.get_next():
                    __get_last(head.get_next())
                return head
            new_curr = __get_last(self.next)
            return new_curr
                
                    

        def __iter__(self):
            if self.has_next():
                for elem in self.next:
                    yield elem
            yield self.val

    def __init__(self, head=None):
        self.head = head


    def append(self, elem):
        def __append(head, elem):
            #If head is None
            if head is None:
                print(f'appended {elem}')
                return SLL.Node(elem)

            #If head is not None
            head.set_next(__append(head.get_next(), elem))

            #Return head
            return head

        self.head = __append(self.head, elem)

                
    def print_lst(self):
        def __print_lst(head):
            if head == None: return
            print(head.get_val())
            __print_lst(head.next)
            return
        __print_lst(self.head)            


    def delete(self, elem):
        def __find(head, elem):
            print(f'seaching {elem}')
            if head is None: return None

            if head.get_val() == elem:
                return head
            return __find(head.get_next(), elem)

        def __delete(head, elem):
            if head != None:
                print(f'Deleting {head.get_val()}')
                if head.has_next() == False:
                    del(head)
                    return
                new_head = head.get_last()
                head.set_val(new_head.get_val())
                new_elem = __find(head.get_next(), head.get_val())
                return __delete(new_elem, head.get_val())

        node_to_delete = __find(self.head, elem)
        if node_to_delete == None:
            return 
        self.head = __delete(self.head, elem)

    #Will print lst backwards.
    def __iter__(self):
        if self.head != None:
            return self.head.__iter__()
        else:
            return [].__iter__()

def main():
    lst = SLL()
    for x in range(10):
        lst.append(x)

    lst.print_lst()

    lst.delete(4)
    lst.delete(3)
    lst.delete(9)
    #lst.delete(0)

    lst.print_lst()

if __name__ == "__main__":
    main()
