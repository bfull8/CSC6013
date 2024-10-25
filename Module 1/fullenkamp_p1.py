# Benjamin Fullenkamp
# CSC6013 - Project 1


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
        """Insert a Node Next to the Current Node"""

        if self.Header is None:
            self.Header = Node(d)
            self.Current = self.Header
        else:
            tmp = Node(d)
            tmp.Next = self.Current.Next
            self.Current.Next = tmp

    def removeBeginning(self):
        """Remove Node from beginning of List"""

        if self.Header is None:
            return None
        else:
            ans = self.Header.Data
            self.Header = self.Header.Next
            self.Current = self.Header

            return ans

    def removeCurrentNext(self):
        if self.Current.Next is None:
            return None
        else:
            ans = self.Current.Next.Data
            self.Current.Next = self.Current.Next.Next

            return ans

    def printList(self, msg="====="):
        """Print the Data of each Data and what the Current Node is"""

        p = self.Header
        print("====", msg)

        while p is not None:
            print(p.Data, end=" ")
            p = p.Next

        if self.Current is not None:
            print(f"Current: {self.Current.Data}")
        else:
            print("Empty Linked List")
        print("-" * 75)


def main():

    # Create an array of the integers
    with open("Data.txt", "r") as file:
        a = []
        for line in file:
            a.append(int(line))

    # Sort the integer array
    a.sort()

    # Create empty LinkedList L
    L = LinkedList()

    # Insert each element into LinkedList, maintaining the order
    for num in a:
        L.insertCurrentNext(num)
        L.nextCurrent()
    L.resetCurrent()

    # Ask user for value x
    L.printList(f"Current Values in List")

    while True:
        try:
            x = int(input(">>Input an Integer Value: "))
            break
        except:
            print("Please enter an integer. Try again.")


    # First check for an empty list (should not happen but a safeguard)
    if L.Header is None:
       L.insertBeginning(x)
       L.printList(f"Inserted {x} at the beginning of list")
    else:
        # Search in LinkedList for value x
        # If value exists, remove it. If value does not exist, insert it
        while L.Current is not None:
            if L.Header.Data == x:  # Remove if the Header equals the input
                L.removeBeginning()
                L.printList(f"Removed {x} from list")
                break
            elif L.Header.Data > x:  # Insert at beginning if Header is greater
                L.insertBeginning(x)
                L.printList(f"Inserted {x} at the beginning of list")
                break
            elif L.Current.Next is None or L.Current.Next.Data > x:  # Insert next to Current if Current.Next is greater or it reaches end of list
                L.insertCurrentNext(x)
                L.printList(f"Inserted {x} next to {L.getCurrent()}")
                break
            elif L.Current.Next.Data == x:  # Remove the value if the Current.Next is equal to input
                L.removeCurrentNext()
                L.printList(f"Removed {x} from list")
                break
            else:
                L.nextCurrent()


main()
