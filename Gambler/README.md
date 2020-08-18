## Gambler

* 很好複習 sage 的一題
* 前面老掉牙的 POW 沒問題
* 看到題目的 encrypt func, 其中 m 可控要求 a, b, p
```
def encrypt(m, p, a, b):
    assert m < p and isPrime(p)
    return (m ** 3 + a * m + b) % p
```
* 廢話不多說 `m=0` 先把 b 帶出來
* 把前三個代入看看 這邊每個 k 都不相等
```
    a + b + 1  = kp + test(1) ... (1)
2 * a + b + 8  = kp + test(2) ... (2)
3 * a + b + 27 = kp + test(3) ... (3)
```
* 所以我們把 `m=i` 扣掉 `m=1` 的 `i` 倍移項一下 可以得到一個 `p` 的倍數
* 一個 for + GCD 逼出 p
```
p = 0
one = test(1)
for i in range(2, 11):
	p = GCD(p, i * one - test(i) - (i-1) * b + i**3 - i)
```
* 有了 `p` 前項減後項逼出 `a` 自然不是一件難事
```
a = 0
for i in range(1, 11):
	a = GCD(a, (test(i+1) - test(i) - (i+1)**3 + i**3) % p)
```
* 接下來是快樂的 sage 時間
* 我們知道 `(flag ** 3 + a * flag + b) % p = enc`
* 所以讓 sage 去解 `x ** 3 + a * x + b - enc` 在 `GF(p)` 時的解吧
```
f.<x> = PolynomialRing(GF(p))
f = x**3 + a*x + b - flag
f.roots()
```
* 還好 flag 夠小解得出來 XD
* `CCTF{__Gerolamo__Cardano_4N_itaLi4N_p0lYma7H}`