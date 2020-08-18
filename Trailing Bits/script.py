from Crypto.Util.number import long_to_bytes

c = int(open('output.txt', 'rb').read().decode().strip(), 2)

for _ in range(10):
	c <<= 1
	print(long_to_bytes(c))