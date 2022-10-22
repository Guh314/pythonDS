#!usr/bin/env python
#Heap implementation with arrays.

def left_child(index):
    return (index * 2) + 1
    
def right_child(index):
    return (index * 2) + 2

def insert(h = [], elem = None):
    h.append(elem)
    while(violate(h) is False):
        invariant(h)   

def poll(h):
    h[0], h[len(h)-1] = h[len(h)-1], h[0]
    ret = h[len(h)-1]
    h.remove(h[len(h)-1])
    while(violate(h) is False):
        invariant(h)
    return ret


def violate(h = []):
    for index, item in enumerate(h):
        try:
            if item > h[left_child(index)]:
                return False
            
            if item > h[right_child(index)]:
                return False
        except IndexError:
            pass
    return True
                
#Invariant being used is if child bigger
def invariant(h = []):
    for index, item in enumerate(h):
        try:
            if item > h[left_child(index)]:
                h[index], h[left_child(index)] = h[left_child(index)], h[index]

            if item > h[right_child(index)]:
                h[index], h[right_child(index)] = h[right_child(index)], h[index]
        except IndexError:
            pass

def heapsort(h):
    while h:
        i = poll(h)
        print(i)

heap = []
insert(heap, 10)
insert(heap, 2)
insert(heap, 30)
insert(heap, 4)
insert(heap, 50)
insert(heap, 6)
insert(heap, 77)
print(heap)
heapsort(heap)
