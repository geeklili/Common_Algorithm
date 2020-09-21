class Queue(object):
	def __init__(self):
		"""初始化队列
		"""
		self.item_li = []
	
	def enqueue(self, value):
		"""进队列
		"""
		self.item_li.insert(0, value)
	
	def dequeue(self):
		"""出队列
		"""
		return self.item_li.pop()
	
	def is_empty(self):
		"""判断队列是否为空
		"""
		return self.item_li == []
	
	def size(self):
		"""返回队列大小
		"""
		return self.item_li.__len__()


if __name__ == '__main__':
	q = Queue()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())
