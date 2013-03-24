c = ' ';
i = 1
while len(c) < 1000001:
	c = c+str(i)
	i = i+1

print int(c[1])*int(c[10])*int(c[100])*int(c[1000])*int(c[10000])*int(c[100000])*int(c[1000000])
