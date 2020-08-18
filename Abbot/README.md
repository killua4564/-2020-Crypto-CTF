## Abbot

* 變數名稱和放的內容不一致的一題
* 把 me, you, us 的 inv func 寫出來剩下都不是難事
* you 和 us 沒什麼困難
* me 那邊的 reducer 如果反過來寫是要寫除 但是考慮 frac 會通分所以寫反向的乘會比較順
```
def inv_me(num, den):
	ans = []
	ans.append(num // den)
	num = num % den
	reducer = 0
	while True:
		reducer += 1
		num, den = den * reducer, num
		ans.append(num // den)
		num = num % den
		if num == 0:
			break
	return bytes(ans)
```
* 之後找到每個 enc 對應的 inv func 然後 concat 即可
* `CCTF{This_13_n0t_Arthur_Who_l0ves_Short_st0ries_This_IS___ASIS___Crypto_CTF____with_very_m0d3rn_arthur_Enc0d1ng!!_D0_you_Enj0y_IT_as_w311??}`