from lib3 import *

def Nrev(N):
	return int(str(N)[::-1])

def dasilva(N):
	Nv = Nrev(N)
	stop = False
	r = 2
	while not stop:
		if gcd(N, Nv+r) != 1:
			return gcd(N, Nv+r), int(N/gcd(N, Nv+r))
		if gcd(N, 2*Nv+r) != 1:
			return gcd(N, 2*Nv+r), int(N/gcd(N, 2*Nv+r))
		if gcd(N, Nv-r) != 1:
			return gcd(N, Nv-r), int(N/gcd(N, Nv-r))
		if gcd(N, 2*Nv-r) != 1:
			return gcd(N, 2*Nv-r), int(N/gcd(N, 2*Nv-r))
		if gcd(N, Nv*r+1) != 1:
			return gcd(N, Nv*r+1), int(N/gcd(N, Nv*r+1))
		if gcd(N, Nv*r+2) != 1:
			return gcd(N, Nv*r+2), int(N/gcd(N, Nv*r+2))
		if gcd(N, Nv*r-1) != 1:
			return gcd(N, Nv*r-1), int(N/gcd(N, Nv*r-1))
		if gcd(N, Nv*r-2) != 1:
			return gcd(N, Nv*r-2), int(N/gcd(N, Nv*r-2))
		r += 1

if __name__ == '__main__':
	N = 143
	print(dasilva(N))