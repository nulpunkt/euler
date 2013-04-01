import re

class WordIterator:
	def __init__(self, file):
		self.words = self.getWords(file)
		self.i = -1
		self.n = len(self.words)

	def getWords(self, file):
		f = open(file, 'r')
		words = f.read()
		return re.split('\W+', words)

	def __iter__(self):
		return self

	def next(self):
		self.i += 1
		if self.i >= self.n:
			raise StopIteration
		if self.words[self.i] != '':
			return self.words[self.i]
		else:
			return self.next()

