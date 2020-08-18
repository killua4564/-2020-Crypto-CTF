import string
import hashlib
import itertools

from Crypto.Util.number import long_to_bytes, GCD
from pwn import *

conn = remote('05.cr.yp.toc.tf', '33371')

arr = conn.recvline().decode().split()
hashfunc, tailhash, l = arr[8].replace('(X)[-6:]', ''), arr[10], int(arr[-1])

if 'md5' == hashfunc: func = hashlib.md5 
elif 'sha1' == hashfunc: func = hashlib.sha1
elif 'sha224' == hashfunc: func = hashlib.sha224
elif 'sha256' == hashfunc: func = hashlib.sha256
elif 'sha384' == hashfunc: func = hashlib.sha384
elif 'sha512' == hashfunc: func = hashlib.sha512

for x in itertools.product(string.digits + string.ascii_letters, repeat=l):
	h = func(''.join(x).encode()).hexdigest()
	if h[-len(tailhash):] == tailhash:
		conn.sendline(''.join(x))
		break

def menu():
	conn.recvuntil('[Q]uit\n')

menu()
conn.sendline('c')
conn.recvuntil(' = ')
enc = int(conn.recvline().decode())

def test(x):
	conn.sendline('t')
	conn.recvuntil(':\n')
	conn.sendline(str(x).encode())
	conn.recvuntil(' = ')
	return int(conn.recvline().decode())

def get_args():
	a, b, p = 0, test(0), 0
	one = test(1)
	for i in range(2, 11):
		p = GCD(p, i * one - test(i) - (i-1) * b + i**3 - i)
	for i in range(1, 11):
		a = GCD(a, (test(i+1) - test(i) - (i+1)**3 + i**3) % p)
	return (a, b, p)

a, b, p = get_args()

print(f'''sage
a={a}
b={b}
p={p}
flag={enc}

f.<x> = PolynomialRing(GF(p))
f = x**3 + a*x + b - flag
f.roots()
''')

print(long_to_bytes(617070432649260050642098026592993401828847317345986217631876412154526214367005234669497025987379900553054333))

'''
def encrypt(m, p, a, b):
    assert m < p and isPrime(p)
    return (m ** 3 + a * m + b) % p

    a + b + 1  = kp + test(1)
2 * a + b + 8  = kp + test(2)
3 * a + b + 27 = kp + test(3)

p = GCD(2 * test(1) - test(2) - b + 6)

    a % p = test(1) - b - 1 % p
2 * a % p = test(2) - b - 8 % p
3 * a % p = test(3) - b - 27 % p

a = GCD(test(2) - test(1) - 8 + 1 % p)
'''
