from pandigital import Pandigital
import itertools
import sys

p  = Pandigital()
result = None
for perm in itertools.permutations('987654321', 9):
	for i in range(1, 5):
		if(p.is_pandigital(''.join(perm), i)):
			result = (''.join(perm), i)
			break
	if (result != None):
		break
print result
