# Benjamin Fullenkamp
# CSC6013 - Project 1
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self, d=None):
        if d is None:
            self.Header = None
            self.Current = None
        else:
            self.Header = Node(d)
            self.Current = self.Header

    def insertNextCurrent(self, d):
        if self.Current is None:
            self.Header = Node(d)
            self.Current = self.Header
        else:
            tmp = Node(d)
            tmp.next = self.Current.next
            self.Current.next = tmp

    def nextCurrent(self):
        if self.Current.next is not None:
            self.Current = self.Current.next
        else:
            self.Current = self.Header

    def printList(self, msg="====="):
        """Print the data of each data and what the Current Node is"""

        p = self.Header
        print("====", msg)

        while p is not None:
            print(p.data, end=" ")
            p = p.next

        if self.Current is not None:
            print(f"Current: {self.Current.data}")
        else:
            print("Empty Linked List")
        print("-" * 75)

    def resetCurrent(self):
        self.Current = self.Header

    def removeCurrentNext(self):
        if self.Current.next == None:
            return None
        else:
            ans = self.Current.next.data
            self.Current.next = self.Current.next.next
        return ans

    def getCurrent(self):
        """Return the data of the Current Node"""

        if self.Current is None:
            return None
        else:
            return self.Current.data


def main():

    # Create an array of the integers
    with open("data.txt", "r") as file:
        a = []
        for line in file:
            a.append(int(line))

    # Sort the integer array
    a.sort()

    # Create empty LinkedList L
    L = LinkedList()

    # Insert each element into LinkedList, maintaining the order
    for num in a:
        L.insertNextCurrent(num)
        L.nextCurrent()
    L.resetCurrent()

    # Ask user for value x
    print(a)
    x = int(input(">>Input an Integer Value: "))

    # Search in LinkedList for value x
    # If value exists, remove it. If value does not exist, insert it
    while L.Current.data < x:
        if L.Current.next is None or L.Current.next.data > x:
            L.insertNextCurrent(x)
            L.printList(f"Inserted {x} next to {L.getCurrent()}")
        elif L.Current.next.data == x:
            L.removeCurrentNext()
            L.printList(f"Removed {x} from LinkedList")

        L.nextCurrent()


main()
