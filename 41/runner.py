from prime import Prime
import itertools
import sys

p  = Pandigital()
result = None
numbers = '987654321'
for n in range(0,6):
	number = numbers[n:]
	for perm in itertools.permutations(number, len(number)):
		candidate = int(''.join(perm))
		if Prime.isprime(int(candidate)):
			result = candidate
			break
	if (result != None):
		break
print result
