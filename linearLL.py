class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    llist = LinkedList()
    llist.head = Node(134)
    second = Node(345)
    third = Node(444)
    llist.head.next = second
    second.next = third
    llist.print()
