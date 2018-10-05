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

	def append(self,data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		end = self.head
		while (end.next):
			end = end.next
		end.next = new_node
	def insertAfter(self,prev,data):
		if prev is None:
			print("Node not in Linked List")
			return
		new_node = Node(data)
		new_node.next = prev.next
		prev.next = new_node
	def PrintList(self):
		temp = self.head
		while (temp):
			print(temp.data)
			temp = temp.next
if __name__ =='__main__':
	ll = LinkedList()
	ll.push(2)
	ll.push(5)
	ll.append(4)
	ll.insertAfter(ll.head,9)
	ll.PrintList()
