#LINKED LIST BASIC
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class ll:
    def __init__(self):
        self.head=None
    
    #add a node in the beginning
    def add_f(self,data):
        new=node(data)
        if self.head is None:
            self.head=new
            return
        new.next=self.head
        self.head=new
    
    #add a node at last
    def add_l(self,data):
        new=node(data)
        if self.head is None:
            self.head=new
            return
        n=self.head
        while n.next:
            n=n.next
        n.next=new



    #add a node after some node X-is node whic is present
    def add_after(self,data,x):
        new=node(data)
        if self.head==None:
            print("ll is empty")
            return
        n=self.head
        while n:
            if n.data==x:
                break
            n=n.next
        else:
            print("node is not present")
            return
        if not n.next:
            n.next=new
        else:
            new.next=n.next
            n.next=new

    #add a node before some node X-is node whic is present
    def add_before(self,data,x):
        new=node(data)
        if self.head==None:
            print("ll is empty")
            return
        if x==self.head.data:
            new.next=self.head
            self.head=new
            return
        n=self.head
        while n.next:
            if n.next.data==x:
                break
            n=n.next
        else:
            print("node is not present")
            return
        new.next=n.next
        n.next=new

    #deletes the first node
    def del_f(self):
        if not self.head:
            print("nothing to delete")
            return
        if not self.head.next:
            self.head=None
            return
        self.head=self.head.next

    #deletes the last node
    def del_l(self):
        if not self.head:
            print("nothing to delete")
            return
        if not self.head.next:
            self.head=None
            return
        n=self.head
        while n.next.next:
            n=n.next
        n.next=None

    #deletes node by value    
    def delval(self,x):
        if not self.head:
            print("nothing to delete")
            return
        if self.head.data==x:
            if not self.head.next:
                self.head=None
            else:
                self.head=self.head.next
            return
        n=self.head
        while n.next:
            if n.next.data==x:
                if n.next.next is None:
                    n.next=None
                else:
                    n.next=n.next.next
                break
            n=n.next
        else:
            print("theres no node like that")


    #prints all nodes of the linkedlist
    @property
    def traversal(self):
        if self.head==None:
            print("no items")

        n=self.head
        while n:
            print(n.data,end=" ")
            n=n.next




#testing
l1=ll()
l1.add_f(20)
l1.add_l(45)
l1.add_f(10)
l1.add_after(30,10)
l1.add_before(40,30)
l1.del_f()
l1.delval(45)
l1.traversal