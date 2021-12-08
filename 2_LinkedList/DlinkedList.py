# -*- coding: utf-8 -*-
"""
    Doubly Linkedlist🔙⬅➡🔜
"""

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    """ insert at begnining """
    def insert_at_begining(self, data):
        if self.head == None:
            self.head = Node(data, self.head, None)
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
    
    """ insert at end"""
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)
            
    
    """ print forward """
    def print_forward(self):
        if self.head == None:
            print("Linked list is empty")
            return
        
        llstr = ""
        itr = self.head
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
    
    """ print backward"""
    def print_backward(self):
        if self.head == None:
            print("Linked list is empty")
            return
        
        llstr = ""
        last_node = self.get_last_node()
        itr = last_node
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.prev
        print("Link list in reverse: ", llstr)
            
    
    """ get last node"""
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    
    """ insert list"""
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            

if __name__ == "__main__":
    ll = DoublyLinkedList()
    
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.print_backward()