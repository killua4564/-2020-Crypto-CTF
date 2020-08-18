from Crypto.Util.number import long_to_bytes
from functools import reduce
import operator

def comb(n, k):
	if k > n :
		return 0
	k = min(k, n - k)
	u = reduce(operator.mul, range(n, n - k, -1), 1)
	d = reduce(operator.mul, range(1, k + 1), 1)
	return u // d 

enc = 5550332817876280162274999855997378479609235817133438293571677699650886802393479724923012712512679874728166741238894341948016359931375508700911359897203801700186950730629587624939700035031277025534500760060328480444149259318830785583493

m, c = 0, ''
while enc:
	c = str(enc % 3) + c
	enc //= 3

for item in c:
	if item == '1':
		m += 1
	elif item == '2':
		m -= 1
	m *= 2

m //= 2

m = list(bin(m)[2:])
n = len(m)
k = m.count('1') - 1
flag = 0
for idx, itr in enumerate(m):
	if idx == 0: continue
	if itr == '1':
		flag += comb(n - idx - 1, k)
		k -= 1
print(long_to_bytes(flag))


