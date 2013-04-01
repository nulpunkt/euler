import itertools
import sys
from p import Pentagon

p  = Pentagon()
for i in range(1, 10000):
	for j in range(i, i+10000):
		pn = p.pn(i)
		pnn = p.pn(j)
		if p.isPentagon(pn+pnn) and p.isPentagon(pnn-pn):
			print pnn-pn
			sys.exit(0)
