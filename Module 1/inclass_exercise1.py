# Benjamin Fullenkamp

class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self, d = None):
        if (d == None):
            self.header = None
            self.current = None
        else:
            self.header = Node(d)
            self.current = self.header

    def insertBeginning(self, d):
        if self.header is None:
            self.header = Node(d)
            self.current = self.header
        else:
            tmp = Node(d)
            tmp.next = self.header
            self.header = tmp

    def printList(self, msg = "====="):
        p = self.header
        print("====",msg)

        while p is not None:
            print(p.data, end = " ")
            p = p.next
        
        if self.current is not None:
            print(f"Current: {self.current.data}")
        else:
            print("Empty Linked List")
        print("------------------------------------")
    
    def resetCurrent(self):
        self.current = self.header

    def nextCurrent(self):
        if self.current.next is not None:
            self.current = self.current.next
        else:
            self.current = self.header

    def getCurrent(self):
        if self.current is None:
            return None
        else:
            return self.current.data

    def removeCurrentNext(self):
        if self.current.next is None:
            return None
        else:
            ans = self.current.next.data
            self.current.next = self.current.next.next
            return ans

    def insertCurrentNext(self, d):
        if self.header is None:
            self.header = Node(d)
            self.current = self.header
        else:
            tmp = Node(d)
            tmp.next = self.current.next.next
            self.current.next = tmp

if __name__ == '__main__':
    mylist = LinkedList()
    mylist.printList("List Created")
    mylist.insertBeginning(91)
    mylist.insertBeginning(56)
    mylist.insertBeginning(34)
    mylist.insertBeginning(11)
    mylist.insertBeginning(88)
    mylist.insertBeginning(76)
    mylist.printList("The Current Status of the List")

    mylist.resetCurrent()
    mylist.printList("Resetting the Current")

    mylist.nextCurrent()
    mylist.nextCurrent()
    mylist.printList(f"Setting current to: {mylist.getCurrent()}")

    mylist.removeCurrentNext()
    mylist.printList(f"Removing next the Current")

    mylist.insertCurrentNext(23)
    mylist.printList(f"Inserting next the Current")

    



