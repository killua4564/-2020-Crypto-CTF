
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

def inv_you(num, den):
	ans = []
	ans.append(num // den)
	num = num % den
	reducer = 1
	while True:
		reducer *= -1
		num, den = den * reducer, num
		ans.append(abs(num // den))
		num = num % den
		if num == 0:
			break
	return bytes(ans)

def inv_us(num, den):
	ans = []
	ans.append(num // den)
	num = num % den
	while True:
		num, den = den, num
		ans.append(abs(num // den))
		num = num % den
		if num == 0:
			break
	return bytes(ans)


enc = [
	(inv_us, 4874974328610108385835995981839358584964018454799387862, 72744608672130404216404640268150609115102538654479393),
	(inv_you, 39640220997840521464725453281273913920171987264976009809, 366968282179507143583456804992018400453304099650742276),
	(inv_me, 145338791483840102508854650881795321139259790204977, 1529712573230983998328149700664285268430918011078),
	(inv_me, 84704403065477663839636886654846156888046890191627, 717773708720775877427974283328022404459326394028),
	(inv_you, 287605888305597385307725138275886061497915866633976011, 8712550395581704680675139804565590824398265004367939)
]

flag = b''
for func, num, den in enc:
	flag += func(num, den)
print(flag)
