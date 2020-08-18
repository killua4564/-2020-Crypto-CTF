## Heaven

* 超暴力解這題XD
* 找一張正常的 jpg 看 header 的規定
* 把 header 和 enc 的前面做 xor 轉 2 進位
```
enc = BitArray(bytes=bytes(open('flag.enc', 'rb').read())).bin
header = BitArray(bytes=bytes(bytes.fromhex('FFD8FFE000104A464946000101'))).bin
oh, no = '0', '1'
ans = ''
for i, j in zip(header, enc):
	ans += oh if i == j else no
print(ans)
```
* 肉眼找規律得到 `len(elf) = 19`
* 說穿了 `born_to_die` 就是個 LFSR
* 暴力兩個 for new_testament 的長度和對應的排列組合
```
new_testament_list = []
for n in range(1, l+1):
	for i in itertools.combinations(list(range(l)), n):
		key = True
		for idx in range(len(register_header)-1):
			if ''.join(born_to_die_plus(list(register_header[idx]), list(i))) != register_header[idx+1]:
				key = False
				break
		if key: new_testament_list.append(list(i))
```
* 把每種可能都解密存成一張圖片 能看的那張就是 flag 了
```
for itr, new_testament in enumerate(new_testament_list):
	ans = ''
	elf = list(register_header[0])
	for idx in range(0, len(enc), l):
		for i, j in zip(enc[idx:idx+l], elf):
			ans += oh if i == j else no
		elf = born_to_die_plus(elf, new_testament)
	# itr = 260
	open(f'image/flag{itr}.jpg', 'wb').write(long_to_bytes(int(ans, 2)))
```
* `CCTF{0Ne_k3y_t0_rU1e_7hem_A11_4Nd_7o_d3crYp7_th3_fl4g!}`