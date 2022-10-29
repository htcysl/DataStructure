class Linked_List_Node:
    def __init__(self,x):
        self.item = x
        self.next = None

class Linked_List_Seq:      
    def __init__(self) :      # O(1)
        self.head = None  
        self.size = 0 

    def __len__(self): return self.size    # O(1)

    def __iter__(self) :    # O(n) iter_seq 
        node = self.head            
        while node:
            yield node.item 
            node = node.next

    def build(self,x):                 # O(n)
        for a in reversed(x) :
            self.insert_first(a) 

    def get_at(self,i):               # O(i)
        node = self.head.leter_node(i) 
        return node.item         
        
    def set_at(self,i,x):             # O(i)
        node = self.head.later_node(i)   
        node.item = x 
    
    def insert_first(self,x):    # O(1)
        new_node = Linked_List_Node(x)   # ???
        new_node.next = self.head 
        self.head = new_node 
        self.size += 1 

    def delete_first(self):   # 
        x = self.head.item 
        self.head = self.head.next 
        self.size -= 1 
        return x
    
    def insert_at(self,i,x):
        if i==0 :
            self.insert_first(x) 
            return 
        new_node = Linked_List_Node(x)
        node = self.head.later_node(i-1) 
        x = node.next.item 
        node.next = node.next.next 
        self.size -= 1
        return x 

    def delete_at(self,i):     # O(i)
        if i==0 :
            return self.delete_first()
        node = self.head.later_node(i-1) 
        x = node.next.item 
        node.next = node.next.next 
        self.size -= 1 
        return x
          
    def insert_last(self,x) : return self.insert_at(len(self),x)     #O(n) 
    def delete_last(self,x) : return self.delete_at(len(self)-1)   # O(n)
 
                





















