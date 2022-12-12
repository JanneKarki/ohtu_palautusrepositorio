from matchers import All, PlaysIn, And, HasAtLeast, HasFewerThan
from stack import Stack


class QueryBuilder:

	def __init__(self, *args):
		if not args:
			self.stack = Stack()
		else:
			self.stack = args[0]

	def build(self):
		if self.stack.empty():
			return All()
		else:
			objects = []
			while not self.stack.empty():
				objects.append(self.stack.pop())

		return And(*objects)


	def playsIn(self, team):
		self.stack.push(PlaysIn(team))
		return QueryBuilder(self.stack)

	def hasAtLeast(self, value, attr):
		self.stack.push(HasAtLeast(value, attr))
		return QueryBuilder(self.stack)

	def hasFewerThan(self, value, attr):
		self.stack.push(HasFewerThan(value, attr))
		return QueryBuilder(self.stack)