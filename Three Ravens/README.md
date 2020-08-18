## Three Ravens

* 太認真對待得一題..
* n 非常的大
* 如果 m 夠小可以不用找 phi(n)
* 只要找 phi(l) 其中 l|n 和 m < l
```
a = b (mod n)
a = b + kn
a = b + ktl (l|n ==> n = tl)

if a < l then
a = b (mod l)
```
* 把 l 代入 p + q + r 就結束了
```
pqr = 31678428119854378475039974072165136708037257624045332601158556362844808093636775192373992510841508137996049429030654845564354209680913299308777477807442821
d = inverse(e, pqr-1)
print(long_to_bytes(pow(enc, d, pqr)))
```
* `CCTF{tH3_thr3E_r4V3n5_ThRe3_cR0w5}`
* ref: [cryptohack](https://blog.cryptohack.org/cryptoctf2020#three-ravens)