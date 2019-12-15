from node import node


class Link__list:
    def __init__(self):
        self.head=None

    def insertatBeg(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode


    def insertatlast(self,data):
        newnode=node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=newnode


    def traverse(self):
        if self.head is None:
            print("No elements in list")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head=self.head.next
