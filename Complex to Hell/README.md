## Complex To Hell

* 當初為什麼沒想到這樣解QQ
* 把 flag 每兩個用 mapstr 對應成數字變成一個 complex
* 然後編成跟 key 的寬一樣高的 matrix 做相乘
* 也就是 `key * flag = cipher`
* 要解密就是 `flag = inv_key * cipher`
* 所以我們只需要找到 inv_key 就結束了
* 由 cipher 我們又得知 key 是個 2x2 matrix
```
Let inv_key = [
	[a+bj, c+dj],
	[e+fj, g+hj],
]
```
* 然後我們也知道 flag 的前四個字是 `CCTF` 所以我們可以得到
```
in Zmod(66)
24a + -36b + 33c + -44d = 38 # C
36a +  24b + 44c +  33d = 38 # C
41a + -47b + 15c + -39d = 55 # T
47a +  41b + 39c +  15d = 41 # F
```
* 這樣我們可以變成矩陣相乘解連立
```
A = Matrix(Zmod(66), [
	[ 24, -36,  33, -44],
	[ 36,  24,  44,  33],
	[ 41, -47,  15, -39],
	[ 47,  41,  39,  15],
])
B = vector(Zmod(66), [38, 38, 55, 41])
print(A.solve_right(B))
```
* 但要考慮到可能不只一種解
* 所以我選擇每兩個字/一組複數去嘗試能不能解 把能解到最後的再留下來
```
T = []   # key
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
```
* 如此一來可以得到兩組前半部的合理解 其中一個就是 flag `CCTF{This_0n3_Is_State_0f_th3_4rt_`
* 後半部可以由 `matrix_col_size = int(math.ceil(len(msg) // (2 * n))) + 1` 來知道結尾會有 1~4 個 0 的可能
* 先猜他是 `}000` 然後 `idx` 反過來寫 `solve_r`
```
T = []   # key
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
```
* 這樣可以得到四組後半的合理解 其中 flag 是 `and_C0mplex_is_Truly_compl3x!!}`
* 所以得到 flag: `CCTF{This_0n3_Is_State_0f_th3_4rt_and_C0mplex_is_Truly_compl3x!!}`
