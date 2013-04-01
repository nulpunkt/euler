import itertools
import sys
from div import Divisible

d  = Divisible()
n = 0
for perm in itertools.permutations('0123456789', 10):
	pandigital = ''.join(perm)
	if d.isDivisible(pandigital):
		n += int(pandigital)

print n
