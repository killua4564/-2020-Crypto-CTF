## Amsterdam

* 加密倒的寫就變解密
* enc 轉成 3 進位依照規則可以還原出 m
```
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
```
* m 轉成 2 進位依照規則可以還原出 flag
```
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
```
* 途中 k 稍微猜一下就是
* `CCTF{With_Re3p3ct_for_Sch4lkwijk_dec3nt_Encoding!}`