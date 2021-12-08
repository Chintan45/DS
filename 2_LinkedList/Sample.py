
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    ### insert at beginning
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    """"print the linkedlist"""
    def print(self):
        if self.head is None:
            print("LinkedList is empty..")
            return
        
        itr = self.head
        listr = " "
        
        while itr:
            listr += str(itr.data) + "-->"
            itr = itr.next
        print(listr)
    
    ### insert at end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
    
    """" convert list to linkedlist """
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    """ get length """
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    """ remove el"""
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1
            
    """ insert at () value """
    def insert_at(self, index, data):
        if index<0  and index>self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr =  itr.next
            count+=1
    
    """ insert_after_value """
    def insert_after_value(self, data_after, data):
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data, self.head.next)
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
    
    """ remove by value"""
    def remove_by_value(self, data):
        if self.head==None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
       
    
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["Facebook", "Amazon", "Apple", "Netflix", "google","AWS"])
    ll.print()
    ll.remove_at(5)
    ll.print()
    print(ll.get_length())
    ll.remove_at(2)
    ll.print()
    ll.insert_at(0,"Apple")
    ll.print()
    
    print("---------------------------------------------------")
    
    ll2 = LinkedList()
    ll2.insert_values(["banana","mango","grapes","orange"])
    ll2.print()
    ll2.insert_after_value("mango","apple") # insert apple after mango
    ll2.print()
    ll2.remove_by_value("orange") # remove orange from linked list
    ll2.print()
    ll2.remove_by_value("figs")
    ll2.print()
    ll2.remove_by_value("banana")
    ll2.remove_by_value("mango")
    ll2.remove_by_value("apple")
    ll2.remove_by_value("grapes")
    ll2.print()
    pass