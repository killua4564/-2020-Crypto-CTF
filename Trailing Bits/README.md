## Trailing Bits

* 題目說少了幾個 bit
* 那位移看看？反正前面後面壞掉也沒差
```
c = int(open('output.txt', 'rb').read().decode().strip(), 2)
for _ in range(10):
	c <<= 1
	print(long_to_bytes(c))
```
* `CCTF{it5_3n0u9h_jU5T_tO_sH1ft_M3}`