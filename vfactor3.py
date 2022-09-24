from lib3 import *

def LSB(decimal):
	return "odd" if bin(decimal).endswith('1') else "even"

def vfactor(N):
	root = int(floor(sqrt(N)))
	if LSB(root) == 'even':
		root -= 1
	y = root
	x = root + 2
	m = x*y

	while m!=N:
		if m<N:
			x += 2
		else:
			y -= 2
		m = x*y

	return x, y

if __name__ == '__main__':
	N = 4183
	print(vfactor(N))

	'''
	(89, 47)
	'''