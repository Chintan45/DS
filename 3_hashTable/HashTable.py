

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None]*(self.MAX)
    
    """ hash function """
    def get_hash(self,key):
        h=0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        




if __name__=='__main__':
    t = HashTable()
    
    t['march 6'] = 130
    print(t['march 6'])
    
    del t['march 6']
    print(t['march 6'])