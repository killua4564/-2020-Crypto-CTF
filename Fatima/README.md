## Fatima

* 耗時間的一題
* 把 flag 對於 Curve 和 G Point 做相對應轉換後經過各種隨機的置換再乘上 CAL matrix
* 一樣畫葫蘆可以生出 C, enc 中的 CL[0] 可以知道 `l=38`
* 用個 for 去跑 a 然後把 B 乘上對應的反矩陣 (100個可能)
* 再跑過每個反置換的可能性 (5! = 120個可能)
* 總共也才 12萬種可能 代碼沒寫太差應該一下就有答案
```
dict_traversal = {
	1: spiral(a),
	2: revspiral(a),
	3: sinwaveform(a),
	4: helical(a),
	5: revhelical(a),
}

def inv(arr, A):
	B = [[0] * 100 for _ in range(100)]
	for i, row in enumerate(arr):
		for j, col in enumerate(row):
			B[col // 100][col % 100] = A[i][j]
	return np.array(B)

for a in range(2, len(B)+1):
	bt = B.dot(np.linalg.inv(pow_matrix(C, a)))
	for i in permutations(list(range(1, 6))):
		b = bt
		for item in i: b = inv(dict_traversal[item], b)
		flag = p2c(invmat(b))
		if b'CCTF{' in flag:
			print(flag)
			break
```
* 最後結果 `a=18`
* `CCTF{Elliptic_Curv3_1s_fun_&_simpLE_Circulaitng_it_make_it_funnier!!}`