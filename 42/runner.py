from wi import WordIterator
from tn import TriangleNumber

tn = TriangleNumber()
print tn.number('AAAA')
print tn.isTN(tn.number('SKY'))

it = WordIterator('words.txt')
for word in it:
	print word
	break
