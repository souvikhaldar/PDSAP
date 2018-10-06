class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def isempty(self):
        return True if self.head == None else False
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.isempty():
            return "stack empty"
        temp = self.head
        self.head = self.head.next
        return temp.data
    def printStack(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
if __name__=='__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.printStack()
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    stack.printStack()
