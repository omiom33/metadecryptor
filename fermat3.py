from lib3 import *

def fermat(N):
	stop, a = False, int(ceil(sqrt(N)))
	while not stop:
		bsquare = a*a - N
		if is_square(bsquare):
			b = sqrt(bsquare)
			p = a - b
			q = a + b
			if p not in [1, N]:
				return p, q
		if a == N:
			stop = True
		a += 1

if __name__ == '__main__':
	N = 360942546576826817
	print('fermat (p, q):', fermat(N))