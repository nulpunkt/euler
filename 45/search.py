from numbers import Number

i = 286
number = Number()
while True:
	n = number.triangle(i)
	if (number.isPantagonal(n) and number.isHexagonal(n)):
		print n
		break

	i += 1
