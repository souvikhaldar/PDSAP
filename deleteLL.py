class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	def push(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
	def delete(self,value):
		if self.head is not None:
			if self.head.data == value:
				self.head = self.head.next
				return
		temp = self.head
		while (temp is not None):
			if temp.data == value:
				break
			prev = temp
			temp = temp.next
		if temp is None:
			return
		prev.next = temp.next
		temp = None
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data)
			temp = temp.next
if __name__ == '__main__':
	ll = LinkedList()
	ll.push(1)
	ll.push(2)
	ll.push(5)
	ll.push(9)
	ll.push(4)
	ll.delete(5)
	ll.push(3)
	ll.printList()
