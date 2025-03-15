# class Node
#
# Instance variables:
#    Data - the value
#    Next - the next node

class Node:
    def __init__(self, d):
        self.Data = d
        self.Next = None

class LinkedList:
    def __init__(self, d=None):
        if (d == None): # an empty list
            self.Header = None
            self.Current = None
        else:
            self.Header = Node(d)
            self.Current = self.Header
    def nextCurrent(self):
        if (self.Current.Next is not None):
            self.Current = self.Current.Next
        else:
            self.Current = self.Header
    def resetCurrent(self):
        self.Current = self.Header
    def getCurrent(self):
        if (self.Current is not None):
            return self.Current.Data
        else:
            return None
    def insertBeginning(self, d):
        if (self.Header is None): # if list is empty
            self.Header = Node(d)
            self.Current = self.Header
        else:                     # if list not empty
            Tmp = Node(d)
            Tmp.Next = self.Header
            self.Header = Tmp
    def insertCurrentNext(self, d):
        if (self.Header is None): # if list is empty
            self.Header = Node(d)
            self.Current = self.Header
        else:                     # if list not empty
            Tmp = Node(d)
            Tmp.Next = self.Current.Next
            self.Current.Next = Tmp
    def removeBeginning(self):
        if (self.Header is None): # if list is empty
            return None
        else:                     # if list not empty
            ans = self.Header.Data
            self.Header = self.Header.Next
            self.Current = self.Header
            return ans
    def removeCurrentNext(self):
        if (self.Current.Next is None): # if there is no node
            return None                 #        after Current
        else:                           # if there is
            ans = self.Current.Next.Data
            self.Current.Next = self.Current.Next.Next
            return ans

    def swap(self):
        if (self.Current.Next is None or self.Header is None):
            return -1
        else:

            # Nodes to swap
            current_next = self.Current.Next
            current_next_next = current_next.Next

            # Iterate until node before current node
            prev = self.Header
            while prev.Next != self.Current:
                prev = prev.Next

            # Current Node's Previous Swaps to Current_next
            prev.Next = current_next

            # Current node is now going to point to the next node that it swapped with
            self.Current.Next = current_next_next

            # Current_next is points to old current
            current_next.Next = self.Current

            return 0

    def printList(self,msg="====="):
        p = self.Header
        print("====",msg)
        while (p is not None):
            print(p.Data, end=" ")
            p = p.Next
        if (self.Current is not None):
            print("Current:", self.Current.Data)
        else:
            print("Empty Linked List")
        input("----------------")


def main():
    mylist = LinkedList()
    mylist.insertBeginning(70)
    mylist.insertBeginning(60)
    mylist.insertBeginning(50)
    mylist.insertBeginning(40)
    mylist.insertBeginning(20)
    mylist.nextCurrent()
    mylist.nextCurrent()
    mylist.nextCurrent()
    print(mylist.swap())
    mylist.printList()

main()
