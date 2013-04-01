from wi import WordIterator
from tn import TriangleNumber

tn = TriangleNumber()
print 

it = WordIterator('words.txt')
ctn = 0
for word in it:
	if tn.isTN(tn.number(word)):
		ctn += 1
print ctn
