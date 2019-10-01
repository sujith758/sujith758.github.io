class Node(object):
    # Each node has data and a pointer that points to next node in the Linked List
    def __init__(self, data, next=None):
        self.data = data;
        self.next = next;

    # function to set data
    def setdata(self, data):
        self.data = data;

    # function to get data of a particular node
    def getdata(self):
        return self.data

    # function to set next node
    def setnext(self, next):
        self.next = next

    # function to get the next node
    def getnext(self):
        return self.next


class Linkedlist(object):
    # Defining the head of the linked list
    def __init__(self):
        self.head = None

    # printing the data in the linked list
    def printlinkedlist(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    # inserting the node at the beginning
    def insertatstart(self, data):
        if self.head == None:
            newnode = Node(data)
            self.head = newnode
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    # inserting at the end of linked list
    def insertatend(self, data):
        newnode = Node(data)
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = newnode


List = Linkedlist()
List.head = Node(1)
node2 = Node(2)
List.head.setnext(node2)
node3 = Node(3)
node2.setnext(node3)
List.insertatstart(4)
List.insertatend(19)
List.printlinkedlist()
print()
