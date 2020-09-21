class Node(object):
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def pre_order(node):
	"""前序遍历
	"""
	if not node:
		return
	print(node.value)
	pre_order(node.left)
	pre_order(node.right)


def mid_order(node):
	"""中序遍历
	"""
	if not node:
		return
	pre_order(node.left)
	print(node.value)
	pre_order(node.right)


def after_order(node):
	"""后序遍历
	"""
	if not node:
		return
	pre_order(node.left)
	pre_order(node.right)
	print(node.value)


def bfs(node):
	"""广度优先遍历,逐层遍历
	"""
	if not node:
		return
	layer_li = [node]
	while layer_li:
		next_layer_li = []
		for node in layer_li:
			print(node.value)
			if node.left:
				next_layer_li.append(node.left)
			if node.right:
				next_layer_li.append(node.right)
		
		layer_li = next_layer_li


nodeC = Node('C')
nodeE = Node('E')
nodeH = Node('H')
nodeA = Node('A')
nodeD = Node('D', nodeC, nodeE)
nodeB = Node('B', nodeA, nodeD)
nodeI = Node('I', nodeH)
nodeG = Node('G', None, nodeI)
nodeF = Node('F', nodeB, nodeG)

pre_order(nodeF)
bfs(nodeF)
