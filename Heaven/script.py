import itertools

from bitstring import BitArray
from Crypto.Util.number import long_to_bytes

enc = BitArray(bytes=bytes(open('flag.enc', 'rb').read())).bin

header = BitArray(bytes=bytes(bytes.fromhex('FFD8FFE000104A464946000101'))).bin

oh, no = '0', '1'

ans = ''
for i, j in zip(header, enc):
	ans += oh if i == j else no

l = 19
register_header = [ans[idx:idx+l] for idx in range(0, len(ans), l)][:-1]

'''
for idx in range(0, len(ans), l):
	print(' ' * (6 - idx//l) + ans[idx:idx+l])
'''

def born_to_die_plus(isengard, new_testament):
    luke = 0
    for book in new_testament:
        luke ^= ord(isengard[book])
    return ([oh] if luke == 0 else [no]) + isengard[:-1]

new_testament_list = []
for n in range(1, l+1):
	for i in itertools.combinations(list(range(l)), n):
		key = True
		for idx in range(len(register_header)-1):
			if ''.join(born_to_die_plus(list(register_header[idx]), list(i))) != register_header[idx+1]:
				key = False
				break
		if key: new_testament_list.append(list(i))

for itr, new_testament in enumerate(new_testament_list):
	ans = ''
	elf = list(register_header[0])
	for idx in range(0, len(enc), l):
		for i, j in zip(enc[idx:idx+l], elf):
			ans += oh if i == j else no
		elf = born_to_die_plus(elf, new_testament)

	# itr = 260
	open(f'image/flag{itr}.jpg', 'wb').write(long_to_bytes(int(ans, 2)))

# CCTF{0Ne_k3y_t0_rU1e_7hem_A11_4Nd_7o_d3crYp7_th3_fl4g!}

