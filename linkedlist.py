# creating linkedlist class
class NodeList:
    def __init__(self,data):
        self.data=data
        self.next=None
    

    # insertion in linked list
    def insertionatbegin(self,data):
        p=NodeList(data)
        if self.head is None:
            self.head=p
            return
        else:
            p.next=self.head
            self.head=p
    
    # insertion at last
    def insertionatend(self,data):
        p=NodeList(data)
        if self.head is None:
            self.head=p
            return
        
        curr=self.head
        while(curr.next):
            curr=curr.next

        curr.next=p

    # insertion at specified position
    def insertatposition(self,data,pos):
        newnode=NodeList(data)
        curr=self.head
        if pos==1:
            self.insertionatbegin(data)
        else:
            p=p-2
            while(pos):
                curr=curr.next
                p-=1
            newnode.next=curr.next
            curr.next=newnode
    
    
            



