import math
import itertools

def pow2(n):
	for i in range(1, n):
		yield math.pow(i,2)

bestP = 1
max = 0
for p in range(1, 1000):
	current = 0
	for a2 in pow2(500):
		for b2 in pow2(500):
			if a2 > b2:
				a = math.sqrt(a2)
				b = math.sqrt(b2)
				c = math.sqrt(a2+b2)
				if a+b+c == p:
					current = current + 1
	if current > max:
		max = current
		bestP = p

print bestP, max
