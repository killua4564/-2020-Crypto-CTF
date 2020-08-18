from fastecdsa.curve import Curve
from fastecdsa.point import Point
from fatima import *
from output import enc
from itertools import permutations

import numpy as np

def p2c(b):
	try:
		return bytes(E[b[idx:idx+16]] for idx in range(0, len(b), 16))
	except: return b''

def invmat(A):
	ans = ''
	for row in A:
		for col in row:
			ans += bin(int(col))[2:].zfill(3)
	return ans

def pow_matrix(A, k):
	T = A
	for _ in range(k-1):
		A = A.dot(T)
	return A

def inv(arr, A):
	B = [[0] * 100 for _ in range(100)]
	for i, row in enumerate(arr):
		for j, col in enumerate(row):
			B[col // 100][col % 100] = A[i][j]
	return np.array(B)

CL0, B = enc

C = np.array(circulant([0 for i in range(len(B)-1)] + [1]))
CL = pow_matrix(C, 38)
B = np.array(B).dot(np.linalg.inv(CL))

a = np.array(list(range(10000))).reshape((100, 100))
dict_traversal = {
	1: spiral(a),
	2: revspiral(a),
	3: sinwaveform(a),
	4: helical(a),
	5: revhelical(a),
}

name = 'curve'.encode('utf-8')
p, a, b, q, gx, gy = 241, 173, 41, 256, 53, 192
curve = Curve(name, p, a, b, q, gx, gy)
G = Point(gx, gy, curve = curve)

E = {}
for k in range(256):
	P = k * G
	E[bin(P.x)[2:].zfill(8) + bin(P.y)[2:].zfill(8)] = k

for a in range(2, len(B)+1):
	bt = B.dot(np.linalg.inv(pow_matrix(C, a)))
	for i in permutations(list(range(1, 6))):
		b = bt
		for item in i: b = inv(dict_traversal[item], b)
		flag = p2c(invmat(b))
		if b'CCTF{' in flag:
			print(flag)
			break

