class Stack(object):
	def __init__(self):
		"""初始化栈
		"""
		self.item_li = []
	
	def push(self, value):
		"""进栈
		"""
		self.item_li.append(value)
	
	def pull(self):
		"""出栈
		"""
		return self.item_li.pop()
	
	def is_empty(self):
		"""判断栈是否为空
		"""
		return self.item_li == []
	
	def size(self):
		"""返回栈大小
		"""
		return self.item_li.__len__()


if __name__ == '__main__':
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)
	print(s.pull())
	print(s.pull())
	print(s.pull())
