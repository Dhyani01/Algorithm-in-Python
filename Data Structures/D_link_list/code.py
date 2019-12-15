from node import node


class doubly_linklist:

    def __init__(self):
        self.head=None

    def insertatbeg(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode

    def insertatlast(self,data):
        newnode=node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=newnode
        temp.prev=newnode
    def traverse(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next
