# Benjamin Fullenkamp
# CSC6013
# In-class Exericse 1


class Node:
    def __init__(self, d):
        self.Data = d
        self.Next = None


class LinkedList:
    def __init__(self, d=None):
        if d == None:
            self.Header = None
            self.Current = None
        else:
            self.Header = Node(d)
            self.Current = self.Header

    def nextCurrent(self):
        """Change the Current to the next Node in the LinkedList"""

        if self.Current.Next is not None:
            self.Current = self.Current.Next
        else:
            self.Current = self.Header

    def resetCurrent(self):
        """Set the Current node to Header Node"""

        self.Current = self.Header

    def getCurrent(self):
        """Return the Data of the Current Node"""

        if self.Current is None:
            return None
        else:
            return self.Current.Data

    def insertBeginning(self, d):
        """Insert a node at the beginning of LinkedList"""

        if self.Header is None:
            self.Header = Node(d)
            self.Current = self.Header
        else:
            tmp = Node(d)
            tmp.Next = self.Header
            self.Header = tmp

    def insertCurrentNext(self, d):
        """Insert a Node next to the Current Node"""

        if self.Header is None:
            self.Header = Node(d)
            self.Current = self.Header
        else:
            tmp = Node(d)
            tmp.Next = self.Current.Next
            self.Current.Next = tmp

    def removeCurrentNext(self):
        """Remove the Node that the Current Node points to"""

        if self.Current.Next is None:
            return None
        else:
            ans = self.Current.Next.Data
            self.Current.Next = self.Current.Next.Next
            return ans

    def printList(self, msg="====="):
        """Print the Data of each Node and what the Current Node is"""

        p = self.Header
        print("====", msg)

        while p is not None:
            print(p.Data, end=" ")
            p = p.Next

        if self.Current is not None:
            print(f"Current: {self.Current.Data}")
        else:
            print("Empty Linked List")
        print("------------------------------------")


def main():
    # Create an empty LinkedList
    mylist = LinkedList()

    # Insert the 6 Integers to the List
    mylist.insertBeginning(91)
    mylist.insertBeginning(56)
    mylist.insertBeginning(34)
    mylist.insertBeginning(11)
    mylist.insertBeginning(88)
    mylist.insertBeginning(76)

    # Print out the Current status of the list
    mylist.printList("Adding 6 Integers to List")

    # Push the Current to the third element of the list
    mylist.resetCurrent()
    mylist.nextCurrent()
    mylist.nextCurrent()

    # Remove the Next to the Current element
    mylist.removeCurrentNext()

    # Insert 23 next to the Current element
    mylist.insertCurrentNext(23)

    # Print the Current status of the list
    mylist.printList(f"Current status of list after all operations")


main()
