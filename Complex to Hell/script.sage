'''
				cipher (mod 66)
inv_key	  
[a+bj, c+dj]	38+38j 55+41j
[e+fj, g+hj]
'''

mapstr = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!{}_"

cipher =  [
	[(24+36j), (41+47j), (3+27j), (36+41j), (57+58j), (11+24j), (33+7j), (52+64j), (26+23j), (30+35j), (64+39j), (52+19j), (39+45j), (33+31j), (3+17j), (21+32j), (15+55j)],
	[(33+44j), (15+39j), (64+50j), (44+41j), (39+20j), (0+42j), (16+12j), (63+27j), (9+52j), (39+64j), (5+18j), (53+25j), (47+31j), (5+49j), (24+8j), (57+9j), (38+16j)]
]

def copy(A):
	return [[item for item in row] for row in A]


T = []
def solve_l(A, B, idx, flag):
	global T
	if idx == 17:
		print(flag, T)
		return
	a, b = cipher[0][idx].real(), cipher[0][idx].imag()
	c, d = cipher[1][idx].real(), cipher[1][idx].imag()
	A.append([a, -b, c, -d])
	A.append([b,  a, d,  c])
	X = Matrix(Zmod(66), A)
	for i in range(66):
		for j in range(66):
			Y = vector(Zmod(66), B + [i, j])
			try:
				T = X.solve_right(Y)
				solve_l(copy(A), B + [i, j], idx + 1, flag + mapstr[i] + mapstr[j])
			except: pass

A = [
	[ 24, -36,  33, -44],
	[ 36,  24,  44,  33],
	[ 41, -47,  15, -39],
	[ 47,  41,  39,  15],
]
B = [38, 38, 55, 41]

solve_l(A, B, 2, 'CCTF')


T = []
def solve_r(A, B, idx, flag):
	global T
	if idx == -1:
		print(flag, T)
		return
	a, b = cipher[0][idx].real(), cipher[0][idx].imag()
	c, d = cipher[1][idx].real(), cipher[1][idx].imag()
	A.insert(0, [b,  a, d,  c])
	A.insert(0, [a, -b, c, -d])
	X = Matrix(Zmod(66), A)
	for i in range(66):
		for j in range(66):
			Y = vector(Zmod(66), [i, j] + B)
			try:
				T = X.solve_right(Y)
				solve_r(copy(A), [i, j] + B, idx - 1, mapstr[i] + mapstr[j] + flag)
			except: pass

A = [
	[ 21, -32,  57,  -9],
	[ 32,  21,   9,  57],
	[ 15, -55,  38, -16],
	[ 55,  15,  16,  38],
]
B = [64, 0, 0, 0]

solve_r(A, B, 14, '}')
